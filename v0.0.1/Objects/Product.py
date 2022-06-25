from Objects.Feature import Feature
class Product:
    __id :str
    __name: str
    __features: list[Feature]

    def __init__(self, id: str = "",
                       name: str = "",
                       features: list[Feature] = []):
        self.__id = id
        self.__name = name
        self.__features = features

    def setID(self, id: str) ->None:
        self.__id = id

    def setName(self, name: str) ->None:
        self.__name = name

    def setFeatures(self, features: list[Feature]) ->None:
        self.__features = features

    def setFeature(self, newValue: Feature, index: int) ->bool:
        if(len(self.__features)>index):
            self.__features[index] = newValue
            return True
        return False

    def deleteFeature(self, index: int) ->bool:
        if(len(self.__features)>index):
            self.__features.pop(index)
            return True
        return False

    def getID(self) ->str:
        return self.__id

    def getname(self) ->str:
        return self.__name

    def getFeatures(self) ->list[Feature]:
        return self.__features