from datetime import datetime
from typing import Optional
from uuid import UUID

from main.shared.date_util import get_utc_now
from src.main.activity.domain.activity_id import ActivityId


class Activity:
    __allow_instantiation = False

    def __init__(self, activity_id: ActivityId, timestamp: datetime.timestamp, account_id: UUID, amount_in_cents: int, category_id: int, merchant_id: UUID, status_id: Optional[int]):
        if not self.__allow_instantiation:
            raise RuntimeError('Use the create method to instantiate an Activity')

        self.id = activity_id
        self.timestamp = timestamp
        self.account_id = account_id
        self.amount_in_cents = amount_in_cents
        self.category_id = category_id
        self.merchant_id = merchant_id
        self.status_id = status_id


    @classmethod
    def create(cls, activity_id: ActivityId, account_id: UUID, amount_in_cents: int, category_id: int, merchant_id: UUID) -> 'Activity':
        cls.__allow_instantiation = True
        return cls(activity_id, get_utc_now().timestamp(), account_id, amount_in_cents, category_id, merchant_id, None)

    @classmethod
    def from_value(cls, *, activity_id: ActivityId, timestamp: datetime.timestamp, account_id: UUID, amount_in_cents: int, category_id: int, merchant_id: UUID, status_id: int) -> 'Activity':
        cls.__allow_instantiation = True
        return cls(activity_id, timestamp, account_id, amount_in_cents, category_id, merchant_id, status_id)