from pydantic import BaseModel


class ProcessActivityRequest(BaseModel):
    account: str
    amount_in_cents: int
    mcc: str
    merchant: str
    merchant_priority: bool = False
    fallback: bool = False