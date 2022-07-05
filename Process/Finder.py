from Object.Basket import Basket
from Object.Product import Product
from Object.Customer import Customer

class Finder:
    basked: Basket
    customer: Customer

    def __init__(self, customer: Customer = None,
                 basked: Basket = None):
        self.customer = customer
        self.basked = basked

    def discover_campaign_list(self) ->list[str]:
        if(self.customer is not None and self.basked is not None):
            productList: list[Product] = self.basked.productList
            criteriaCampaignList: list[str] = []
            actionCampaignList: list[str] = []
            response: list[str] = []
            for product in productList:
                criteriaCampaignList = criteriaCampaignList + product.criteriaCampaignList
                actionCampaignList = actionCampaignList + product.actionCampaignList

            for criteria in criteriaCampaignList:
                if(criteria in actionCampaignList and criteria in self.customer.campaignList):
                    response.append(criteria)

            return response
        return []