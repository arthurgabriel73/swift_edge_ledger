from datetime import datetime

from src.main.shared.date_util import get_utc_now
from src.main.merchant.domain.mcc_id import MccId


class Mcc:
    __allow_instantiation = False

    def __init__(self, mcc_id: MccId, code: str, category_id: int, created_at: datetime):
        if not self.__allow_instantiation:
            raise RuntimeError('Use the create method to instantiate a Mcc')

        self.id = mcc_id
        self.code = code
        self.category_id = category_id
        self.created_at = created_at

    @classmethod
    def create(cls, mcc_id: MccId, code: str, category_id: int) -> 'Mcc':
        cls.__allow_instantiation = True
        return cls(mcc_id, code, category_id, get_utc_now())

    @classmethod
    def from_value(cls, *, mcc_id: MccId, code: str, category_id: int, created_at: datetime) -> 'Mcc':
        cls.__allow_instantiation = True
        return cls(mcc_id, code, category_id, created_at)

