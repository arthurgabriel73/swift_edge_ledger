from uuid import UUID

from src.main.account.application.ports.driven.account_repository import AccountRepository
from src.main.account.application.use_cases.exceptions.account_not_found_exception import AccountNotFoundException
from src.main.account.domain.account_id import AccountId
from src.main.activity.application.use_cases.exceptions.account_balance_conflict_exception import \
    AccountBalanceConflictException
from src.main.activity.domain.account_balance import AccountBalance
from src.main.merchant.application.ports.driven.category_repository import CategoryRepository
from src.main.merchant.application.use_cases.exceptions.category_not_found_exception import CategoryNotFoundException
from src.main.activity.application.ports.driven.account_balance_repository import AccountBalanceRepository
from src.main.activity.application.ports.driver.commands.save_account_balance_command import SaveAccountBalanceCommand
from src.main.activity.application.ports.driver.commands.save_account_balance_command_output import \
    SaveAccountBalanceCommandOutput
from src.main.activity.application.ports.driver.save_account_balance_driver_port import SaveAccountBalanceDriverPort


class SaveAccountBalanceUseCase(SaveAccountBalanceDriverPort):
    def __init__(self,
                 account_balance_repository: AccountBalanceRepository,
                 account_repository: AccountRepository,
                 category_repository: CategoryRepository
                 ) -> None:

        self.account_balance_repository = account_balance_repository
        self.account_repository = account_repository
        self.category_repository = category_repository

    def execute(self, command: SaveAccountBalanceCommand) -> SaveAccountBalanceCommandOutput:
        self._require_account_balance_does_not_exist(command.account_id, command.category_id)
        self._require_account_exists(command.account_id)
        self._require_category_exists(command.category_id)
        created_account_balance: AccountBalance = self.account_balance_repository.save(
            AccountBalance.create(
                account_id=command.account_id,
                category_id=command.category_id,
                amount_in_cents=command.amount_in_cents
            )
        )
        return SaveAccountBalanceCommandOutput(
            account_id=created_account_balance.account_id,
            category_id=created_account_balance.category_id,
            amount_in_cents=created_account_balance.amount_in_cents
        )


    def _require_account_balance_does_not_exist(self, account_id: UUID, category_id: int):
        existing_account_balance = self.account_balance_repository.find_by_account_id_and_category_id(account_id, category_id)
        if existing_account_balance:
            raise AccountBalanceConflictException(f"Account balance for account {account_id} and category {category_id} already exists.")

    def _require_account_exists(self, account_id: UUID):
        existing_account = self.account_repository.find_by_id(AccountId(account_id))
        if not existing_account:
            raise AccountNotFoundException(f"Account with ID {account_id} does not exist.")

    def _require_category_exists(self, category_id: int):
        existing_category = self.category_repository.find_by_id(category_id)
        if not existing_category:
            raise CategoryNotFoundException(f"Category with ID {category_id} does not exist.")