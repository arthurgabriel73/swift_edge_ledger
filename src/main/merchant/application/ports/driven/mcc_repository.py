from abc import ABC, abstractmethod
from typing import Optional

from src.main.merchant.domain.mcc import Mcc
from src.main.merchant.domain.mcc_id import MccId


class MccRepository(ABC):

    @abstractmethod
    def save(self, mcc: Mcc) -> Mcc:
        pass

    @abstractmethod
    def find_by_id(self, mcc_id: MccId) -> Optional[Mcc]:
        pass

    @abstractmethod
    def find_by_code(self, code: str) -> Optional[Mcc]:
        pass