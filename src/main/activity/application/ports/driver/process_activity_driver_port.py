from abc import ABC, abstractmethod

from src.main.activity.application.ports.driver.process_activity_command import ProcessActivityCommand
from src.main.activity.application.ports.driver.process_activity_command_output import ProcessActivityCommandOutput


class ProcessActivityDriverPort(ABC):
    @abstractmethod
    def execute(self, command: ProcessActivityCommand) -> ProcessActivityCommandOutput:
        pass
