from Objects.Campaign import Campaign
from Objects.Basked import Basked

class Calculator:
    campaignList:list[Campaign]
    basked: Basked

    def __init__(self, campaignList: list[Campaign] = None, basked: Basked = None):
        self.campaignList = campaignList
        self.basked = basked

    def calculateBasked(self) ->Basked:
        return Basked()

    def fintOptimumCampaignSelection(self) ->list[Campaign]:
        return list[Campaign]