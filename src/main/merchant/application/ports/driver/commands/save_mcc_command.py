class SaveMccCommand:
    def __init__(self, code: str, category_id: int):
        self.validate_code(code)
        self.validate_category_id(category_id)
        self.code = code
        self.category_id = category_id

    @staticmethod
    def validate_code(code: str):
        if not code or not isinstance(code, str):
            raise ValueError("Invalid MCC code")
        if len(code) != 4:
            raise ValueError("MCC code must be 4 characters long")

    @staticmethod
    def validate_category_id(category_id: int):
        if not isinstance(category_id, int) or category_id <= 0:
            raise ValueError("Invalid category ID")