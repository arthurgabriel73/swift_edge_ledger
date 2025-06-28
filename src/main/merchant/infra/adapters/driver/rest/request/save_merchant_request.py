from uuid import UUID

from pydantic import BaseModel


class SaveMerchantRequest(BaseModel):
    merchant_name: str
    mcc_id: UUID
