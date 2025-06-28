from uuid import UUID


class MccId:
    def __init__(self, mcc_id: UUID):
        self._value = mcc_id

    def value(self) -> UUID:
        return self._value