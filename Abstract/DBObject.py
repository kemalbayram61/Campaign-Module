from abc import ABC, abstractmethod

class DBObject(ABC):
    @abstractmethod
    def get(self) ->object:
        pass