class ProcessActivityCommand:
    def __init__(self, account: str, amount_in_cents: int, mcc: str, merchant: str):
        self.account = account
        self.amount_in_cents = amount_in_cents
        self.mcc = mcc
        self.merchant = merchant

    @staticmethod
    def validate_account(account: str):
        if not account or not isinstance(account, str):
            raise ValueError("Invalid account")

    @staticmethod
    def validate_amount_in_cents(amount_in_cents: int):
        if not isinstance(amount_in_cents, int) or amount_in_cents <= 0:
            raise ValueError("Amount in cents must be a positive integer")

    @staticmethod
    def validate_mcc(mcc: str):
        if not mcc or not isinstance(mcc, str):
            raise ValueError("Invalid MCC")
        if len(mcc) != 4:
            raise ValueError("MCC code must be 4 characters long")

    @staticmethod
    def validate_merchant(merchant: str):
        if not merchant or not isinstance(merchant, str):
            raise ValueError("Invalid merchant")
        if len(merchant) < 3 or len(merchant) > 100:
            raise ValueError("Merchant name must be between 3 and 100 characters long")