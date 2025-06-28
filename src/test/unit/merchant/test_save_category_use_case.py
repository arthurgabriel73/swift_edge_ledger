import pytest

from src.main.merchant.application.ports.driven.category_repository import CategoryRepository
from src.main.merchant.application.ports.driver.commands.save_category_command import SaveCategoryCommand
from src.main.merchant.application.use_cases.save_category_use_case import SaveCategoryUseCase
from src.main.merchant.infra.adapters.driven.persistence.in_memory_category_repository import InMemoryCategoryRepository


class TestSaveCategoryUseCase:
    category_repository: CategoryRepository
    sut: SaveCategoryUseCase

    @pytest.fixture
    def setup(self):
        self.category_repository = InMemoryCategoryRepository()
        self.sut = SaveCategoryUseCase(self.category_repository)

    def test_save_category_success(self, setup):
        # Arrange
        code = "FOOD"
        description = "A category for food-related expenses"
        command = SaveCategoryCommand(code=code,description=description)

        # Act
        output = self.sut.execute(command)

        # Assert
        assert output.category_id is not None
        assert output.code == code
        assert output.description == description

    def test_save_category_with_existing_code_raises_error(self, setup):
        # Arrange
        code = "FOOD"
        description = "A category for food-related expenses"
        self.sut.execute(SaveCategoryCommand(code=code, description=description))

        # Act & Assert
        with pytest.raises(Exception, match=f"Category with code {code} already exists."):
            self.sut.execute(SaveCategoryCommand(code=code, description="Another description"))