from uuid import UUID


class SaveAccountBalanceCommandOutput:
    def __init__(self, account_balance_id: int, account_id: UUID, category_id: int, amount_in_cents: int):
        self.account_balance_id = account_balance_id
        self.account_id = account_id
        self.category_id = category_id
        self.amount_in_cents = amount_in_cents
