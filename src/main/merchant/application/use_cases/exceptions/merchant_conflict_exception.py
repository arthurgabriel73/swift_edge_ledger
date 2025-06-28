from main.merchant.application.use_cases.exceptions.application_exception import ApplicationException


class MerchantConflictException(ApplicationException):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
