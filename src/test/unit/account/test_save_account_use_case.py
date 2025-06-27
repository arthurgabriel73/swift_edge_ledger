import pytest

from src.main.account.application.ports.driver.save_account_command import SaveAccountCommand
from src.main.account.application.use_cases.save_account_use_case import SaveAccountUseCase
from src.main.account.infra.adapters.driven.persistence.in_memory_account_repository import InMemoryAccountRepository


class TestSaveAccountUseCase:
    accountRepository: InMemoryAccountRepository
    sut: SaveAccountUseCase


    @pytest.fixture
    def setup(self):
        self.accountRepository = InMemoryAccountRepository()
        self.sut = SaveAccountUseCase(self.accountRepository)

    def test_save_account_success(self, setup):
        # Arrange
        command = SaveAccountCommand(account_number="123456789")

        # Act
        output = self.sut.execute(command)

        # Assert
        assert output.account_id is not None
        assert output.account_number == command.account_number

    def test_save_account_with_existing_account_number_raises_error(self, setup):
        # Arrange
        account_number = "123456789"
        command = SaveAccountCommand(account_number)
        self.sut.execute(command)

        # Act & Assert
        with pytest.raises(ValueError,match=f"Account with number {account_number} already exists." ):
            self.sut.execute(SaveAccountCommand(account_number))