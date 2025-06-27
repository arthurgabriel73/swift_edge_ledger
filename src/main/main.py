import uvicorn

from fastapi import FastAPI

from src.main.shared.environment_settings import get_environment_variables
from src.main.account.infra.adapters.driver.rest.account_controller import accounts_router

description = "Swift Edge Ledger is a decentralized ledger system designed to provide secure, transparent, and efficient transaction processing across multiple nodes. This API allows users to interact with the ledger, manage accounts, and perform transactions."
app = FastAPI(
    title='Swift Edge Ledger - API',
    description=description
)

@app.get('/')
def root():
    return {'message': 'Welcome to the Swift Edge Ledger API!'}

app.include_router(accounts_router)

if __name__ == '__main__':
    env = get_environment_variables()
    uvicorn.run("main:app", host=env.APP_HOST, port=env.APP_PORT, log_level='info', reload=True)