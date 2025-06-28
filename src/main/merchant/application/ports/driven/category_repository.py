from abc import ABC, abstractmethod
from typing import Optional

from src.main.merchant.domain.category import Category


class CategoryRepository(ABC):
    pass

    @abstractmethod
    def save(self, category: Category) -> Category:
        pass

    @abstractmethod
    def find_by_id(self, category_id: int) -> Optional[Category]:
        pass

    @abstractmethod
    def find_by_code(self, code: str) -> Optional[Category]:
        pass