from datetime import datetime
from typing import Optional

from src.main.shared.date_util import get_utc_now


class Category:
    __allow_instantiation = False

    def __init__(self, *, category_id: Optional[int], code: str, description: str, created_at: datetime):
        if not self.__allow_instantiation:
            raise RuntimeError('Use the create method to instantiate a Category')

        self.id = category_id
        self.code = code
        self.description = description
        self.created_at = created_at

    @classmethod
    def create(cls, code: str, description: str) -> 'Category':
        cls.__allow_instantiation = True
        return cls(category_id=None, code=code, description=description, created_at=get_utc_now())

    @classmethod
    def from_value(cls, *, category_id: int, code: str, description: str, created_at: datetime) -> 'Category':
        cls.__allow_instantiation = True
        return cls(category_id=category_id, code=code, description=description, created_at=created_at)