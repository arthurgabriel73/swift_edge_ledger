from src.main.merchant.application.ports.driven.category_repository import CategoryRepository
from src.main.merchant.application.ports.driver.commands.save_category_command_output import SaveCategoryCommandOutput
from src.main.merchant.application.ports.driver.save_category_driver_port import SaveCategoryDriverPort
from src.main.merchant.application.use_cases.exceptions.category_conflict_exception import CategoryConflictException
from src.main.merchant.domain.category import Category


class SaveCategoryUseCase(SaveCategoryDriverPort):
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def execute(self, command):
        self.require_category_code_does_not_exist(command.code)
        created_category = self.category_repository.save(Category.create(command.code, command.description))
        return SaveCategoryCommandOutput(code=created_category.code, description=created_category.description)

    def require_category_code_does_not_exist(self, code):
        existing_category = self.category_repository.find_by_code(code)
        if existing_category:
            raise CategoryConflictException(f"Category with code {code} already exists.")