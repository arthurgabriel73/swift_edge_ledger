from typing import List, Optional

from main.merchant.application.ports.driven.mcc_repository import MccRepository
from main.merchant.domain.mcc import Mcc
from main.merchant.domain.mcc_id import MccId


class InMemoryMccRepository(MccRepository):
    def __init__(self):
        self.mcc_list: List[Mcc] = []

    def save(self, mcc: Mcc) -> Mcc:
        self.mcc_list.append(self.to_new_instance(mcc))
        return self.to_new_instance(mcc)

    def find_by_id(self, mcc_id: MccId) -> Optional[Mcc]:
        found = next((mcc for mcc in self.mcc_list if mcc.id.value() == mcc_id.value()), None)
        return self.to_new_instance(found) if found else None

    def find_by_code(self, code: str) -> Optional[Mcc]:
        found = next((mcc for mcc in self.mcc_list if mcc.code == code), None)
        return self.to_new_instance(found) if found else None

    def to_new_instance(self, mcc: Mcc) -> Mcc:
        return Mcc.from_value(mcc_id=mcc.id, code=mcc.code, category_id=mcc.category_id)