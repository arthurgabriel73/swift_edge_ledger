from starlette.responses import JSONResponse

from src.main.account.application.use_cases.exceptions.account_not_found_exception import AccountNotFoundException
from src.main.activity.application.use_cases.exceptions.account_balance_conflict_exception import \
    AccountBalanceConflictException
from src.main.merchant.application.use_cases.exceptions.category_not_found_exception import CategoryNotFoundException
from src.main.merchant.application.use_cases.exceptions.category_conflict_exception import CategoryConflictException
from src.main.merchant.application.use_cases.exceptions.mcc_conflict_exception import MccConflictException
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

@app.exception_handler(MccConflictException)
async def mcc_conflict_exception_handler(request, exc):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc.message)}
    )

@app.exception_handler(CategoryConflictException)
async def category_conflict_exception_handler(request, exc):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc.message)}
    )

@app.exception_handler(AccountBalanceConflictException)
async def account_balance_conflict_exception_handler(request, exc):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc.message)}
    )

@app.exception_handler(AccountNotFoundException)
async def account_not_found_exception_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc.message)}
    )

@app.exception_handler(CategoryNotFoundException)
async def category_not_found_exception_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc.message)}
    )