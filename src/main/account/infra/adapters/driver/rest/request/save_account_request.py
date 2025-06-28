from pydantic import BaseModel


class SaveAccountRequest(BaseModel):
    account_number: str

