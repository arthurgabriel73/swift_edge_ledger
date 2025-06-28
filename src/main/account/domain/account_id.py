from uuid import UUID

class AccountId:
    def __init__(self, account_id: UUID):
        self._value = account_id

    def value(self) -> UUID:
        return self._value

