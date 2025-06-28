import uuid

import pytest

from src.main.merchant.application.ports.driver.commands.save_merchant_command import SaveMerchantCommand
from src.main.merchant.application.ports.driven.merchant_repository import MerchantRepository
from src.main.merchant.application.use_cases.save_merchant_use_case import SaveMerchantUseCase
from src.main.merchant.infra.adapters.driven.persistence.in_memory_merchant_repository import InMemoryMerchantRepository


class TestSaveMerchantUseCase:
    merchant_repository: MerchantRepository
    sut: SaveMerchantUseCase

    @pytest.fixture
    def setup(self):
        self.merchant_repository = InMemoryMerchantRepository()
        self.sut = SaveMerchantUseCase(self.merchant_repository)

    def test_save_merchant_success(self, setup):
        # Arrange
        command = SaveMerchantCommand(merchant_name="Test Merchant", mcc_id=uuid.uuid4())

        # Act
        output = self.sut.execute(command)

        # Assert
        assert output.merchant_id is not None
        assert output.merchant_name == command.merchant_name


    def test_save_merchant_with_existing_merchant_name_raises_error(self, setup):
        # Arrange
        merchant_name = "Existing Merchant"
        command = SaveMerchantCommand(merchant_name, mcc_id=uuid.uuid4())
        self.sut.execute(command)

        # Act & Assert
        with pytest.raises(Exception, match=f"Merchant with name {merchant_name} already exists."):
            self.sut.execute(SaveMerchantCommand(merchant_name, mcc_id=uuid.uuid4()))