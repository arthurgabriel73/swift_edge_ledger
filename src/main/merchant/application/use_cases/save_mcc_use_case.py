import uuid

from src.main.merchant.application.ports.driven.mcc_repository import MccRepository
from src.main.merchant.application.ports.driver.commands.save_mcc_command import SaveMccCommand
from src.main.merchant.application.ports.driver.commands.save_mcc_command_output import SaveMccCommandOutput
from src.main.merchant.application.ports.driver.save_mcc_driver_port import SaveMccDriverPort
from src.main.merchant.application.use_cases.exceptions.mcc_conflict_exception import MccConflictException
from src.main.merchant.domain.mcc import Mcc
from src.main.merchant.domain.mcc_id import MccId


class SaveMccUseCase(SaveMccDriverPort):
    def __init__(self, mcc_repository: MccRepository):
        self.mcc_repository = mcc_repository

    def execute(self, command: SaveMccCommand) -> SaveMccCommandOutput:
        self.require_mcc_code_does_not_exist(command.code)
        created_mcc = self.mcc_repository.save(Mcc.create(MccId(uuid.uuid4()), command.code, command.category_id))
        return SaveMccCommandOutput(created_mcc.id, created_mcc.code, created_mcc.category_id)

    def require_mcc_code_does_not_exist(self, code: str):
        existing_mcc = self.mcc_repository.find_by_code(code)
        if existing_mcc:
            raise MccConflictException(f"MCC with code {code} already exists.")