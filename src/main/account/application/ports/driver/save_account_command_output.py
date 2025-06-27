from src.main.account.domain.account_id import AccountId
from src.main.account.domain.account_number import AccountNumber


class SaveAccountCommandOutput:
    def __init__(self, account_id: AccountId, account_number: AccountNumber):
        self.account_id = account_id.value().hex
        self.account_number = account_number.value()
