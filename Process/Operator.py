from typing import Optional
from Object.Basket import Basket
from Object.Campaign import Campaign


class Operator:
    campaign: Campaign
    basket: Basket

    def __init__(self, basket: Basket = None,
                 campaign: Campaign = None):
        self.basket = basket
        self.campaign = campaign

    @staticmethod
    def evaluate_basket_ceiling(basket: Basket) -> float:
        ceiling: float = 0.0
        for product in basket.product_list:
            ceiling = ceiling + product.ceiling
        return ceiling

    def apply_campaign(self) -> Optional[Basket]:
        if self.basket is not None and self.campaign is not None:
            return self.basket
        else:
            return None
