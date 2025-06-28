import pytest

from src.main.merchant.domain.category import Category
from src.main.shared.date_util import get_utc_now


class TestCategory:
    def test_use_constructor_outside_class(self):
        # Act & Assert
        with pytest.raises(RuntimeError, match='Use the create method to instantiate a Category'):
            Category(category_id=123, code="FOOD", description="A food category", created_at=get_utc_now())

    def test_use_create_method(self):
        # Arrange
        code = "FOOD"
        description = "A food category"

        # Act
        category = Category.create(code, description)

        # Assert
        assert category.id is None
        assert category.code == code
        assert category.description == description
        assert category.created_at is not None

    def test_use_from_value_method(self):
        # Arrange
        category_id = 123
        code = "FOOD"
        description = "A food category"
        created_at = get_utc_now()

        # Act
        category = Category.from_value(category_id=category_id, code=code, description=description, created_at=created_at)

        # Assert
        assert category.id == category_id
        assert category.code == code
        assert category.description == description
        assert category.created_at == created_at