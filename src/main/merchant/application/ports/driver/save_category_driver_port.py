from abc import ABC, abstractmethod

from src.main.merchant.application.ports.driver.commands.save_category_command import SaveCategoryCommand
from src.main.merchant.application.ports.driver.commands.save_category_command_output import SaveCategoryCommandOutput


class SaveCategoryDriverPort(ABC):
    @abstractmethod
    def execute(self, command: SaveCategoryCommand) -> SaveCategoryCommandOutput:
        pass