from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from src.main.merchant.domain.category import Category
from src.main.merchant.domain.mcc import Mcc
from src.main.merchant.domain.mcc_id import MccId
from src.main.merchant.domain.merchant import Merchant
from src.main.merchant.domain.merchant_id import MerchantId
from src.main.merchant.domain.merchant_name import MerchantName

Base = declarative_base()
metadata = Base.metadata

from datetime import datetime
from uuid import UUID

from src.main.account.domain.account import Account
from src.main.account.domain.account_id import AccountId
from src.main.account.domain.account_number import AccountNumber
from sqlalchemy.orm import Mapped, mapped_column

class AccountEntity(Base):
    __tablename__ = 'accounts'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    account_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)

    def to_domain(self):
        return Account.from_value(
            account_id=AccountId(self.id),
            account_number=AccountNumber(self.account_number),
            created_at=self.created_at
        )

    @classmethod
    def from_domain(cls, account: Account) -> 'AccountEntity':
        return cls(
            id=account.id.value(),
            account_number=account.account_number.value(),
            created_at=account.created_at
        )

    def to_dict(self):
        return {
            'id': str(self.id),
            'account_number': self.account_number,
            'created_at': self.created_at.isoformat()
        }

class MerchantEntity(Base):
    __tablename__ = 'merchants'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    merchant_name: Mapped[str] = mapped_column(nullable=False, unique=True)
    mcc_id: Mapped[UUID] = mapped_column(ForeignKey("mcc.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)

    def to_domain(self):
        return Merchant.from_value(
            merchant_id=MerchantId(self.id),
            merchant_name=MerchantName(self.merchant_name),
            mcc_id=MccId(self.mcc_id),
            created_at=self.created_at
        )

    @classmethod
    def from_domain(cls, merchant: Merchant) -> 'MerchantEntity':
        return cls(
            id=merchant.id.value(),
            merchant_name=merchant.name.value(),
            mcc_id=merchant.mcc_id.value(),
            created_at=merchant.created_at
        )

    def to_dict(self):
        return {
            'id': str(self.id),
            'merchant_name': self.merchant_name,
            'mcc_id': self.mcc_id,
            'created_at': self.created_at.isoformat()
        }

class MccEntity(Base):
    __tablename__ = 'mcc'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(nullable=False, unique=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)

    def to_domain(self):
        return Mcc.from_value(
            mcc_id=MccId(self.id),
            code=self.code,
            category_id=self.category_id,
            created_at=self.created_at
        )

    @classmethod
    def from_domain(cls, mcc) -> 'MccEntity':
        return cls(
            id=mcc.id.value(),
            code=mcc.code,
            category_id=mcc.category_id,
            created_at=datetime.now()
        )

    def to_dict(self):
        return {
            'id': str(self.id),
            'code': self.code,
            'category_id': self.category_id,
            'created_at': self.created_at.isoformat()
        }

class CategoryEntity(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)

    def to_domain(self):
        return Category.from_value(
            category_id=self.id,
            code=self.code,
            description=self.description,
            created_at=self.created_at
        )

    @classmethod
    def from_domain(cls, category) -> 'CategoryEntity':
        return cls(
            id=category.id,
            code=category.code,
            description=category.description,
            created_at=category.created_at
        )

    def to_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }