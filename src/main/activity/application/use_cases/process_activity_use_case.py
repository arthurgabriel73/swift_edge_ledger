from uuid import uuid4, UUID
from typing import Optional
import logging
from src.main.activity.domain.activity import Activity
from src.main.activity.domain.activity_id import ActivityId
from src.main.activity.domain.activity_status import ActivityStatus
from src.main.shared.application.constants import CASH_CATEGORY_CODE
from src.main.activity.domain.account_balance import AccountBalance
from src.main.activity.application.ports.driven.account_balance_repository import AccountBalanceRepository
from src.main.activity.application.ports.driven.activity_repository import ActivityRepository
from src.main.activity.application.ports.driven.merchant_gateway import MerchantGateway
from src.main.activity.application.ports.driver.commands.process_activity_command import ProcessActivityCommand
from src.main.activity.application.ports.driver.commands.process_activity_command_output import ProcessActivityCommandOutput
from src.main.activity.application.ports.driver.process_activity_driver_port import ProcessActivityDriverPort


class ProcessActivityUseCase(ProcessActivityDriverPort):
    _merchant_id: UUID = None
    _account_balance: AccountBalance = None

    def __init__(self, activity_repository: ActivityRepository, merchant_gateway: MerchantGateway, account_balance_repository: AccountBalanceRepository):
        self.activity_repository = activity_repository
        self.merchant_gateway = merchant_gateway
        self.account_balance_repository = account_balance_repository

    def execute(self, command: ProcessActivityCommand) -> ProcessActivityCommandOutput:
        try:
            self._set_merchant_id(command.merchant)
            self._set_account_balance(command)
            result = self._process_activity(command.amount_in_cents)
            if not result and command.fallback:
                result = self._process_fallback(command)
            activity_status = ActivityStatus.APPROVED if result else ActivityStatus.REJECTED
            self._save_activity(command.amount_in_cents, activity_status)
            return ProcessActivityCommandOutput(code = activity_status)
        except Exception as e:
            logging.error(f"Error processing activity: {e}")
            self._save_activity(command.amount_in_cents, ActivityStatus.ERROR)
            return ProcessActivityCommandOutput(code=ActivityStatus.ERROR)

    def _set_merchant_id(self, merchant_name: str) -> None:
        merchant_id = self.merchant_gateway.find_merchant_id_by_name(merchant_name)
        if not merchant_id:
            raise ValueError(f"Merchant '{merchant_name}' not found")
        self._merchant_id = merchant_id

    def _set_account_balance(self, command: ProcessActivityCommand) -> None:
        category_id = self._get_category_id(command)
        if not category_id:
            raise ValueError(f"Category not found for MCC '{command.mcc}' or Merchant '{command.merchant}'")
        self._account_balance = self.account_balance_repository.find_by_account_and_category_id(command.account, category_id)

    def _get_category_id(self, command: ProcessActivityCommand) -> Optional[int]:
        if command.merchant_priority:
            if not command.merchant:
                raise ValueError("Merchant must be provided when merchant priority is enabled")
            merchant_category_id = self.merchant_gateway.get_category_id_by_merchant(command.merchant)
            if merchant_category_id: return merchant_category_id
        return self.merchant_gateway.get_category_id_by_mcc(command.mcc)

    def _process_activity(self, amount_in_cents: int) -> bool:
        if not self._account_balance: return False
        if not self._account_balance.withdraw(amount_in_cents):
            return False
        self.account_balance_repository.update_balance(self._account_balance)
        return True

    def _process_fallback(self, command: ProcessActivityCommand) -> bool:
        self._set_fallback_account_balance(command.account)
        if not self._account_balance: return False
        if not self._account_balance.withdraw(command.amount_in_cents):
            return False
        self.account_balance_repository.update_balance(self._account_balance)
        return True

    def _set_fallback_account_balance(self, account: str) -> Optional[AccountBalance]:
        cash_category_id = self.merchant_gateway.get_category_id_by_code(CASH_CATEGORY_CODE)
        self._account_balance = self.account_balance_repository.find_by_account_and_category_id(account, cash_category_id)

    def _save_activity(self, amount_in_cents: int, status: ActivityStatus) -> None:
        if not self._account_balance or not self._merchant_id: return
        self.activity_repository.save(Activity.create(
            activity_id=ActivityId(uuid4()),
            account_id=self._account_balance.account_id,
            amount_in_cents=amount_in_cents,
            category_id=self._account_balance.category_id,
            merchant_id=self._merchant_id,
            status=status
        ))