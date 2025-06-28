class AccountNumber:
    def __init__(self, account_number: str):
        self._value = account_number

    def value(self) -> str:
        return self._value
