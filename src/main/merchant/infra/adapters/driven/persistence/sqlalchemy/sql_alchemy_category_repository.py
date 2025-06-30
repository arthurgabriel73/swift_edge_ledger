from typing import Optional

from sqlalchemy.future import select
from sqlalchemy.orm import Session

from src.main.merchant.application.ports.driven.category_repository import CategoryRepository
from src.main.merchant.domain.category import Category
from src.main.shared.database.sqlalchemy.models import CategoryEntity
from src.main.shared.persistence_decorators import repository


@repository
class SqlAlchemyCategoryRepository(CategoryRepository):
    def save(self, category: Category, session: Optional[Session] = None) -> Category:
        if session is None:
            raise ValueError("Session must be provided for saving the category.")

        category_entity = CategoryEntity.from_domain(category)
        session.add(category_entity)
        return category_entity.to_domain()

    def find_by_id(self, category_id: int, session: Optional[Session] = None) -> Optional[Category]:
        if session is None:
            raise ValueError("Session must be provided for finding the category by ID.")

        query = select(CategoryEntity).where(CategoryEntity.id == category_id)
        category_entity = session.execute(query).scalars().unique().one_or_none()
        if category_entity is None:
            return None
        return category_entity.to_domain()

    def find_by_code(self, code: str, session: Optional[Session] = None) -> Optional[Category]:
        if session is None:
            raise ValueError("Session must be provided for finding the category by code.")

        query = select(CategoryEntity).where(CategoryEntity.code == code)
        category_entity = session.execute(query).scalars().unique().one_or_none()
        if category_entity is None:
            return None
        return category_entity.to_domain()

    def list_all(self, session: Optional[Session] = None) -> list[Category]:
        if session is None:
            raise ValueError("Session must be provided for listing all categories.")

        query = select(CategoryEntity)
        category_entities = session.execute(query).scalars().all()
        return [category_entity.to_domain() for category_entity in category_entities]
