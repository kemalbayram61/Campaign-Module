from Objects.Feature import Feature
class ProductFilterCriteria:
    nameList: list[str]
    featureList: list[Feature]

    def __init__(self, nameList: list[str] = None,
                       featureList: list[Feature] = None):
        self.nameList = nameList
        self.featureList = featureList

    def listToStr(self, listObject):
        response = ""
        for element in listObject:
            response = response + str(element) + ';'
        return response

    def __str__(self):
        if(self.nameList == None):
            return self.listToStr(self.featureList)
        else:
            return self.listToStr(self.nameList)