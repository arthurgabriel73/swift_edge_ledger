from uuid import UUID

class MerchantId:
    def __init__(self, merchant_id: UUID):
        self._value = merchant_id

    def value(self) -> UUID:
        return self._value