from typing import Optional
from uuid import UUID

from sqlalchemy import Table
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from src.main.shared.database.sqlalchemy.models import AccountBalanceEntity, AccountEntity
from src.main.activity.application.ports.driven.account_balance_repository import AccountBalanceRepository
from src.main.activity.domain.account_balance import AccountBalance
from src.main.shared.persistence_decorators import repository


@repository
class SqlAlchemyAccountBalanceRepository(AccountBalanceRepository):


    def save(self, account_balance: AccountBalance, session: Optional[Session] = None) -> AccountBalance:
        if session is None:
            raise ValueError("Session must be provided for saving the account balance.")

        account_balance_entity = AccountBalanceEntity.from_domain(account_balance)
        table = Table('account_balances', AccountBalanceEntity.metadata)
        session.execute(table.insert(), [account_balance_entity.to_dict()])
        return account_balance_entity.to_domain()

    def find_by_account_and_category_id(self, account: str, category_id: int, session: Optional[Session] = None) -> Optional[AccountBalance]:
        if session is None:
            raise ValueError("Session must be provided for finding the account balance by account and category ID.")

        query = select(AccountBalanceEntity, AccountEntity.account_number).join(AccountEntity, AccountBalanceEntity.account_id == AccountEntity.id).where(
            AccountEntity.account_number == account,
            AccountBalanceEntity.category_id == category_id
        )
        account_balance_entity = session.execute(query).scalars().unique().one_or_none()
        if account_balance_entity is None:
            return None
        return account_balance_entity.to_domain()

    def find_by_account_id_and_category_id(self, account_id: UUID, category_id: int, session: Optional[Session] = None) -> Optional[AccountBalance]:
        if session is None:
            raise ValueError("Session must be provided for finding the account balance by account and category ID.")

        query = select(AccountBalanceEntity).where(
            AccountBalanceEntity.account_id == account_id,
            AccountBalanceEntity.category_id == category_id
        )
        account_balance_entity = session.execute(query).scalars().unique().one_or_none()
        if account_balance_entity is None:
            return None
        return account_balance_entity.to_domain()

    def update_balance(self, account_balance: AccountBalance, session: Optional[Session] = None) -> AccountBalance:
        if session is None:
            raise ValueError("Session must be provided for updating the account balance.")

        query = select(AccountBalanceEntity).where(AccountBalanceEntity.id == account_balance.id)
        account_balance_entity = session.execute(query).scalars().unique().one_or_none()
        if account_balance_entity is None:
            raise ValueError("Account balance must be provided for updating the account balance.")

        updated_account_balance_entity = AccountBalanceEntity.from_domain(account_balance)
        updated = session.query(AccountBalanceEntity).where(
            AccountBalanceEntity.id == account_balance.id,
            AccountBalanceEntity.version == (account_balance.version - 1)
        ).update(updated_account_balance_entity.to_dict())

        if updated == 0:
            raise ValueError("Failed to update account balance due to version conflict or not found.")

        return updated_account_balance_entity.to_domain()


