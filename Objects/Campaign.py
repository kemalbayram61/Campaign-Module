from Abstracts.EProductFilter import ProductFilter
from Abstracts.EImplementationType import ImplementationType
from Abstracts.EImplementationTypeCriteria import ImplementationTypeCriteria
from Abstracts.EComparison import Comparison
from Objects.ProductFilterCriteria import ProductFilterCriteria
class Campaign:
    __id: str
    __name: str
    __companyID: str
    __productFilter:ProductFilter
    __productFilterCriteria: ProductFilterCriteria
    __implementationType: ImplementationType
    __implementationTypeCriteria: ImplementationTypeCriteria
    __implementationTypeAmount: float
    __requiredType: ProductFilter
    __requiredCriteria: ProductFilterCriteria
    __requiredCount: int
    __requiredCondition: Comparison
    __requiredConditionAmount: float
    __redundantType: ProductFilter
    __redundantCriteria: ProductFilterCriteria
    __redundantCount: int
    __redundantCondition: Comparison
    __redundantConditionAmount: float

    def __init__(self, id: str = None,
                 name: str = None,
                 companyID: str = None,
                 productFilter: ProductFilter = None,
                 productFilterCriteria: ProductFilterCriteria = None,
                 implementationType: ImplementationType = None,
                 implementationTypeCriteria: ImplementationTypeCriteria = None,
                 implementationTypeAmount: float = None,
                 requiredType: ProductFilter = None,
                 requiredCriteria: ProductFilterCriteria = None,
                 requiredCount: int = None,
                 requiredCondition: Comparison = None,
                 requiredConditionAmount: float = None,
                 redundantType: ProductFilter = None,
                 redundantCriteria: ProductFilterCriteria = None,
                 redundantCount: int = None,
                 redundantCondition: Comparison = None,
                 redundantConditionAmount: float = None):
        self.__id = id
        self.__name = name
        self.__companyID = companyID
        self.__productFilter = productFilter
        self.__productFilterCriteria = productFilterCriteria
        self.__implementationType = implementationType
        self.__implementationTypeCriteria = implementationTypeCriteria
        self.__implementationTypeAmount = implementationTypeAmount
        self.__requiredType = requiredType
        self.__requiredCriteria = requiredCriteria
        self.__requiredCount = requiredCount
        self.__redundantType = redundantType
        self.__redundantCriteria = redundantCriteria
        self.__redundantCount = redundantCount
        self.__requiredCondition = requiredCondition
        self.__requiredConditionAmount = requiredConditionAmount
        self.__redundantCondition = redundantCondition
        self.__redundantConditionAmount = redundantConditionAmount

    def getID(self) ->str:
        return self.__id

    def getImplementationType(self) ->ImplementationType:
        return self.__implementationType

    def getImplementationTypeCriteria(self) ->ImplementationTypeCriteria:
        return self.__implementationTypeCriteria

    def getImplementationTypeAmount(self) ->float:
        return self.__implementationTypeAmount

    def getRequiredCondition(self) ->Comparison:
        return  self.__requiredCondition

    def getRequiredConditionAmount(self) ->float:
        return self.__requiredConditionAmount

    def getRedundantCondition(self) -> Comparison:
        return self.__redundantCondition

    def getRedundantConditionAmount(self) -> float:
        return self.__redundantConditionAmount

    def getCompanyID(self) ->str:
        return self.__companyID

    def getName(self) ->str:
        return self.__name

    def getProductFilter(self) ->ProductFilter:
        return self.__productFilter

    def getProductFilterCriteria(self) ->ProductFilterCriteria:
        return self.__productFilterCriteria

    def setID(self, id: str) ->None:
        self.__id = id

    def setCompanyID(self, id: str) ->None:
        self.__companyID = id

    def setName(self, name: str) ->None:
        self.__name = name

    def setProductFilter(self, productFilter: ProductFilter) ->None:
        self.__productFilter = productFilter

    def setProductFilterCriteria(self, productFilterCriteria: ProductFilterCriteria):
        self.__productFilterCriteria = productFilterCriteria

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