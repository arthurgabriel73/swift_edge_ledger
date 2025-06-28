from typing import List, Optional

from src.main.account.application.ports.driven.account_repository import AccountRepository
from src.main.account.domain.account import Account
from src.main.account.domain.account_id import AccountId
from src.main.account.domain.account_number import AccountNumber


class InMemoryAccountRepository(AccountRepository):
    def __init__(self):
        self.accounts: List[Account] = []

    def save(self, account: Account) -> Account:
        self.accounts.append(self.to_new_instance(account))
        return self.to_new_instance(account)

    def find_by_id(self, account_id: AccountId) -> Optional[Account]:
        found = next((account for account in self.accounts if account.id.value() == account_id.value()), None)
        return self.to_new_instance(found) if found else None

    def find_by_account_number(self, account_number: AccountNumber) -> Optional[Account]:
        found = next((account for account in self.accounts if account.account_number.value() == account_number.value()), None)
        return self.to_new_instance(found) if found else None

    def to_new_instance(self, account: Account) -> Account:
        return Account.from_value(account_id=account.id, account_number=account.account_number, created_at=account.created_at)