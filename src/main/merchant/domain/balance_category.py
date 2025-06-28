class BalanceCategory:
    __allow_instantiation = False

    def __init__(self, category_id: int, name: str, description: str):
        if not self.__allow_instantiation:
            raise RuntimeError('Use the create method to instantiate a BalanceCategory')

        self.id = category_id
        self.name = name
        self.description = description

    @classmethod
    def create(cls, category_id: int, name: str, description: str) -> 'BalanceCategory':
        cls.__allow_instantiation = True
        return cls(category_id, name, description)

    @classmethod
    def from_value(cls, *, category_id: int, name: str, description: str) -> 'BalanceCategory':
        cls.__allow_instantiation = True
        return cls(category_id, name, description)