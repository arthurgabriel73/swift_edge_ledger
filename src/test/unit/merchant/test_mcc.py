import uuid

import pytest

from src.main.merchant.domain.mcc import Mcc
from src.main.merchant.domain.mcc_id import MccId
from src.main.shared.date_util import get_utc_now



class TestMcc:
    def test_use_constructor_outside_class(self):
        # Act & Assert
        with pytest.raises(RuntimeError, match='Use the create method to instantiate a Mcc'):
            Mcc(code="5444", category_id=123, mcc_id=MccId(uuid.uuid4()), created_at=get_utc_now())

    def test_use_create_method(self):
        # Arrange
        mcc_id = MccId(uuid.uuid4())
        code = "5444"
        category_id = 123

        # Act
        mcc = Mcc.create(mcc_id, code, category_id)

        # Assert
        assert mcc.id == mcc_id
        assert mcc.code == code
        assert mcc.category_id == category_id
        assert mcc.created_at is not None

    def test_use_from_value_method(self):
        # Arrange
        mcc_id = MccId(uuid.uuid4())
        code = "5444"
        category_id = 123
        created_at = get_utc_now()

        # Act
        mcc = Mcc.from_value(mcc_id=mcc_id, code=code, category_id=category_id, created_at=created_at)

        # Assert
        assert mcc.id == mcc_id
        assert mcc.code == code
        assert mcc.category_id == category_id
        assert mcc.created_at == created_at