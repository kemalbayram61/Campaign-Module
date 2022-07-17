from typing import Optional
from Object.Basket import Basket
from Object.Campaign import Campaign
from Object.Product import Product
from Utility.Date import Date


class Operator:
    campaign: Campaign
    basket: Basket
    criteria_product_list: list[Product]
    action_product_list: list[Product]

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

    def set_product_list_of_campaign_by_criteria(self) -> None:
        product_list: list[Product] = self.basket.product_list
        response: list[Product] = []
        for product in product_list:
            if self.campaign.id in product.criteria_campaign_list:
                response.append(product)
        self.criteria_product_list = response

    def set_product_list_of_campaign_by_action(self) -> None:
        product_list: list[Product] = self.basket.product_list
        response: list[Product] = []
        for product in product_list:
            if self.campaign.id in product.action_campaign_list:
                response.append(product)
        self.action_product_list = response


    def apply_campaign(self) -> Optional[Basket]:
        current_date: str = Date.get_current_date()
        if self.basket is not None and self.campaign is not None and Date.compare_date(self.campaign.start_date, current_date) <= 0 and Date.compare_date(self.campaign.end_date, current_date) >= 0 and self.campaign.is_active:
            self.set_product_list_of_campaign_by_criteria()
            self.set_product_list_of_campaign_by_action()

            return self.basket
        else:
            return self.basket
