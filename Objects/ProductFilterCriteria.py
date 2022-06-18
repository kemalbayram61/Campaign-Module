from Objects.Feature import Feature
class ProductFilterCriteria:
    nameList: list[str]
    featureList: list[Feature]

    def __init__(self, nameList: list[str] = None,
                       featureList: list[Feature] = None):
        self.nameList = nameList
        self.featureList = featureList

    def getDocument(self):
        if(self.nameList == None):
            return list(map(lambda feature: feature.getDocument(), self.featureList))
        else:
            return self.nameList