class SaveAccountCommand:
    def __init__(self, account_number: str):
        SaveAccountCommand.validate_account_number(account_number)
        self.account_number = account_number

    @staticmethod
    def validate_account_number(account_number: str):
        if not account_number or not isinstance(account_number, str):
            raise ValueError("Invalid account number")
        if len(account_number) < 10 or len(account_number) > 20:
            raise ValueError("Account number must be between 10 and 20 characters long")
