from uuid import UUID


class SaveAccountBalanceCommandOutput:
    def __init__(self,account_id: UUID, category_id: int, amount_in_cents: int):
        self.account_id = account_id
        self.category_id = category_id
        self.amount_in_cents = amount_in_cents
