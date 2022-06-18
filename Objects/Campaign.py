from Abstracts.EProductFilter import ProductFilter
from Objects.ProductFilterCriteria import ProductFilterCriteria
from Objects.ConditionalSelection import ConditionalSelection
class Campaign:
    __id: str
    __name: str
    __productFilter:ProductFilter
    __productFilterCriteria: ProductFilterCriteria
    __conditionalSelectionID: str
    __conditionalSelectionObject: ConditionalSelection

    def __init__(self, id: str = None,
                 name: str = None,
                 productFilter: ProductFilter = None,
                 productFilterCriteria: ProductFilterCriteria = None,
                 conditionalSelectionID: "str" = None,
                 conditionalSelectionObject: ConditionalSelection = None):
        self.__id = id
        self.__name = name
        self.__productFilter = productFilter
        self.__productFilterCriteria = productFilterCriteria
        self.__conditionalSelectionID = conditionalSelectionID
        self.__conditionalSelectionObject = conditionalSelectionObject

    def getID(self) ->str:
        return self.__id

    def getName(self) ->str:
        return self.__name

    def getProductFilter(self) ->ProductFilter:
        return self.__productFilter

    def getProductFilterCriteria(self) ->ProductFilterCriteria:
        return self.__productFilterCriteria

    def getConditionalSelectionID(self) ->str:
        return self.__conditionalSelectionID

    def getConditionalSelectionObject(self) ->ConditionalSelection:
        return self.__conditionalSelectionObject

    def setID(self, id: str) ->None:
        self.__id = id

    def setName(self, name: str) ->None:
        self.__name = name

    def setProductFilter(self, productFilter: ProductFilter) ->None:
        self.__productFilter = productFilter

    def setProductFilterCriteria(self, productFilterCriteria: ProductFilterCriteria):
        self.__productFilterCriteria = productFilterCriteria

    def setConditionalSelectionID(self, id: str) ->None:
        self.__conditionalSelectionID = id

    def setConditionalSelectionObject(self, conditionalSelectionObject: ConditionalSelection) ->None:
        self.__conditionalSelectionObject = conditionalSelectionObject

    def getDocument(self) ->dict:
        if(self.__id is not None):
            return {"_id": self.__id,
                    "name": self.__name,
                    "productFilter": self.__productFilter.name,
                    "productFilterCriteria": self.__productFilterCriteria.getDocument(),
                    "conditionalSelectionID": self.__conditionalSelectionID,
                    "conditionalSelectionObject": self.__conditionalSelectionObject.getDocument()}
        else:
            return {"name": self.__name,
                    "productFilter": self.__productFilter.name,
                    "productFilterCriteria": self.__productFilterCriteria.getDocument(),
                    "conditionalSelectionID": self.__conditionalSelectionID,
                    "conditionalSelectionObject": self.__conditionalSelectionObject.getDocument()}