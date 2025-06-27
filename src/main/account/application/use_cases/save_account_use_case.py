import uuid

from src.main.account.application.ports.driven.account_repository import AccountRepository
from src.main.account.application.ports.driver.save_account_command import SaveAccountCommand
from src.main.account.application.ports.driver.save_account_command_output import SaveAccountCommandOutput
from src.main.account.application.ports.driver.save_account_driver_port import SaveAccountDriverPort
from src.main.account.domain.account import Account
from src.main.account.domain.account_id import AccountId
from src.main.account.domain.account_number import AccountNumber


class SaveAccountUseCase(SaveAccountDriverPort):
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def execute(self, command: SaveAccountCommand) -> SaveAccountCommandOutput:
        self._require_account_number_does_not_exist(command.account_number)
        created_account: Account =  self.account_repository.save(Account.create(AccountId(uuid.uuid4()), AccountNumber(command.account_number)))
        return SaveAccountCommandOutput(created_account.id, created_account.account_number)


    def _require_account_number_does_not_exist(self, account_number: str):
        existing_account = self.account_repository.find_by_account_number(AccountNumber(account_number))
        if existing_account:
            raise ValueError(f"Account with number {account_number} already exists.") # TODO: Use a custom exception
