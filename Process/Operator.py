from Abstract.ActionType import ActionType
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
    def evaluate_basket_amount(basket: Basket) -> float:
        amount: float = 0.0
        for product in basket.product_list:
            amount = amount + product.amount
        return amount

    def set_criteria_product_list_for_campaign(self) -> None:
        product_list: list[Product] = self.basket.product_list
        response: list[Product] = []
        for product in product_list:
            if self.campaign.id in product.criteria_campaign_list and product.is_used is False:
                response.append(product)
        self.criteria_product_list = response

    def set_action_product_list_for_campaign(self) -> None:
        product_list: list[Product] = self.basket.product_list
        response: list[Product] = []
        for product in product_list:
            if self.campaign.id in product.action_campaign_list and product.is_used is False:
                response.append(product)
        self.action_product_list = response

    def sort_criteria_product_list(self) -> None:
        #bubble sort was used as a start
        for i in range(len(self.criteria_product_list)):
            for j in range(0, len(self.criteria_product_list) - 1):
                if self.criteria_product_list[j].qty * self.criteria_product_list[j].unit_price > self.criteria_product_list[j + 1].qty * self.criteria_product_list[j + 1].unit_price:
                    temp = self.criteria_product_list[j]
                    self.criteria_product_list[j] = self.criteria_product_list[j + 1]
                    self.criteria_product_list[j + 1] = temp

    def sort_action_product_list(self) -> None:
        #bubble sort was used as a start
        for i in range(len(self.action_product_list)):
            for j in range(0, len(self.action_product_list) - 1):
                if self.action_product_list[j].qty * self.action_product_list[j].unit_price > self.action_product_list[j + 1].qty * self.action_product_list[j + 1].unit_price:
                    temp = self.action_product_list[j]
                    self.action_product_list[j] = self.action_product_list[j + 1]
                    self.action_product_list[j + 1] = temp

    def get_criteria_product_list_amount(self) -> float:
        amount: float = 0.0
        for product in self.criteria_product_list:
            amount = amount + product.unit_price * product.qty
        return amount

    def get_criteria_product_list_count(self) -> int:
        count: int = 0
        for product in self.criteria_product_list:
            count = count + product.qty
        return count

    def update_basket_products(self) -> None:
        for action_product in self.action_product_list:
            for basket_product in self.basket.product_list:
                if action_product.id == basket_product.id:
                    basket_product.amount = action_product.amount
                    basket_product.is_used = action_product.is_used


    def apply_campaign(self) -> Optional[Basket]:
        current_date: str = Date.get_current_date()
        if self.basket is not None and self.campaign is not None and Date.compare_date(self.campaign.start_date, current_date) <= 0 and Date.compare_date(self.campaign.end_date, current_date) >= 0 and self.campaign.is_active:
            self.set_criteria_product_list_for_campaign()
            self.set_action_product_list_for_campaign()
            self.sort_criteria_product_list()
            self.sort_action_product_list()
            rate: float = 0.0
            amount: float = 0.0

            #controls
            if self.campaign.min_amount is not None and self.campaign.min_amount > self.get_criteria_product_list_amount():
                #todo throw error with appropriate error code
                return None
            if self.campaign.min_qty is not None and self.campaign.min_qty > self.get_criteria_product_list_count():
                #todo throw error with appropriate error code
                return None

            if self.campaign.action_amount is not None:
                if self.campaign.action_type == ActionType.AMOUNT:
                    amount = self.campaign.action_amount
                elif self.campaign.action_type == ActionType.PERCENT:
                    rate = self.campaign.action_amount

            if amount != 0.0:
                for action_product in self.action_product_list:
                    action_product.amount = 0 if action_product.amount < 0 else action_product.amount
                    action_product.is_used = True
            elif rate != 0.0:
                for action_product in self.action_product_list:
                    action_product.amount = 0 if action_product.amount < 0 else action_product.amount
                    action_product.is_used = True
            self.update_basket_products()
            return self.basket
        else:
            return self.basket
