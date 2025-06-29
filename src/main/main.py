import uvicorn

from fastapi import FastAPI

from src.main.activity.infra.adapters.driver.rest.account_balance_controller import account_balances_router
from src.main.activity.infra.adapters.driver.rest.activity_controller import activities_router
from src.main.merchant.infra.adapters.driver.rest.category_controller import categories_router
from src.main.merchant.infra.adapters.driver.rest.mcc_controller import mcc_router
from src.main.shared.environment_settings import get_environment_variables
from src.main.account.infra.adapters.driver.rest.account_controller import accounts_router
from src.main.merchant.infra.adapters.driver.rest.merchant_controller import merchants_router


description = "Swift Edge Ledger is a decentralized ledger system designed to provide secure, transparent, and efficient transaction processing across multiple nodes. This API allows users to interact with the ledger, manage accounts, and perform transactions."
app = FastAPI(
    title='Swift Edge Ledger - API',
    description=description
)

from src.main.shared.custom_exception_handler import * # important: to load custom exception handlers

@app.get('/')
def root():
    return {'message': 'Welcome to the Swift Edge Ledger API!'}

app.include_router(accounts_router)
app.include_router(merchants_router)
app.include_router(mcc_router)
app.include_router(categories_router)

app.include_router(activities_router)

app.include_router(account_balances_router)

if __name__ == '__main__':
    env = get_environment_variables()
    uvicorn.run("main:app", host=env.APP_HOST, port=env.APP_PORT, log_level='info', reload=True)