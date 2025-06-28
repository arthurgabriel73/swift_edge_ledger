from typing import Optional

from sqlalchemy import Table
from sqlalchemy.orm import Session

from src.main.merchant.application.ports.driven.merchant_repository import MerchantRepository
from src.main.merchant.domain.merchant import Merchant
from src.main.shared.database.sqlalchemy.models import MerchantEntity
from src.main.shared.persistence_decorators import repository


@repository
class SqlAlchemyMerchantRepository(MerchantRepository):
    def save(self, merchant: Merchant, session: Optional[Session] = None) -> Merchant:
        if session is None:
            raise ValueError("Session must be provided for saving the merchant.")

        merchant_entity = MerchantEntity.from_domain(merchant)
        table = Table('merchants', MerchantEntity.metadata)
        session.execute(table.insert(), [merchant_entity.to_dict()])
        return merchant_entity.to_domain()