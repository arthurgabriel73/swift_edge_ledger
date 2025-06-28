from starlette.responses import JSONResponse

from src.main.merchant.application.use_cases.exceptions.merchant_conflict_exception import MerchantConflictException
from src.main.account.application.use_cases.exceptions.account_conflict_exception import AccountConflictException
from src.main.main import app


@app.exception_handler(ValueError)
async def value_error_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )

@app.exception_handler(AccountConflictException)
async def account_conflict_exception_handler(request, exc):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc.message)}
    )

@app.exception_handler(MerchantConflictException)
async def merchant_conflict_exception_handler(request, exc):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc.message)}
    )