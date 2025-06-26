from datetime import datetime

from src.main.account.domain.account_id import AccountId
from src.main.account.domain.account_number import AccountNumber
from src.main.shared.date_util import get_utc_now


class Account:
    __allow_instantiation = False

    def __init__(self, account_id: AccountId, account_number: AccountNumber, created_at: datetime):
        if not self.__allow_instantiation:
            raise RuntimeError('Use the create method to instantiate an Account')

        self.id = account_id
        self.account_number = account_number
        self.created_at = created_at

    @classmethod
    def create(cls, account_id: AccountId, account_number: AccountNumber) -> 'Account':
        cls.__allow_instantiation = True
        return cls(account_id, account_number, get_utc_now())

    @classmethod
    def from_value(cls, *, account_id: AccountId, account_number: AccountNumber, created_at: datetime) -> 'Account':
        cls.__allow_instantiation = True
        return cls(account_id, account_number, created_at)