from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from src.main.activity.domain.account_balance import AccountBalance


class AccountBalanceRepository(ABC):

    @abstractmethod
    def save(self, account_balance: AccountBalance) -> AccountBalance:
        pass

    @abstractmethod
    def find_by_account_and_category_id(self, account: str, category_id: int) -> Optional[AccountBalance]:
        pass

    @abstractmethod
    def find_by_account_id_and_category_id(self, account_id: UUID, category_id: int) -> Optional[AccountBalance]:
        pass

    @abstractmethod
    def update_balance(self, account_balance: AccountBalance) -> AccountBalance:
        pass
