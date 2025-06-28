import uuid

import pytest

from src.main.activity.domain.activity import Activity
from src.main.activity.domain.activity_id import ActivityId
from src.main.shared.date_util import get_utc_now


class TestActivity:
    def test_use_constructor_outside_class(self):
        # Act & Assert
        with pytest.raises(RuntimeError, match='Use the create method to instantiate an Activity'):
            Activity(activity_id=ActivityId(uuid.uuid4()), timestamp=get_utc_now().timestamp(), account_id=uuid.uuid4(), amount_in_cents=1000, category_id=1, merchant_id=uuid.uuid4(), status_id=1)

    def test_use_create_method(self):
        # Arrange
        activity_id = ActivityId(uuid.uuid4())
        account_id = uuid.uuid4()
        amount_in_cents = 1000
        category_id = 1
        merchant_id = uuid.uuid4()

        # Act
        activity = Activity.create(activity_id, account_id, amount_in_cents, category_id, merchant_id)

        # Assert
        assert activity.id == activity_id
        assert activity.account_id == account_id
        assert activity.amount_in_cents == amount_in_cents
        assert activity.category_id == category_id
        assert activity.merchant_id == merchant_id
        assert activity.status_id is None
        assert activity.timestamp is not None

    def test_use_from_value_method(self):
        # Arrange
        activity_id = ActivityId(uuid.uuid4())
        timestamp = get_utc_now().timestamp()
        account_id = uuid.uuid4()
        amount_in_cents = 1000
        category_id = 1
        merchant_id = uuid.uuid4()
        status_id = 1

        # Act
        activity = Activity.from_value(activity_id=activity_id, timestamp=timestamp, account_id=account_id, amount_in_cents=amount_in_cents, category_id=category_id, merchant_id=merchant_id, status_id=status_id)

        # Assert
        assert activity.id == activity_id
        assert activity.timestamp == timestamp
        assert activity.account_id == account_id
        assert activity.amount_in_cents == amount_in_cents
        assert activity.category_id == category_id
        assert activity.merchant_id == merchant_id
        assert activity.status_id == status_id