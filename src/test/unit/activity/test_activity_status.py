import pytest

from main.activity.domain.activity_status import ActivityStatus
from main.shared.date_util import get_utc_now


class TestActivityStatus:
    def test_use_constructor_outside_class(self):
        # Act & Assert
        with pytest.raises(RuntimeError, match='Use the create method to instantiate an ActivityStatus'):
            ActivityStatus(status_id=1, code="SUCCESS", description="Operation was successful", created_at=get_utc_now())

    def test_use_create_method(self):
        # Arrange
        code = "SUCCESS"
        description = "Operation was successful"

        # Act
        activity_status = ActivityStatus.create(code, description)

        # Assert
        assert activity_status.id is None
        assert activity_status.code == code
        assert activity_status.description == description
        assert activity_status.created_at is not None

    def test_use_from_value_method(self):
        # Arrange
        status_id = 1
        code = "SUCCESS"
        description = "Operation was successful"
        created_at = get_utc_now()

        # Act
        activity_status = ActivityStatus.from_value(status_id=status_id, code=code, description=description, created_at=created_at)

        # Assert
        assert activity_status.id == status_id
        assert activity_status.code == code
        assert activity_status.description == description
        assert activity_status.created_at == created_at