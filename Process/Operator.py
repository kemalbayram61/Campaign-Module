from Object.Basket import Basket
from Object.Campaign import Campaign


class Operator:
    campaign: Campaign
    basket: Basket

    def __init__(self, basket: Basket = None,
                 campaign: Campaign = None):
        self.basket = basket
        self.campaign = campaign

    def apply_campaign(self) -> Basket:
        if self.basket is not None and self.campaign is not None:
            return self.basket
        else:
            return self.basket
