from datetime import datetime

from sqlalchemy import UUID

from main.account.domain.account import Account
from main.account.domain.account_id import AccountId
from main.account.domain.account_number import AccountNumber
from src.main.shared.base_entity import BaseEntity
from sqlalchemy.orm import Mapped, mapped_column

class AccountEntity(BaseEntity):
    __tablename__ = 'accounts'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    account_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime]

    def to_domain(self):
        return Account.from_value(
            account_id=AccountId(self.id),
            account_number=AccountNumber(self.account_number),
            created_at=self.created_at
        )

    @classmethod
    def from_domain(cls, account: Account) -> 'AccountEntity':
        return cls(
            id=account.id,
            account_number=account.account_number.value(),
            created_at=account.created_at
        )