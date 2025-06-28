import uuid

import pytest

from main.merchant.domain.mcc_id import MccId
from main.merchant.domain.merchant import Merchant
from main.merchant.domain.merchant_id import MerchantId
from main.merchant.domain.merchant_name import MerchantName
from main.shared.date_util import get_utc_now


class TestMerchant:
    def test_use_constructor_outside_class(self):
        # Act & Assert
        with pytest.raises(RuntimeError, match='Use the create method to instantiate a Merchant'):
            Merchant(merchant_id=MerchantId(uuid.uuid4()), merchant_name=MerchantName("Test Merchant"), mcc_id=1232, created_at=get_utc_now())


    def test_use_create_method(self):
        # Arrange
        merchant_id = MerchantId(uuid.uuid4())
        merchant_name = MerchantName("Test Merchant")
        mcc_id = MccId(uuid.uuid4())

        # Act
        merchant = Merchant.create(merchant_id, merchant_name, mcc_id)

        # Assert
        assert merchant.id == merchant_id
        assert merchant.name == merchant_name
        assert merchant.mcc_id == mcc_id
        assert merchant.created_at is not None

