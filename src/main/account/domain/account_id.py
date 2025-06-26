from uuid import UUID

class AccountId:
    def __init__(self, account_id: UUID):
        self.id = account_id

    def string(self) -> str:
        return str(self.id)
