import uuid

import pytest

from main.merchant.domain.mcc import Mcc
from main.merchant.domain.mcc_id import MccId
from src.main.merchant.infra.adapters.driven.persistence.in_memory_mcc_repository import InMemoryMccRepository
from src.main.merchant.application.ports.driven.mcc_repository import MccRepository
from src.main.merchant.application.ports.driver.commands.save_merchant_command import SaveMerchantCommand
from src.main.merchant.application.ports.driven.merchant_repository import MerchantRepository
from src.main.merchant.application.use_cases.save_merchant_use_case import SaveMerchantUseCase
from src.main.merchant.infra.adapters.driven.persistence.in_memory_merchant_repository import InMemoryMerchantRepository


class TestSaveMerchantUseCase:
    merchant_repository: MerchantRepository
    mcc_repository: MccRepository
    sut: SaveMerchantUseCase

    @pytest.fixture
    def setup(self):
        self.merchant_repository = InMemoryMerchantRepository()
        self.mcc_repository = InMemoryMccRepository()
        self.sut = SaveMerchantUseCase(self.merchant_repository, self.mcc_repository)

    def test_save_merchant_success(self, setup):
        # Arrange
        mcc = Mcc.create(mcc_id=MccId(uuid.uuid4()), code="1234", category_id=123)
        self.mcc_repository.save(mcc)
        command = SaveMerchantCommand(merchant_name="Test Merchant", mcc_id=mcc.id.value())

        # Act
        output = self.sut.execute(command)

        # Assert
        assert output.merchant_id is not None
        assert output.merchant_name == command.merchant_name


    def test_save_merchant_with_existing_merchant_name_raises_error(self, setup):
        # Arrange
        merchant_name = "Existing Merchant"
        mcc = Mcc.create(mcc_id=MccId(uuid.uuid4()), code="1234", category_id=123)
        self.mcc_repository.save(mcc)
        command = SaveMerchantCommand(merchant_name, mcc_id=mcc.id.value())
        self.sut.execute(command)

        # Act & Assert
        with pytest.raises(Exception, match=f"Merchant with name {merchant_name} already exists."):
            self.sut.execute(SaveMerchantCommand(merchant_name, mcc_id=uuid.uuid4()))