from typing import Optional

from sqlalchemy import Table
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from src.main.merchant.application.ports.driven.mcc_repository import MccRepository
from src.main.merchant.domain.mcc import Mcc
from src.main.merchant.domain.mcc_id import MccId
from src.main.shared.database.sqlalchemy.models import MccEntity
from src.main.shared.persistence_decorators import repository


@repository
class SqlAlchemyMccRepository(MccRepository):
    def save(self, mcc: Mcc, session: Optional[Session] = None) -> Mcc:
        if session is None:
            raise ValueError("Session must be provided for saving the MCC.")

        mcc_entity = MccEntity.from_domain(mcc)
        table = Table('mcc', MccEntity.metadata)
        session.execute(table.insert(), [mcc_entity.to_dict()])
        return mcc_entity.to_domain()

    def find_by_id(self, mcc_id: MccId, session: Optional[Session] = None) -> Optional[Mcc]:
        if session is None:
            raise ValueError("Session must be provided for finding the MCC by ID.")

        query = select(MccEntity).where(MccEntity.id == mcc_id.value())
        mcc_entity = session.execute(query).scalars().unique().one_or_none()
        if mcc_entity is None:
            return None
        return mcc_entity.to_domain()

    def find_by_code(self, code: str, session: Optional[Session] = None) -> Optional[Mcc]:
        if not code:
            raise ValueError("Code must be provided for finding the MCC by code.")

        query = select(MccEntity).where(MccEntity.code == code)
        mcc_entity = session.execute(query).scalars().unique().one_or_none()
        if mcc_entity is None:
            return None
        return mcc_entity.to_domain()
