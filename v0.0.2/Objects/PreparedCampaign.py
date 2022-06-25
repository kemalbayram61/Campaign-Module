from Abstracts.CriteriaTypes import CriteriaTypes
class PreparedCampaign:
    campaignName: str
    feature: CriteriaTypes
    featureValue = None
    isPotential: bool
    campaignID: str

    def __init__(self, campaignID:str =None, campaignName: str = None, feature: CriteriaTypes = None, featureValue = None, isPotential: bool = None):
        self.campaignID = campaignID
        self.campaignName = campaignName
        self.feature = feature
        self.featureValue = featureValue
        self.isPotential = isPotential

    def __str__(self):
        return str(self.campaignID) + "\t" + str(self.campaignName) +"\t\t" + str(self.feature) + "\t" + str(self.featureValue) + "\t" + str(self.isPotential)

