from abc import ABC, abstractmethod


class DBObject(ABC):
    @abstractmethod
    def get(self) -> object:
        pass

    @abstractmethod
    def load_data(self) -> None:
        pass

    @abstractmethod
    def get_all(self, org_id: str) -> list[object]:
        pass
