from Object.Basket import Basket
from Object.Campaign import Campaign


class Optimizer:
    basket:Basket
    campaign_list: list[Campaign]

    def __init__(self, basket: Basket = None,
                 campaign_list: list[Campaign] = None):
        self.basket = basket
        self.campaign_list = campaign_list

    def optimize_basket(self) -> (Basket, list[Campaign]):
        return (self.basket, self.campaign_list)