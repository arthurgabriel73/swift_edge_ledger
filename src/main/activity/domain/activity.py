from datetime import datetime
from uuid import UUID

from src.main.activity.domain.activity_status import ActivityStatus
from src.main.shared.date_util import get_utc_now
from src.main.activity.domain.activity_id import ActivityId


class Activity:
    __allow_instantiation = False

    def __init__(self, *, activity_id: ActivityId, timestamp: datetime.timestamp, account_id: UUID, amount_in_cents: int, category_id: int, merchant_id: UUID, status: ActivityStatus):
        if not self.__allow_instantiation:
            raise RuntimeError('Use the create method to instantiate an Activity')

        self.id = activity_id
        self.timestamp = timestamp
        self.account_id = account_id
        self.amount_in_cents = amount_in_cents
        self.category_id = category_id
        self.merchant_id = merchant_id
        self.status = status

    def approve(self) -> None:
        if self.status is not None:
            raise RuntimeError('Activity is already approved or rejected')
        self.status = ActivityStatus.APPROVED

    def reject(self) -> None:
        if self.status is not None:
            raise RuntimeError('Activity is already approved or rejected')
        self.status = ActivityStatus.REJECTED

    @classmethod
    def create(cls, activity_id: ActivityId, account_id: UUID, amount_in_cents: int, category_id: int, merchant_id: UUID, status: ActivityStatus) -> 'Activity':
        cls.__allow_instantiation = True
        return cls(activity_id=activity_id, timestamp=get_utc_now().timestamp(), account_id=account_id, amount_in_cents=amount_in_cents, category_id=category_id, merchant_id=merchant_id, status=status)

    @classmethod
    def from_value(cls, *, activity_id: ActivityId, timestamp: datetime.timestamp, account_id: UUID, amount_in_cents: int, category_id: int, merchant_id: UUID, status: ActivityStatus) -> 'Activity':
        cls.__allow_instantiation = True
        return cls(activity_id=activity_id, timestamp=timestamp, account_id=account_id, amount_in_cents=amount_in_cents, category_id=category_id, merchant_id=merchant_id, status=status)