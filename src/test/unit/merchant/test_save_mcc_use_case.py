import pytest

from src.main.merchant.application.use_cases.exceptions.category_not_found_exception import CategoryNotFoundException
from src.main.merchant.domain.category import Category
from src.main.merchant.infra.adapters.driven.persistence.in_memory_category_repository import InMemoryCategoryRepository
from src.main.merchant.application.ports.driven.category_repository import CategoryRepository
from src.main.merchant.application.ports.driven.mcc_repository import MccRepository
from src.main.merchant.application.ports.driver.commands.save_mcc_command import SaveMccCommand
from src.main.merchant.application.use_cases.save_mcc_use_case import SaveMccUseCase
from src.main.merchant.infra.adapters.driven.persistence.in_memory_mcc_repository import InMemoryMccRepository


class TestSaveMccUseCase:
    mcc_repository: MccRepository
    category_repository: CategoryRepository
    sut: SaveMccUseCase

    @pytest.fixture
    def setup(self):
        self.mcc_repository = InMemoryMccRepository()
        self.category_repository = InMemoryCategoryRepository()
        self.sut = SaveMccUseCase(self.mcc_repository, self.category_repository)

    def test_save_mcc_success(self, setup):
        # Arrange
        code = "5444"
        category = Category.create('FOOD', 'Test Category')
        self.category_repository.save(category)
        command = SaveMccCommand(code=code, category_id=category.id)

        # Act
        output = self.sut.execute(command)

        # Assert
        assert output.mcc_id is not None
        assert output.code == code
        assert output.category_id == category.id

    def test_save_mcc_with_existing_code_raises_error(self, setup):
        # Arrange
        code = "5444"
        category = Category.create('FOOD', 'Test Category')
        self.category_repository.save(category)
        self.sut.execute(SaveMccCommand(code=code, category_id=category.id))

        # Act & Assert
        with pytest.raises(Exception, match=f"MCC with code {code} already exists."):
            self.sut.execute(SaveMccCommand(code=code, category_id=category.id))

    def test_save_mcc_with_nonexisting_category_raises_error(self, setup):
        # Arrange
        code = "5444"
        category_id = 123

        # Act & Assert
        with pytest.raises(CategoryNotFoundException, match=f"ApplicationException: Category with ID {category_id} does not exist."):
            self.sut.execute(SaveMccCommand(code=code, category_id=category_id))

