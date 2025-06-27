from datetime import datetime

from sqlalchemy import UUID

from src.main.shared.base_entity import BaseEntity
from sqlalchemy.orm import Mapped, mapped_column

class AccountEntity(BaseEntity):
    __tablename__ = 'accounts'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    account_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime]
