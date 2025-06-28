from typing import List, Optional

from src.main.merchant.domain.merchant_id import MerchantId
from src.main.merchant.domain.merchant_name import MerchantName
from src.main.merchant.application.ports.driven.merchant_repository import MerchantRepository
from src.main.merchant.domain.merchant import Merchant


class InMemoryMerchantRepository(MerchantRepository):
    def __init__(self):
        self.merchants: List[Merchant] = []

    def save(self, merchant: Merchant) -> Merchant:
        self.merchants.append(self.to_new_instance(merchant))
        return self.to_new_instance(merchant)

    def find_by_id(self, merchant_id: MerchantId) -> Optional[Merchant]:
        found = next((merchant for merchant in self.merchants if merchant.id.value() == merchant_id.value()), None)
        return self.to_new_instance(found) if found else None

    def find_by_merchant_name(self, merchant_name: MerchantName):
        found = next((merchant for merchant in self.merchants if merchant.name.value() == merchant_name.value()), None)
        return self.to_new_instance(found) if found else None

    def to_new_instance(self, merchant: Merchant):
        return Merchant.from_value(merchant_id=merchant.id, merchant_name=merchant.name, mcc_id=merchant.mcc_id, created_at=merchant.created_at)