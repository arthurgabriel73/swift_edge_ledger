from datetime import datetime

from src.main.account.domain.account_id import AccountId
from src.main.shared.date_util import get_utc_now


class Account:
    __allow_instantiation = False

    def __init__(self, account_id: AccountId, created_at: datetime):
        if not self.__allow_instantiation:
            raise RuntimeError('Use the create method to instantiate an Account')

        self.id = account_id
        self.created_at = created_at

    @classmethod
    def create(cls, account_id: AccountId) -> 'Account':
        cls.__allow_instantiation = True
        return cls(account_id, get_utc_now())

    @classmethod
    def from_value(cls, *, account_id: AccountId, created_at: datetime) -> 'Account':
        cls.__allow_instantiation = True
        return cls(account_id, created_at)