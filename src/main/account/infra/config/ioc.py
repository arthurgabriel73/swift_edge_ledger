from functools import lru_cache

from src.main.account.application.ports.driver.save_account_driver_port import SaveAccountDriverPort
from src.main.account.application.use_cases.save_account_use_case import SaveAccountUseCase
from src.main.account.infra.adapters.driven.persistence.sqlalchemy.sqlalchemy_account_repository import \
    SqlAlchemyAccountRepository


@lru_cache
def save_account_driver_factory() -> SaveAccountDriverPort:
    return SaveAccountUseCase(account_repository=SqlAlchemyAccountRepository())