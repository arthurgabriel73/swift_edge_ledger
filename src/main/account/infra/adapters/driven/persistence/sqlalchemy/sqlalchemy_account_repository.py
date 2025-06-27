from typing import Optional

from sqlalchemy import Table
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from main.account.application.ports.driven.account_repository import AccountRepository
from main.account.domain.account import Account
from main.account.domain.account_id import AccountId
from main.account.domain.account_number import AccountNumber
from main.account.infra.adapters.driven.persistence.sqlalchemy.account_entity import AccountEntity


class SqlAlchemyAccountRepository(AccountRepository):
    def save(self, account: Account, session: Optional[Session] = None) -> Account:
        if session is None:
            raise ValueError("Session must be provided for saving the account.")

        account_entity = AccountEntity.from_domain(account)
        session.add(account_entity.from_domain(account))
        session.commit()
        session.refresh(account_entity)
        return account_entity.to_domain()


    def find_by_id(self, account_id: AccountId, session: Optional[Session] = None) -> Optional[Account]:
        if session is None:
            raise ValueError("Session must be provided for finding the account by ID.")

        query = select(AccountEntity).where(AccountEntity.id == account_id.value())
        account_entity = session.execute(query).scalars().unique().one_or_none()
        if account_entity is None:
            return None
        return account_entity.to_domain()

    def find_by_account_number(self, account_number: AccountNumber, session: Optional[Session] = None) -> Optional[Account]:
        if session is None:
            raise ValueError("Session must be provided for finding the account by account number.")

        query = select(AccountEntity).where(AccountEntity.account_number == account_number.value())
        account_entity = session.execute(query).scalars().unique().one_or_none()
        if account_entity is None:
            return None
        return account_entity.to_domain()
