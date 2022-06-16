from Objects.Feature import Feature
class ProductFilterCriteria:
    nameList: list[str]
    featureList: list[Feature]

    def __init__(self, nameList: list[str] = None,
                       featureList: list[Feature] = None):
        self.nameList = nameList
        self.featureList = featureList