import uuid

import pytest

from src.main.activity.domain.account_balance import AccountBalance


class TestAccountBalance:
    def test_use_constructor_outside_class(self):
        # Act & Assert
        with pytest.raises(RuntimeError, match='Use the create method to instantiate an AccountBalance'):
            AccountBalance(account_balance_id=1, account_id=uuid.uuid4(), category_id=2, amount_in_cents=10000, version=None)

    def test_use_create_method(self):
        # Arrange
        account_id = uuid.uuid4()
        category_id = 2
        amount_in_cents = 10000

        # Act
        account_balance = AccountBalance.create(account_id, category_id, amount_in_cents)

        # Assert
        assert account_balance.id is None
        assert account_balance.account_id == account_id
        assert account_balance.category_id == category_id
        assert account_balance.amount_in_cents == amount_in_cents
        assert account_balance.version is None

    def test_use_from_value_method(self):
        # Arrange
        account_balance_id = 1
        account_id = uuid.uuid4()
        category_id = 2
        amount_in_cents = 10000
        version = 1

        # Act
        account_balance = AccountBalance.from_value(account_balance_id=account_balance_id, account_id=account_id, category_id=category_id, amount_in_cents=amount_in_cents, version=version)

        # Assert
        assert account_balance.id == account_balance_id
        assert account_balance.account_id == account_id
        assert account_balance.category_id == category_id
        assert account_balance.amount_in_cents == amount_in_cents
        assert account_balance.version == version