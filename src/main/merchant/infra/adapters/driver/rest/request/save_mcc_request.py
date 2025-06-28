from pydantic import BaseModel


class SaveMccRequest(BaseModel):
    code: str
    category_id: int
