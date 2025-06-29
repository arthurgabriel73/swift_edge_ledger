from src.main.activity.application.ports.driver.process_activity_driver_port import ProcessActivityDriverPort
from src.main.activity.application.use_cases.process_activity_use_case import ProcessActivityUseCase
from src.main.activity.infra.adapters.driven.persistence.sqlalchemy.sqlalchemy_account_balance_repository import \
    SqlAlchemyAccountBalanceRepository
from src.main.activity.infra.adapters.driven.persistence.sqlalchemy.sqlalchemy_activity_repository import \
    SqlAlchemyActivityRepository
from src.main.activity.infra.adapters.driven.persistence.sqlalchemy.sqlalchemy_merchant_gateway import \
    SqlAlchemyMerchantGateway


def process_activity_driver_factory() -> ProcessActivityDriverPort:
    return ProcessActivityUseCase(
        activity_repository=SqlAlchemyActivityRepository(),
        merchant_gateway=SqlAlchemyMerchantGateway(),
        account_balance_repository=SqlAlchemyAccountBalanceRepository()
    )