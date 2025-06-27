from typing import Optional

from sqlalchemy import Table
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from src.main.shared.database.sqlalchemy.models import AccountEntity
from src.main.account.application.ports.driven.account_repository import AccountRepository
from src.main.account.domain.account import Account
from src.main.account.domain.account_id import AccountId
from src.main.account.domain.account_number import AccountNumber
from src.main.shared.persistence_decorators import repository


@repository
class SqlAlchemyAccountRepository(AccountRepository):
    def save(self, account: Account, session: Optional[Session] = None) -> Account:
        if session is None:
            raise ValueError("Session must be provided for saving the account.")

        account_entity = AccountEntity.from_domain(account)
        table = Table('accounts', AccountEntity.metadata)
        session.execute(table.insert(), [account_entity.to_dict()])
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
