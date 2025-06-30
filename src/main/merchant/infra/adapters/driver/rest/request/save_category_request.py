from pydantic import BaseModel


class SaveCategoryRequest(BaseModel):
    code: str
    description: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "code": "FOOD",
                "description": "FOOD Category",
            }
        },
    }
