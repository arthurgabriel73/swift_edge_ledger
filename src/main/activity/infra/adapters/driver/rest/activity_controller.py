from fastapi import APIRouter

from src.main.activity.infra.config.ioc import process_activity_driver_factory
from src.main.activity.application.ports.driver.process_activity_driver_port import ProcessActivityDriverPort
from src.main.shared.persistence_decorators import transactional
from src.main.activity.application.ports.driver.commands.process_activity_command import ProcessActivityCommand
from src.main.activity.infra.adapters.driver.rest.request.process_activity_request import ProcessActivityRequest

ACTIVITIES_URL = "/activities"

activities_router = APIRouter(
    prefix=ACTIVITIES_URL,
    tags=["Activities"]
)

@activities_router.post("/", status_code=201)
@transactional
def process_activity(request: ProcessActivityRequest):
    driver: ProcessActivityDriverPort = process_activity_driver_factory()
    command = ProcessActivityCommand(
        account=request.account,
        amount_in_cents=request.amount_in_cents,
        mcc=request.mcc,
        merchant=request.merchant,
        merchant_priority=request.merchant_priority,
        fallback=request.fallback
    )
    return driver.execute(command)
