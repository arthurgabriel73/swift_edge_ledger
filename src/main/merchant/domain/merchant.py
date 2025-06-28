from datetime import datetime

from main.shared.date_util import get_utc_now
from src.main.merchant.domain.mcc_id import MccId
from src.main.merchant.domain.merchant_name import MerchantName
from src.main.merchant.domain.merchant_id import MerchantId


class Merchant:
    __allow_instantiation = False

    def __init__(self, merchant_id: MerchantId, merchant_name: MerchantName, mcc_id: MccId, created_at: datetime):
        if not self.__allow_instantiation:
            raise RuntimeError('Use the create method to instantiate a Merchant')

        self.id = merchant_id
        self.name = merchant_name
        self.mcc_id = mcc_id
        self.created_at = created_at

    @classmethod
    def create(cls, merchant_id: MerchantId, merchant_name: MerchantName, mcc_id: MccId) -> 'Merchant':
        cls.__allow_instantiation = True
        return cls(merchant_id, merchant_name, mcc_id, get_utc_now())

    @classmethod
    def from_value(cls, *, merchant_id: MerchantId, merchant_name: MerchantName, mcc_id: MccId, created_at: datetime) -> 'Merchant':
        cls.__allow_instantiation = True
        return cls(merchant_id, merchant_name, mcc_id, created_at)