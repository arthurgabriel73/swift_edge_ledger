from abc import ABC, abstractmethod

from src.main.merchant.application.ports.driver.save_merchant_command import SaveMerchantCommand
from src.main.merchant.application.ports.driver.save_merchant_command_output import SaveMerchantCommandOutput


class SaveMerchantDriverPort(ABC):
    @abstractmethod
    def execute(self, command: SaveMerchantCommand) -> SaveMerchantCommandOutput:
        pass
