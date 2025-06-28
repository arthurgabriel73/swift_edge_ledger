from starlette.responses import JSONResponse

from src.main.account.application.use_cases.exceptions.account_conflict_exception import AccountConflictException
from src.main.main import app


@app.exception_handler(ValueError)
async def value_error_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )

@app.exception_handler(AccountConflictException)
async def account_conflict_exception_handler(request, exc: AccountConflictException):
    return JSONResponse(
        status_code=409,
        content={"detail": exc.message}
    )