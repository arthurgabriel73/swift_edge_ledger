class SaveCategoryCommandOutput:
    def __init__(self, category_id: int, code: str, description: str):
        self.category_id = category_id
        self.code = code
        self.description = description
