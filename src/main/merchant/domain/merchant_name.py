class MerchantName:
    def __init__(self, name: str):
        if not name or name.strip() == "":
            raise ValueError("Merchant name cannot be empty")
        self._value = name

    def value(self) -> str:
        return self._value
