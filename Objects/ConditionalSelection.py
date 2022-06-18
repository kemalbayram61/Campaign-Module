from Abstracts.EProductFilter import ProductFilter
from Objects.ProductFilterCriteria import ProductFilterCriteria
class ConditionalSelection:
    __id:str
    __requiredType: ProductFilter
    __requiredCriteria: ProductFilterCriteria
    __requiredCount: int
    __redundantType: ProductFilter
    __redundantCriteria: ProductFilterCriteria
    __redundantCount: int

    def getID(self) ->str:
        return self.__id

    def getRequiredType(self) ->ProductFilter:
        return self.__requiredType

    def getRequiredCriteria(self) ->ProductFilterCriteria:
        return self.__requiredCriteria

    def getRequiredCount(self) ->int:
        return self.__requiredCount

    def getRedundantType(self) -> ProductFilter:
        return self.__redundantType

    def getRedundantCriteria(self) -> ProductFilterCriteria:
        return self.__redundantCriteria

    def getRedundantCount(self) -> int:
        return self.__redundantCount

    def setID(self, id:str) ->None:
        self.__id = id

    def setRequiredType(self, requiredType: ProductFilter) ->None:
        self.__requiredType = requiredType

    def setRequiredCriteria(self, requiredCriteria: ProductFilterCriteria) ->None:
        self.__requiredCriteria = requiredCriteria

    def setRequiredCount(self, count: int) ->None:
        self.__requiredCount = count

    def setRedundantType(self, redundantType: ProductFilter) -> None:
        self.__redundantType = redundantType

    def setRedundantCriteria(self, redundandCriteria: ProductFilterCriteria) -> None:
        self.__redundantCriteria = redundandCriteria

    def setRedundantCount(self, count: int) -> None:
        self.__redundantCount = count