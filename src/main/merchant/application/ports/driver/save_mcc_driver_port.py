from abc import ABC, abstractmethod

from src.main.merchant.application.ports.driver.commands.save_mcc_command import SaveMccCommand
from src.main.merchant.application.ports.driver.commands.save_mcc_command_output import SaveMccCommandOutput


class SaveMccDriverPort(ABC):
    @abstractmethod
    def execute(self, command: SaveMccCommand) -> SaveMccCommandOutput:
        pass