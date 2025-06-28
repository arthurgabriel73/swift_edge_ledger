from datetime import datetime
from typing import Optional

from main.shared.date_util import get_utc_now


class ActivityStatus:
    __allow_instantiation = False

    def __init__(self, *, status_id: Optional[int], code: str, description: str, created_at: datetime):
        if not self.__allow_instantiation:
            raise RuntimeError('Use the create method to instantiate an ActivityStatus')

        self.id = status_id
        self.code = code
        self.description = description
        self.created_at = created_at


    @classmethod
    def create(cls, code: str, description: str) -> 'ActivityStatus':
        cls.__allow_instantiation = True
        return cls(status_id=None, code=code, description=description, created_at=get_utc_now())

    @classmethod
    def from_value(cls, *, status_id: int, code: str, description: str, created_at: datetime) -> 'ActivityStatus':
        cls.__allow_instantiation = True
        return cls(status_id=status_id, code=code, description=description, created_at=created_at)

