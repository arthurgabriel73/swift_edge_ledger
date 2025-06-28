from typing import List, Optional

from src.main.merchant.application.ports.driven.category_repository import CategoryRepository
from src.main.merchant.domain.category import Category


class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self):
        self.categories: List[Category] = []

    def save(self, category: Category) -> Category:
        self.categories.append(self.to_new_instance(category))
        return self.to_new_instance(category)

    def find_by_id(self, category_id: int) -> Optional[Category]:
        found = next((category for category in self.categories if category.id == category_id), None)
        return self.to_new_instance(found) if found else None

    def find_by_code(self, code: str) -> Optional[Category]:
        found = next((category for category in self.categories if category.code == code), None)
        return self.to_new_instance(found) if found else None

    def to_new_instance(self, category: Category) -> Category:
        return Category.from_value(category_id=category.id, code=category.code, description=category.description, created_at=category.created_at)