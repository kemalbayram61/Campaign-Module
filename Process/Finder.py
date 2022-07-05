from Object.Basket import Basket
from Object.Campaign import Campaign
from Object.Product import Product

class Finder:
    basked: Basket
    campaignList: list[Campaign]

    def discover_campaign_list(self) ->list[str]:
        productList: list[Product] = self.basked.productList
        criteriaCampaignList: list[str] = []
        actionCampaignList: list[str] = []
        response: list[str] = []
        for product in productList:
            criteriaCampaignList = criteriaCampaignList + product.criteriaCampaignList
            actionCampaignList = actionCampaignList + product.actionCampaignList

        for criteria in criteriaCampaignList:
            if(criteria in actionCampaignList):
                response.append(criteria)

        return response