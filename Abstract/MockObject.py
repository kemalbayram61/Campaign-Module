from abc import ABC,abstractmethod
class MockObject(ABC):
    @abstractmethod
    def get_mock_sql(self) -> str:
        pass