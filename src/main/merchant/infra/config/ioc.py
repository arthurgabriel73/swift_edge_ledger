from functools import lru_cache

from src.main.merchant.application.use_cases.list_categories_use_case import ListCategoriesUseCase
from src.main.merchant.application.ports.driver.list_categories_driver_port import ListCategoriesDriverPort
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
    return SaveMerchantUseCase(merchant_repository=SqlAlchemyMerchantRepository(), mcc_repository=SqlAlchemyMccRepository())

@lru_cache
def save_mcc_driver_factory() -> SaveMccDriverPort:
    return SaveMccUseCase(mcc_repository=SqlAlchemyMccRepository(), category_repository=SqlAlchemyCategoryRepository())

@lru_cache
def save_category_driver_factory() -> SaveCategoryDriverPort:
    return SaveCategoryUseCase(category_repository=SqlAlchemyCategoryRepository())

@lru_cache
def list_categories_driver_factory() -> ListCategoriesDriverPort:
    return ListCategoriesUseCase(category_repository=SqlAlchemyCategoryRepository())