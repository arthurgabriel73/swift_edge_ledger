from src.main.shared.application.exceptions.application_exception import ApplicationException


class AccountBalanceConflictException(ApplicationException):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message