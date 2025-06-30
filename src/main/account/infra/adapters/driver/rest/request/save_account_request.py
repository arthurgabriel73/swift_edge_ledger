from pydantic import BaseModel


class SaveAccountRequest(BaseModel):
    account_number: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "account_number": "65433467",
            }
        },

    }