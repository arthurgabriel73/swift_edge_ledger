from typing import Optional
from uuid import UUID


class AccountBalance:
    __allow_instantiation = False

    def __init__(self, *, account_balance_id: Optional[int], account_id: UUID, category_id: int, amount_in_cents: int, version: Optional[int]):
        if not self.__allow_instantiation:
            raise RuntimeError('Use the create method to instantiate an AccountBalance')

        self.id = account_balance_id
        self.account_id = account_id
        self.category_id = category_id
        self.amount_in_cents = amount_in_cents
        self.version = version

    def withdraw(self, amount_in_cents: int) -> bool:
        if self._may_withdraw(amount_in_cents):
            self.amount_in_cents -= amount_in_cents
            self.version += 1
            return True
        return False

    def _may_withdraw(self, amount_in_cents: int) -> bool:
        return self.amount_in_cents >= amount_in_cents

    @classmethod
    def create(cls, account_id: UUID, category_id: int, amount_in_cents: int) -> 'AccountBalance':
        cls.__allow_instantiation = True
        return cls(account_balance_id=None, account_id=account_id, category_id=category_id, amount_in_cents=amount_in_cents, version=None)

    @classmethod
    def from_value(cls, *, account_balance_id: int, account_id: UUID, category_id: int, amount_in_cents: int, version: Optional[int]) -> 'AccountBalance':
        cls.__allow_instantiation = True
        return cls(account_balance_id=account_balance_id, account_id=account_id, category_id=category_id, amount_in_cents=amount_in_cents, version=version)