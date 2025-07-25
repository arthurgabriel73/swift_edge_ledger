import uuid

from src.main.merchant.application.ports.driven.mcc_repository import MccRepository
from src.main.merchant.application.use_cases.exceptions.mcc_not_found_exception import MccNotFoundException
from src.main.merchant.application.ports.driven.merchant_repository import MerchantRepository
from src.main.merchant.application.ports.driver.commands.save_merchant_command import SaveMerchantCommand
from src.main.merchant.application.ports.driver.commands.save_merchant_command_output import SaveMerchantCommandOutput
from src.main.merchant.application.ports.driver.save_merchant_driver_port import SaveMerchantDriverPort
from src.main.merchant.application.use_cases.exceptions.merchant_conflict_exception import MerchantConflictException
from src.main.merchant.domain.mcc_id import MccId
from src.main.merchant.domain.merchant import Merchant
from src.main.merchant.domain.merchant_id import MerchantId
from src.main.merchant.domain.merchant_name import MerchantName


class SaveMerchantUseCase(SaveMerchantDriverPort):
    def __init__(self, merchant_repository: MerchantRepository, mcc_repository: MccRepository):
        self.merchant_repository = merchant_repository
        self.mcc_repository = mcc_repository

    def execute(self, command: SaveMerchantCommand) -> SaveMerchantCommandOutput:
        self.require_merchant_name_does_not_exist(command.merchant_name)
        self.require_mcc_exists(command.mcc_id)
        created_merchant: Merchant = self.merchant_repository.save(
            Merchant.create(MerchantId(uuid.uuid4()), MerchantName(command.merchant_name), MccId(command.mcc_id))
        )
        return SaveMerchantCommandOutput(created_merchant.id, created_merchant.name)


    def require_merchant_name_does_not_exist(self, merchant_name: str):
        existing_merchant = self.merchant_repository.find_by_merchant_name(MerchantName(merchant_name))
        if existing_merchant:
            raise MerchantConflictException(f"Merchant with name {merchant_name} already exists.")

    def require_mcc_exists(self, mcc_id: uuid.UUID):
        existing_mcc = self.mcc_repository.find_by_id(MccId(mcc_id))
        if not existing_mcc:
            raise MccNotFoundException(f"MCC with ID {mcc_id} does not exist.")