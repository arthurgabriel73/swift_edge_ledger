from abc import ABC, abstractmethod

from src.main.account.application.ports.driver.save_account_command import SaveAccountCommand
from src.main.account.application.ports.driver.save_account_command_output import SaveAccountCommandOutput


class SaveAccountDriverPort(ABC):
    @abstractmethod
    def execute(self, command: SaveAccountCommand) -> SaveAccountCommandOutput:
        pass