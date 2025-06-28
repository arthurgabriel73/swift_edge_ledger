from fastapi import APIRouter

from src.main.merchant.application.ports.driver.commands.save_mcc_command import SaveMccCommand
from src.main.merchant.application.ports.driver.commands.save_mcc_command_output import SaveMccCommandOutput
from src.main.merchant.application.ports.driver.save_mcc_driver_port import SaveMccDriverPort
from src.main.merchant.infra.adapters.driver.rest.request.save_mcc_request import SaveMccRequest
from src.main.merchant.infra.config.ioc import save_mcc_driver_factory
from src.main.shared.persistence_decorators import transactional

MCC_URL = "/mcc"

mcc_router = APIRouter(
    prefix=MCC_URL,
    tags=["MCC"]
)

@mcc_router.post("/", status_code=201)
@transactional
def save_mcc(request: SaveMccRequest) -> SaveMccCommandOutput:
    driver: SaveMccDriverPort = save_mcc_driver_factory()
    command = SaveMccCommand(
        code=request.code,
        category_id=request.category_id
    )
    return driver.execute(command)