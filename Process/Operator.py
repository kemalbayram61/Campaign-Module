from typing import Optional
from Object.Basket import Basket
from Object.Campaign import Campaign
from Utility.Date import Date


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
        current_date: str = Date.get_current_date()
        if self.basket is not None and self.campaign is not None and Date.compare_date(self.campaign.start_date, current_date) <= 0 and Date.compare_date(self.campaign.end_date, current_date) >= 0 and self.campaign.is_active:
            return self.basket
        else:
            return self.basket
