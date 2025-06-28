from src.main.account.application.use_cases.exceptions.application_exception import ApplicationException


class AccountConflictException(ApplicationException):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message