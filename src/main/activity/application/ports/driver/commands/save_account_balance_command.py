from uuid import UUID


class SaveAccountBalanceCommand:
    def __init__(self, account_id: UUID, category_id: int, amount_in_cents: int):
        self.account_id = account_id
        self.category_id = category_id
        self.amount_in_cents = amount_in_cents

    @staticmethod
    def validate_account_id(account_id: UUID):
        if not isinstance(account_id, UUID):
            raise ValueError("Invalid account ID")

    @staticmethod
    def validate_category_id(category_id: int):
        if not isinstance(category_id, int) or category_id <= 0:
            raise ValueError("Category ID must be a positive integer")

    @staticmethod
    def validate_amount_in_cents(amount_in_cents: int):
        if not isinstance(amount_in_cents, int) or amount_in_cents < 0:
            raise ValueError("Amount in cents must be a non-negative integer")