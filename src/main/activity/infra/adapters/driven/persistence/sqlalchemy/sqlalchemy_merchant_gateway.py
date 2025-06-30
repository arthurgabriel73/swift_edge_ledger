from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Session

from src.main.shared.database.sqlalchemy.models import MerchantEntity, MccEntity, CategoryEntity
from src.main.shared.persistence_decorators import repository
from src.main.activity.application.ports.driven.merchant_gateway import MerchantGateway


@repository
class SqlAlchemyMerchantGateway(MerchantGateway):
    def find_merchant_id_by_name(self, merchant_name: str, session: Optional[Session] = None) -> Optional[UUID]:
        if session is None:
            raise ValueError("Session must be provided for finding the merchant ID by name.")

        query = session.query(MerchantEntity.id).filter(MerchantEntity.merchant_name == merchant_name)
        merchant_id = session.execute(query).scalars().unique().one_or_none()
        if merchant_id is None:
            return None
        return merchant_id if isinstance(merchant_id, UUID) else UUID(str(merchant_id))

    def get_category_id_by_merchant(self, merchant_name: str, session: Optional[Session] = None) -> Optional[int]:
        if session is None:
            raise ValueError("Session must be provided for getting the category ID by merchant name.")

        mcc_id_query = session.query(MerchantEntity.mcc_id).filter(MerchantEntity.merchant_name == merchant_name)
        mcc_id = session.execute(mcc_id_query).scalars().unique().one_or_none()
        if mcc_id is None:
            return None
        category_id_query = session.query(MccEntity.category_id).filter(MccEntity.id == mcc_id)
        category_id = session.execute(category_id_query).scalars().unique().one_or_none()
        if category_id is None:
            return None
        return category_id if isinstance(category_id, int) else category_id.value

    def get_category_id_by_mcc(self, mcc: str, session: Optional[Session] = None) -> Optional[int]:
        if session is None:
            raise ValueError("Session must be provided for getting the category ID by MCC.")

        query = session.query(MccEntity.category_id).filter(MccEntity.code == mcc)
        category_id = session.execute(query).scalars().unique().one_or_none()
        if category_id is None:
            return None
        return category_id if isinstance(category_id, int) else category_id.value

    def get_category_id_by_code(self, code: str, session: Optional[Session] = None) -> Optional[int]:
        if session is None:
            raise ValueError("Session must be provided for getting the category ID by code.")

        query = session.query(CategoryEntity.id).filter(CategoryEntity.code == code)
        category_id = session.execute(query).scalars().unique().one_or_none()
        if category_id is None:
            return None
        return category_id if isinstance(category_id, int) else category_id.value
