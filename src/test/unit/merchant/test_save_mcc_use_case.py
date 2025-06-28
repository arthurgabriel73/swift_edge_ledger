import pytest

from main.merchant.application.ports.driven.mcc_repository import MccRepository
from main.merchant.application.ports.driver.commands.save_mcc_command import SaveMccCommand
from main.merchant.application.use_cases.save_mcc_use_case import SaveMccUseCase
from main.merchant.infra.adapters.driven.persistence.in_memory_mcc_repository import InMemoryMccRepository


class TestSaveMccUseCase:
    mcc_repository: MccRepository
    sut: SaveMccUseCase

    @pytest.fixture
    def setup(self):
        self.mcc_repository = InMemoryMccRepository()
        self.sut = SaveMccUseCase(self.mcc_repository)

    def test_save_mcc_success(self, setup):
        # Arrange
        code = "5444"
        category_id = 123
        command = SaveMccCommand(code=code, category_id=category_id)

        # Act
        output = self.sut.execute(command)

        # Assert
        assert output.mcc_id is not None
        assert output.code == code
        assert output.category_id == category_id

    def test_save_mcc_with_existing_code_raises_error(self, setup):
        # Arrange
        code = "5444"
        category_id = 123
        self.sut.execute(SaveMccCommand(code=code, category_id=category_id))

        # Act & Assert
        with pytest.raises(Exception, match=f"MCC with code {code} already exists."):
            self.sut.execute(SaveMccCommand(code=code, category_id=category_id))

