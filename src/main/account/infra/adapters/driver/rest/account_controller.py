from fastapi import APIRouter

from src.main.shared.persistence_decorators import transactional
from src.main.account.infra.adapters.driver.rest.request.save_account_request import SaveAccountRequest
from src.main.account.application.ports.driver.save_account_driver_port import SaveAccountDriverPort
from src.main.account.application.ports.driver.save_account_command import SaveAccountCommand
from src.main.account.infra.config.ioc import save_account_driver_factory

ACCOUNTS_URL = "/accounts"

accounts_router = APIRouter(
    prefix=ACCOUNTS_URL,
    tags=["Accounts"]
)

@accounts_router.post(ACCOUNTS_URL, status_code=201)
@transactional
def save_account(request: SaveAccountRequest):
    driver: SaveAccountDriverPort = save_account_driver_factory()
    command = SaveAccountCommand(request.account_number)
    return driver.execute(command)
