import sys
from pathlib import Path

from src.main.shared.environment_settings import get_environment_variables

sys.path.append(str(Path(__file__).resolve().parent))


import asyncio

import uvicorn

from fastapi import FastAPI

description = "a"
app = FastAPI(
    title='Swift Edge Ledger - API',
    description=description
)

@app.get('/')
async def root():
    return {'message': 'Welcome to the Swift Edge Ledger API!'}

if __name__ == '__main__':
    env = get_environment_variables()
    uvicorn.run("main:app", host=env.APP_HOST, port=env.APP_PORT, log_level='info', reload=True)