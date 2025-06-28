from abc import ABC, abstractmethod
from typing import Optional

from src.main.activity.domain.activity_status import ActivityStatus


class ActivityStatusRepository(ABC):
    pass

    @abstractmethod
    def save(self, status: ActivityStatus) -> ActivityStatus:
        pass

    @abstractmethod
    def find_by_id(self, status_id: int) -> Optional[ActivityStatus]:
        pass

    @abstractmethod
    def find_by_code(self, status: str) -> Optional[ActivityStatus]:
        pass