from fastapi import APIRouter

from src.main.merchant.application.ports.driver.commands.save_category_command import SaveCategoryCommand
from src.main.merchant.application.ports.driver.save_category_driver_port import SaveCategoryDriverPort
from src.main.merchant.infra.adapters.driver.rest.request.save_category_request import SaveCategoryRequest
from src.main.merchant.infra.config.ioc import save_category_driver_factory
from src.main.shared.persistence_decorators import transactional

CATEGORY_URL = "/categories"

categories_router = APIRouter(
    prefix=CATEGORY_URL,
    tags=["Categories"]
)

@categories_router.post("/", status_code=201)
@transactional
def save_category(request: SaveCategoryRequest):
    driver: SaveCategoryDriverPort = save_category_driver_factory()
    command = SaveCategoryCommand(
        code=request.code,
        description=request.description
    )
    return driver.execute(command)