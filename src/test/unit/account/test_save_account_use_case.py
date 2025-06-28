import pytest

from src.main.account.application.use_cases.exceptions.account_conflict_exception import AccountConflictException
from src.main.account.application.ports.driver.save_account_command import SaveAccountCommand
from src.main.account.application.use_cases.save_account_use_case import SaveAccountUseCase
from src.main.account.infra.adapters.driven.persistence.in_memory_account_repository import InMemoryAccountRepository


class TestSaveAccountUseCase:
    account_repository: InMemoryAccountRepository
    sut: SaveAccountUseCase


    @pytest.fixture
    def setup(self):
        self.account_repository = InMemoryAccountRepository()
        self.sut = SaveAccountUseCase(self.account_repository)

    def test_save_account_success(self, setup):
        # Arrange
        command = SaveAccountCommand(account_number="123456787458789")

        # Act
        output = self.sut.execute(command)

        # Assert
        assert output.account_id is not None
        assert output.account_number == command.account_number

    def test_save_account_with_existing_account_number_raises_error(self, setup):
        # Arrange
        account_number = "212341234123432"
        command = SaveAccountCommand(account_number)
        self.sut.execute(command)

        # Act & Assert
        with pytest.raises(AccountConflictException,match=f"Account with number {account_number} already exists." ):
            self.sut.execute(SaveAccountCommand(account_number))