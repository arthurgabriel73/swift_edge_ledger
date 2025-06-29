from typing import Optional

from sqlalchemy.orm import Session

from src.main.activity.application.ports.driven.account_balance_repository import AccountBalanceRepository
from src.main.activity.domain.account_balance import AccountBalance
from src.main.shared.persistence_decorators import repository


@repository
class SqlAlchemyAccountBalanceRepository(AccountBalanceRepository):
    def save(self, account_balance: AccountBalance, session: Optional[Session] = None) -> AccountBalance:
        if session is None:
            raise ValueError("Session must be provided for saving the account balance.")

    def find_by_account_and_category_id(self, account: str, category_id: int, session: Optional[Session] = None) -> Optional[AccountBalance]:
        if session is None:
            raise ValueError("Session must be provided for finding the account balance by account and category ID.")

    def update_balance(self, account_balance: AccountBalance, session: Optional[Session] = None) -> AccountBalance:
        if session is None:
            raise ValueError("Session must be provided for updating the account balance.")
