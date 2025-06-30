from typing import List

from src.main.merchant.application.ports.driven.category_repository import CategoryRepository
from src.main.merchant.application.ports.driver.list_categories_driver_port import ListCategoriesDriverPort
from src.main.merchant.domain.category import Category


class ListCategoriesUseCase(ListCategoriesDriverPort):
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def execute(self) -> List[Category]:
        return self.category_repository.list_all()