from fastapi import APIRouter

from src.main.activity.application.ports.driver.commands.save_account_balance_command import SaveAccountBalanceCommand
from src.main.activity.application.ports.driver.save_account_balance_driver_port import SaveAccountBalanceDriverPort
from src.main.activity.infra.adapters.driver.rest.request.save_account_balance_request import SaveAccountBalanceRequest
from src.main.activity.infra.config.ioc import save_account_balance_driver_factory

ACCOUNT_BALANCES_URL = "/account_balances"

account_balances_router = APIRouter(
    prefix=ACCOUNT_BALANCES_URL,
    tags=["Account Balances"]
)

@account_balances_router.post("/", status_code=201)
def save_account_balance(request: SaveAccountBalanceRequest):
    driver: SaveAccountBalanceDriverPort = save_account_balance_driver_factory()
    command = SaveAccountBalanceCommand(
        account_id=request.account_id,
        category_id=request.category_id,
        amount_in_cents=request.amount_in_cents,
    )
    return driver.execute(command)