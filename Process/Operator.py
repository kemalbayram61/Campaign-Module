from Abstract.ActionType import ActionType
from Abstract.AllProductAction import AllProductAction
from typing import Optional
from Object.Basket import Basket
from Object.Campaign import Campaign
from Object.Product import Product
from Object.BasketLine import BasketLine
from Utility.Date import Date


class Operator:
    campaign: Campaign
    basket: Basket
    criteria_product_list: list[Product]
    criteria_basket_lines: list[BasketLine]
    action_product_list: list[Product]
    action_basket_lines: list[BasketLine]

    def __init__(self, basket: Basket = None,
                 campaign: Campaign = None):
        self.basket = basket
        self.campaign = campaign

    @staticmethod
    def evaluate_basket_amount(basket: Basket) -> float:
        amount: float = 0.0
        for basket_line in basket.basket_lines:
            amount = amount + basket_line.amount
        return amount

    def set_criteria_product_list_for_campaign(self) -> None:
        product_list: list[Product] = self.basket.product_list
        criteria_product_list: list[Product] = []
        criteria_basket_lines: list[BasketLine] = []
        for index, product in enumerate(product_list, start=0):
            if self.campaign.id in product.criteria_campaign_list and self.basket.basket_lines[index].is_used is False:
                criteria_product_list.append(product)
                criteria_basket_lines.append(self.basket.basket_lines[index])
        self.criteria_product_list = criteria_product_list
        self.criteria_basket_lines = criteria_basket_lines

    def set_action_product_list_for_campaign(self) -> None:
        product_list: list[Product] = self.basket.product_list
        action_product_list: list[Product] = []
        action_basket_lines: list[BasketLine] = []
        for index, product in enumerate(product_list, start=0):
            if self.campaign.id in product.action_campaign_list and self.basket.basket_lines[index].is_used is False:
                action_product_list.append(product)
                action_basket_lines.append(self.basket.basket_lines[index])
        self.action_product_list = action_product_list
        self.action_basket_lines = action_basket_lines

    def sort_criteria_product_list(self) -> None:
        #bubble sort was used as a start
        for i in range(len(self.criteria_basket_lines)):
            for j in range(0, len(self.criteria_basket_lines) - 1):
                if self.criteria_basket_lines[j].amount > self.criteria_basket_lines[j + 1].amount:
                    temp_bl = self.criteria_basket_lines[j]
                    temp_pl = self.criteria_product_list[j]
                    self.criteria_basket_lines[j] = self.criteria_basket_lines[j + 1]
                    self.criteria_product_list[j] = self.criteria_product_list[j + 1]
                    self.criteria_basket_lines[j + 1] = temp_bl
                    self.criteria_product_list[j + 1] = temp_pl

    def sort_action_product_list(self) -> None:
        #bubble sort was used as a start
        for i in range(len(self.action_basket_lines)):
            for j in range(0, len(self.action_basket_lines) - 1):
                if self.action_basket_lines[j].amount > self.action_basket_lines[j + 1].amount:
                    temp_bl = self.action_basket_lines[j]
                    temp_pl = self.action_product_list[j]
                    self.action_basket_lines[j] = self.action_basket_lines[j + 1]
                    self.action_product_list[j] = self.action_product_list[j + 1]
                    self.action_basket_lines[j + 1] = temp_bl
                    self.action_product_list[j + 1] = temp_pl

    def get_criteria_product_list_amount(self) -> float:
        amount: float = 0.0
        for basket_line in self.action_basket_lines:
            amount = amount + basket_line.amount
        return amount

    def get_criteria_product_count(self) -> int:
        count: int = 0
        for basket_line in self.criteria_basket_lines:
            count = count + basket_line.qty
        return count

    def get_action_product_count(self) -> int:
        count: int = 0
        for basket_line in self.criteria_basket_lines:
            count = count + basket_line.qty
        return count

    def update_basket_with_action_products(self) -> None:
        for index, action_product in enumerate(self.action_product_list, start=0):
            for basket_product in self.basket.product_list:
                if action_product.id == basket_product.id:
                    basket_product.amount = self.action_basket_lines[index].amount
                    basket_product.is_used = self.action_basket_lines[index].amount

    def get_basket_product_count(self) -> int:
        count: int = 0
        for basket_line in self.basket.basket_lines:
            count = count + basket_line.qty
        return count

    def apply_percentage_discount_to_basket(self, rate: float):
        for basket_line in self.basket.basket_lines:
            discount = basket_line.amount - basket_line.amount * rate
            basket_line.line_amount = basket_line.amount if discount > basket_line.amount else discount
            basket_line.discount_amount = basket_line.amount - basket_line.line_amount
            basket_line.is_used = True
            basket_line.discount_lines.append({'campaign_id':self.campaign.id, 'discount_amount':basket_line.discount_amount})

    def apply_amount_discount_to_basket(self, amount: float):
        discount_per_product: float = amount / self.get_basket_product_count()
        for basket_line in self.basket.basket_lines:
            discount = basket_line.amount - basket_line.qty * discount_per_product
            basket_line.line_amount = basket_line.amount if discount > basket_line.amount else discount
            basket_line.discount_amount = basket_line.amount - basket_line.line_amount
            basket_line.is_used = True
            basket_line.discount_lines.append({'campaign_id': self.campaign.id, 'discount_amount': basket_line.discount_amount})

    def apply_percentage_discount_to_action_product(self, rate: float):
        for basket_line in self.action_basket_lines:
            discount = basket_line.amount - basket_line.amount * rate
            basket_line.line_amount = basket_line.amount if discount > basket_line.amount else discount
            basket_line.discount_amount = basket_line.amount - basket_line.line_amount
            basket_line.is_used = True
            basket_line.discount_lines.append({'campaign_id': self.campaign.id, 'discount_amount': basket_line.discount_amount})

    def apply_amount_discount_to_action_product(self, amount: float):
        discount_per_product: float = amount / self.get_action_product_count()
        for basket_line in self.action_basket_lines:
            discount = basket_line.amount - basket_line.qty * discount_per_product
            basket_line.line_amount = basket_line.amount if discount > basket_line.amount else discount
            basket_line.discount_amount = basket_line.amount - basket_line.line_amount
            basket_line.is_used = True
            basket_line.discount_lines.append({'campaign_id': self.campaign.id, 'discount_amount': basket_line.discount_amount})


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
                return self.basket
            if self.campaign.min_qty is not None and self.campaign.min_qty > self.get_criteria_product_count():
                return self.basket

            if self.campaign.action_amount is not None:
                if self.campaign.action_type == ActionType.AMOUNT:
                    amount = self.campaign.action_amount
                elif self.campaign.action_type == ActionType.PERCENT:
                    rate = self.campaign.action_amount

            if amount != 0.0:
                if self.campaign.all_product_action == AllProductAction.YES:
                    self.apply_amount_discount_to_basket(amount)
                else:
                    self.apply_amount_discount_to_action_product(amount)

            elif rate != 0.0:
                if self.campaign.all_product_action == AllProductAction.YES:
                    self.apply_percentage_discount_to_basket(rate)
                else:
                    self.apply_percentage_discount_to_action_product(rate)
            return self.basket
        else:
            return self.basket
