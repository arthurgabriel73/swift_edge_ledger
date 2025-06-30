from abc import abstractmethod, ABC

from src.main.activity.application.ports.driver.commands.save_account_balance_command import SaveAccountBalanceCommand
from src.main.activity.application.ports.driver.commands.save_account_balance_command_output import \
    SaveAccountBalanceCommandOutput


class SaveAccountBalanceDriverPort(ABC):
    @abstractmethod
    def execute(self, command: SaveAccountBalanceCommand) -> SaveAccountBalanceCommandOutput:
        pass