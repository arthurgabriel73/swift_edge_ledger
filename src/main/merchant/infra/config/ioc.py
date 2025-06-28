from functools import lru_cache

from src.main.merchant.application.ports.driver.save_category_driver_port import SaveCategoryDriverPort
from src.main.merchant.application.use_cases.save_category_use_case import SaveCategoryUseCase
from src.main.merchant.infra.adapters.driven.persistence.sqlalchemy.sql_alchemy_category_repository import \
    SqlAlchemyCategoryRepository
from src.main.merchant.application.use_cases.save_mcc_use_case import SaveMccUseCase
from src.main.merchant.infra.adapters.driven.persistence.sqlalchemy.sql_alchemy_mcc_repository import \
    SqlAlchemyMccRepository
from src.main.merchant.application.ports.driver.save_mcc_driver_port import SaveMccDriverPort
from src.main.merchant.application.ports.driver.save_merchant_driver_port import SaveMerchantDriverPort
from src.main.merchant.application.use_cases.save_merchant_use_case import SaveMerchantUseCase
from src.main.merchant.infra.adapters.driven.persistence.sqlalchemy.sqlalchemy_merchant_repository import \
    SqlAlchemyMerchantRepository


@lru_cache
def save_merchant_driver_factory() -> SaveMerchantDriverPort:
    return SaveMerchantUseCase(merchant_repository=SqlAlchemyMerchantRepository())

@lru_cache
def save_mcc_driver_factory() -> SaveMccDriverPort:
    return SaveMccUseCase(mcc_repository=SqlAlchemyMccRepository())

@lru_cache
def save_category_driver_factory() -> SaveCategoryDriverPort:
    return SaveCategoryUseCase(category_repository=SqlAlchemyCategoryRepository())