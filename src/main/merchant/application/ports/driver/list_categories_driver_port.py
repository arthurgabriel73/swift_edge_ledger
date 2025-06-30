from abc import abstractmethod, ABC


class ListCategoriesDriverPort(ABC):
    @abstractmethod
    def execute(self) -> list:
        pass