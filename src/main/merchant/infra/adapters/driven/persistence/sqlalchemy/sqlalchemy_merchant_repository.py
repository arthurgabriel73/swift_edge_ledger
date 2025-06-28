from typing import Optional

from sqlalchemy import Table
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from src.main.merchant.domain.merchant_id import MerchantId
from src.main.merchant.domain.merchant_name import MerchantName
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

    def find_by_id(self, merchant_id: MerchantId, session: Optional[Session] = None) -> Optional[Merchant]:
        if session is None:
            raise ValueError("Session must be provided for finding the merchant by ID.")

        query = select(MerchantEntity).where(MerchantEntity.id == merchant_id.value())
        merchant_entity = session.execute(query).scalars().unique().one_or_none()
        if merchant_entity is None:
            return None
        return merchant_entity.to_domain()

    def find_by_merchant_name(self, merchant_name: MerchantName, session: Optional[Session] = None) -> Optional[Merchant]:
        if session is None:
            raise ValueError("Session must be provided for finding the merchant by name.")

        query = select(MerchantEntity).where(MerchantEntity.merchant_name == merchant_name.value())
        merchant_entity = session.execute(query).scalars().unique().one_or_none()
        if merchant_entity is None:
            return None
        return merchant_entity.to_domain()