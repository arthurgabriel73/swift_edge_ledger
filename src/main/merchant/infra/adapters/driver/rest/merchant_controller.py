from fastapi import APIRouter

from src.main.merchant.application.ports.driver.commands.save_merchant_command_output import SaveMerchantCommandOutput
from src.main.merchant.application.ports.driver.commands.save_merchant_command import SaveMerchantCommand
from src.main.merchant.application.ports.driver.save_merchant_driver_port import SaveMerchantDriverPort
from src.main.merchant.infra.adapters.driver.rest.request.save_merchant_request import SaveMerchantRequest
from src.main.merchant.infra.config.ioc import save_merchant_driver_factory
from src.main.shared.persistence_decorators import transactional

MERCHANTS_URL = "/merchants"

merchants_router = APIRouter(
    prefix=MERCHANTS_URL,
    tags=["Merchants"]
)

@merchants_router.post("/", status_code=201)
@transactional
def save_merchant(request: SaveMerchantRequest):
    driver: SaveMerchantDriverPort = save_merchant_driver_factory()
    command = SaveMerchantCommand(
        merchant_name=request.merchant_name,
        mcc_id=request.mcc_id
    )
    return driver.execute(command)