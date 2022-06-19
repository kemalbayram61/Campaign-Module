from Abstracts.EProductFilter import ProductFilter
from Objects.ProductFilterCriteria import ProductFilterCriteria
class ConditionalSelection:
    __id:str
    __campaignID: str
    __requiredType: ProductFilter
    __requiredCriteria: ProductFilterCriteria
    __requiredCount: int
    __redundantType: ProductFilter
    __redundantCriteria: ProductFilterCriteria
    __redundantCount: int

    def __init__(self, id: str = None,
                 campaignID: str = None,
                 requiredType: ProductFilter = None,
                 requiredCriteria: ProductFilterCriteria = None,
                 requiredCount:int = None,
                 redundantType: ProductFilter = None,
                 redundantCriteria: ProductFilterCriteria = None,
                 redundantCount: int = None):
        self.__id = id
        self.__campaignID = campaignID
        self.__requiredType = requiredType
        self.__requiredCriteria = requiredCriteria
        self.__requiredCount = requiredCount
        self.__redundantType = redundantType
        self.__redundantCriteria = redundantCriteria
        self.__redundantCount = redundantCount

    def getID(self) ->str:
        return self.__id

    def getCampaignID(self) ->str:
        return self.__campaignID

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

    def setCampaignID(self, id:str) ->None:
        self.__campaignID = id

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

    def getDocument(self) ->dict:
        if(self.__id is not None):
            return {"_id": self.__id,
                    "requiredType": self.__requiredType.name,
                    "requiredCriteria": self.__requiredCriteria.getDocument(),
                    "requiredCount": self.__requiredCount,
                    "redundantType": self.__redundantType.name,
                    "redundantCriteria": self.__redundantCriteria.getDocument(),
                    "redundantCount": self.__requiredCount}
        else:
            return {"requiredType": self.__requiredType.name,
                    "requiredCriteria": self.__requiredCriteria.getDocument(),
                    "requiredCount": self.__requiredCount,
                    "redundantType": self.__redundantType.name,
                    "redundantCriteria": self.__redundantCriteria.getDocument(),
                    "redundantCount": self.__requiredCount}