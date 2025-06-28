from abc import abstractmethod, ABC
from typing import Optional

from src.main.merchant.domain.merchant_id import MerchantId
from src.main.merchant.domain.merchant_name import MerchantName
from src.main.merchant.domain.merchant import Merchant


class MerchantRepository(ABC):
    pass

    @abstractmethod
    def save(self, merchant: Merchant) -> Merchant:
        pass

    @abstractmethod
    def find_by_id(self, merchant_id: MerchantId) -> Optional[Merchant]:
        pass

    @abstractmethod
    def find_by_merchant_name(self, merchant_name: MerchantName) -> Optional[Merchant]:
        pass