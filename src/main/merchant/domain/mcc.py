from src.main.merchant.domain.mcc_id import MccId


class Mcc:
    __allow_instantiation = False

    def __init__(self, mcc_id: MccId, code: str, category_id: int):
        if not self.__allow_instantiation:
            raise RuntimeError('Use the create method to instantiate an Mcc')

        self.id = mcc_id
        self.code = code
        self.category_id = category_id

    @classmethod
    def create(cls, mcc_id: MccId, code: str, category_id: int) -> 'Mcc':
        cls.__allow_instantiation = True
        return cls(mcc_id, code, category_id)

    @classmethod
    def from_value(cls, *, mcc_id: MccId, code: str, category_id: int) -> 'Mcc':
        cls.__allow_instantiation = True
        return cls(mcc_id, code, category_id)

