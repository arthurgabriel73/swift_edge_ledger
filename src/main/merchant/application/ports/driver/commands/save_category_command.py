class SaveCategoryCommand:
    def __init__(self, code: str, description: str):
        self.validate_code(code)
        self.validate_description(description)
        self.code = code
        self.description = description

    @staticmethod
    def validate_code(code: str):
        if not code or not isinstance(code, str):
            raise ValueError("Invalid category code")
        if len(code) < 3 or len(code) > 100:
            raise ValueError("Category code must be between 3 and 100 characters long")

    @staticmethod
    def validate_description(description: str):
        if not description or not isinstance(description, str):
            raise ValueError("Invalid category description")
        if len(description) < 3 or len(description) > 140:
            raise ValueError("Category description must be between 3 and 140 characters long")