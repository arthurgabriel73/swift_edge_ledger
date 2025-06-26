import uuid

import pytest

from src.main.account.domain.account import Account
from src.main.account.domain.account_id import AccountId
from src.main.shared.date_util import get_utc_now


class TestAccount:
    def test_use_constructor_outside_class(self):
        # Act & Assert
        with pytest.raises(RuntimeError, match='Use the create method to instantiate an Account'):
            Account(account_id = AccountId(uuid.uuid4()), created_at=get_utc_now())

    def test_use_create_method(self):
        # Arrange
        account_id = AccountId(uuid.uuid4())

        # Act
        account = Account.create(account_id)

        # Assert
        assert account.id == account_id
        assert account.created_at is not None

    def test_use_from_value_method(self):
        # Arrange
        account_id = AccountId(uuid.uuid4())
        created_at = get_utc_now()

        # Act
        account = Account.from_value(account_id=account_id, created_at=created_at)

        # Assert
        assert account.id == account_id
        assert account.created_at == created_at