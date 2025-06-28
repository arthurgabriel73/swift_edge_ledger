from pydantic import BaseModel


class SaveCategoryRequest(BaseModel):
    code: str
    description: str
