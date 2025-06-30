from uuid import UUID

from pydantic import BaseModel


class SaveAccountBalanceRequest(BaseModel):
    account_id: UUID
    category_id: int
    amount_in_cents: int