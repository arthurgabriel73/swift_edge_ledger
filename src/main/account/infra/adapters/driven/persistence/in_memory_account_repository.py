from typing import List

from src.main.account.application.ports.driven.account_repository import AccountRepository
from src.main.account.domain.account import Account


class InMemoryAccountRepository(AccountRepository):
    def __init__(self):
        self.accounts: List[Account] = []

    def save(self, account) -> Account:
        self.accounts.append(self.to_new_instance(account))
        return self.to_new_instance(account)

    def find_by_id(self, account_id):
        found = next((account for account in self.accounts if account.id == account_id), None)
        return self.to_new_instance(found) if found else None

    def find_by_account_number(self, account_number):
        found = next((account for account in self.accounts if account.account_number == account_number), None)
        return self.to_new_instance(found) if found else None

    def to_new_instance(self, account: Account) -> Account:
        return Account.from_value(account_id=account.id, account_number=account.account_number, created_at=account.created_at)