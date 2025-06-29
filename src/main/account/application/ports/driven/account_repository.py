from abc import ABC, abstractmethod
from typing import Optional

from src.main.account.domain.account import Account
from src.main.account.domain.account_id import AccountId
from src.main.account.domain.account_number import AccountNumber


class AccountRepository(ABC):

    @abstractmethod
    def save(self, account: Account) -> Account:
        pass

    @abstractmethod
    def find_by_id(self, account_id: AccountId) -> Optional[Account]:
        pass

    @abstractmethod
    def find_by_account_number(self, account_number: AccountNumber) -> Optional[Account]:
        pass
