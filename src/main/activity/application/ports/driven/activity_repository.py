from abc import ABC, abstractmethod
from typing import Optional

from src.main.activity.domain.activity import Activity
from src.main.activity.domain.activity_id import ActivityId


class ActivityRepository(ABC):
    pass

    @abstractmethod
    def save(self, activity: Activity) -> Activity:
        pass

    @abstractmethod
    def find_by_id(self, activity_id: ActivityId) -> Optional[Activity]:
        pass