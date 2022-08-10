from Abstract.ActionType import ActionType
from Abstract.AllProductAction import AllProductAction
from Abstract.AllProductCriteria import AllProductCriteria
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
            amount = amount + basket_line.line_amount
        return amount

    def set_criteria_product_list_for_campaign(self) -> None:
        product_list: list[Product] = self.basket.product_list
        criteria_product_list: list[Product] = []
        criteria_basket_lines: list[BasketLine] = []
        for index, product in enumerate(product_list, start=0):
            if self.campaign.id in product.criteria_campaign_list or self.campaign.all_product_criteria == AllProductCriteria.YES:
                criteria_product_list.append(product)
                criteria_basket_lines.append(self.basket.basket_lines[index])
        self.criteria_product_list = criteria_product_list
        self.criteria_basket_lines = criteria_basket_lines

    def set_action_product_list_for_campaign(self) -> None:
        product_list: list[Product] = self.basket.product_list
        action_product_list: list[Product] = []
        action_basket_lines: list[BasketLine] = []
        for index, product in enumerate(product_list, start=0):
            if self.campaign.id in product.action_campaign_list or self.campaign.all_product_criteria == AllProductCriteria.YES:
                action_product_list.append(product)
                action_basket_lines.append(self.basket.basket_lines[index])
        self.action_product_list = action_product_list
        self.action_basket_lines = action_basket_lines

    def sort_criteria_product_list(self) -> None:
        #bubble sort was used as a start
        for i in range(len(self.criteria_basket_lines)):
            for j in range(0, len(self.criteria_basket_lines) - 1):
                if self.criteria_basket_lines[j].amount / self.criteria_basket_lines[j].qty > self.criteria_basket_lines[j + 1].amount / self.criteria_basket_lines[j + 1].qty:
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
                if self.action_basket_lines[j].amount / self.action_basket_lines[j + 1].qty > self.action_basket_lines[j + 1].amount / self.action_basket_lines[j].qty:
                    temp_bl = self.action_basket_lines[j]
                    temp_pl = self.action_product_list[j]
                    self.action_basket_lines[j] = self.action_basket_lines[j + 1]
                    self.action_product_list[j] = self.action_product_list[j + 1]
                    self.action_basket_lines[j + 1] = temp_bl
                    self.action_product_list[j + 1] = temp_pl

    def get_criteria_product_amount(self) -> float:
        amount: float = 0.0
        for basket_line in self.criteria_basket_lines:
            amount = amount + basket_line.amount
        return amount

    def get_criteria_product_count(self) -> int:
        count: int = 0
        for basket_line in self.criteria_basket_lines:
            count = count + basket_line.qty
        return count

    def get_action_product_count(self) -> int:
        count: int = 0
        for basket_line in self.action_basket_lines:
            count = count + basket_line.qty
        return count

    def get_basket_product_count(self) -> int:
        count: int = 0
        for basket_line in self.basket.basket_lines:
            count = count + basket_line.qty
        return count

    def get_real_max_discount(self) -> float:
        real_discount: float = self.campaign.max_discount
        if self.campaign.min_qty is not None:
            degree: int = int(self.get_criteria_product_count() / self.campaign.min_qty)
            real_discount = real_discount * degree
        elif self.campaign.min_amount is not None:
            degree: int = int(self.get_criteria_product_amount() / self.campaign.min_amount)
            real_discount = real_discount * degree
        return real_discount

    def get_real_action_qty(self) -> int:
        real_action_qty: int = self.campaign.action_qty
        if self.campaign.min_qty is not None:
            degree: int = int(self.get_criteria_product_count() / self.campaign.min_qty)
            real_action_qty = real_action_qty * degree
        elif self.campaign.min_amount is not None:
            degree: int = int(self.get_criteria_product_amount() / self.campaign.min_amount)
            real_action_qty = real_action_qty * degree
        return real_action_qty

    # her bir ürüne ayrı ayrı amount kadar indirim uygula max discountu geçmesin f1()
    def f1(self):
        implemented_total_discount: float = 0.0
        action_amount: float = self.campaign.action_amount
        max_discount: float = self.get_real_max_discount()
        for basket_line in self.basket.basket_lines:
            if implemented_total_discount < max_discount:
                if basket_line.is_used is False:
                    tmp_action_amount = action_amount
                    tmp_action_amount = tmp_action_amount * basket_line.qty
                    if basket_line.line_amount > tmp_action_amount:
                        basket_line.line_amount = basket_line.line_amount - tmp_action_amount
                        basket_line.discount_amount = tmp_action_amount
                        basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": tmp_action_amount})
                        basket_line.is_used = True
                        implemented_total_discount = implemented_total_discount + tmp_action_amount
                    else:
                        implemented_total_discount = implemented_total_discount + basket_line.line_amount
                        basket_line.discount_amount = basket_line.line_amount
                        basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": basket_line.line_amount})
                        basket_line.is_used = True
                        basket_line.line_amount = 0.0
                    if implemented_total_discount > max_discount:
                        distance = (implemented_total_discount - max_discount)
                        basket_line.line_amount = basket_line.line_amount + distance
                        basket_line.discount_amount = basket_line.discount_amount - distance
                        basket_line.discount_lines[len(basket_line.discount_lines)-1]["discount_amount"] = basket_line.discount_amount
                        basket_line.is_used = True
                        implemented_total_discount = max_discount
            else:
                break

    # action_qty kadar ürüne ayrı ayrı amount kadar indirim uygula f2()
    def f2(self):
        implemented_total_qty: int = 0
        action_amount: float = self.campaign.action_amount
        action_qty: int = self.get_real_action_qty()
        for basket_line in self.basket.basket_lines:
            if implemented_total_qty < action_qty:
                if basket_line.is_used is False:
                    implemented_total_qty = implemented_total_qty + basket_line.qty
                    tmp_action_amount = action_amount
                    if implemented_total_qty > action_qty:
                        tmp_action_amount = tmp_action_amount * (implemented_total_qty - action_qty)
                        implemented_total_qty = action_qty
                    else:
                        tmp_action_amount = tmp_action_amount * basket_line.qty

                    if basket_line.line_amount > tmp_action_amount:
                        basket_line.line_amount = basket_line.line_amount - tmp_action_amount
                        basket_line.discount_amount = tmp_action_amount
                        basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": tmp_action_amount})
                        basket_line.is_used = True
                    else:
                        basket_line.discount_amount = basket_line.line_amount
                        basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": basket_line.line_amount})
                        basket_line.is_used = True
                        basket_line.line_amount = 0.0
            else:
                break

    # her bir ürüne toplamda amount kadar indirim uygula f3()
    def f3(self):
        action_amount: float = self.campaign.action_amount
        unit_discount: float = action_amount / self.get_basket_product_count()
        for basket_line in self.basket.basket_lines:
            if basket_line.is_used is False:
                discount_amount = unit_discount * basket_line.qty
                if discount_amount < basket_line.line_amount:
                    basket_line.line_amount = basket_line.line_amount - discount_amount
                    basket_line.discount_amount = discount_amount
                    basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": discount_amount})
                    basket_line.is_used = True
                else:
                    basket_line.discount_amount = basket_line.line_amount
                    basket_line.line_amount = 0.0
                    basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": basket_line.discount_amount})
                    basket_line.is_used = True

    # kampanya ürünlerine ayrı ayrı amount kadar indirim uygula max discountu geçmesin f4()
    def f4(self):
        implemented_total_discount: float = 0.0
        action_amount: float = self.campaign.action_amount
        max_discount: float = self.get_real_max_discount()
        for index, basket_line in enumerate(self.basket.basket_lines, start=0):
            if implemented_total_discount < max_discount:
                if self.campaign.id in self.basket.product_list[index].action_campaign_list and basket_line.is_used is False:
                    tmp_action_amount = action_amount
                    tmp_action_amount = tmp_action_amount * basket_line.qty
                    if basket_line.line_amount > tmp_action_amount:
                        basket_line.line_amount = basket_line.line_amount - tmp_action_amount
                        basket_line.discount_amount = tmp_action_amount
                        basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": tmp_action_amount})
                        basket_line.is_used = True
                        implemented_total_discount = implemented_total_discount + tmp_action_amount
                    else:
                        implemented_total_discount = implemented_total_discount + basket_line.line_amount
                        basket_line.discount_amount = basket_line.line_amount
                        basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": basket_line.line_amount})
                        basket_line.is_used = True
                        basket_line.line_amount = 0.0
                    if implemented_total_discount > max_discount:
                        distance = (implemented_total_discount - max_discount)
                        basket_line.line_amount = basket_line.line_amount + distance
                        basket_line.discount_amount = basket_line.discount_amount - distance
                        basket_line.discount_lines[len(basket_line.discount_lines) - 1]["discount_amount"] = basket_line.discount_amount
                        basket_line.is_used = True
                        implemented_total_discount = max_discount
            else:
                break

    # kampanya ürünlerinden action_qty kadar ürüne ayrı ayrı amount kadar indirim uygula f5()
    def f5(self):
        implemented_total_qty: int = 0
        action_amount: float = self.campaign.action_amount
        action_qty: int = self.get_real_action_qty()
        for index, basket_line in enumerate(self.basket.basket_lines, start=0):
            if implemented_total_qty < action_qty:
                if self.campaign.id in self.basket.product_list[index].action_campaign_list and basket_line.is_used is False:
                    implemented_total_qty = implemented_total_qty + basket_line.qty
                    tmp_action_amount = action_amount
                    if implemented_total_qty > action_qty:
                        tmp_action_amount = tmp_action_amount * (implemented_total_qty - action_qty)
                        implemented_total_qty = action_qty
                    else:
                        tmp_action_amount = tmp_action_amount * basket_line.qty

                    if basket_line.line_amount > tmp_action_amount:
                        basket_line.line_amount = basket_line.line_amount - tmp_action_amount
                        basket_line.discount_amount = tmp_action_amount
                        basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": tmp_action_amount})
                        basket_line.is_used = True
                    else:
                        basket_line.discount_amount = basket_line.line_amount
                        basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": basket_line.line_amount})
                        basket_line.is_used = True
                        basket_line.line_amount = 0.0
            else:
                break

    # kampanya ürünlerine toplamda amount kadar indirim uygula f6()
    def f6(self):
        action_amount: float = self.campaign.action_amount
        unit_discount: float = action_amount / self.get_action_product_count()
        for index, basket_line in enumerate(self.basket.basket_lines, start=0):
            if self.campaign.id in self.basket.product_list[index].action_campaign_list and basket_line.is_used is False:
                discount_amount = unit_discount * basket_line.qty
                if discount_amount < basket_line.line_amount:
                    basket_line.line_amount = basket_line.line_amount - discount_amount
                    basket_line.discount_amount = discount_amount
                    basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": discount_amount})
                    basket_line.is_used = True
                else:
                    basket_line.discount_amount = basket_line.line_amount
                    basket_line.line_amount = 0.0
                    basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": basket_line.discount_amount})
                    basket_line.is_used = True

    # her bir üründen action_qty kadar ürüne ayrı ayrı rate kadar indirim uygula max discountu geçmesin f7()
    def f7(self):
        implemented_total_discount: float = 0.0
        implemented_total_qty: int = 0
        action_amount: float = self.campaign.action_amount
        max_discount: float = self.get_real_max_discount()
        action_qty: int = self.get_real_action_qty()
        for basket_line in self.basket.basket_lines:
            if implemented_total_discount < max_discount and implemented_total_qty < action_qty:
                if basket_line.is_used is False:
                    tmp_action_amount = action_amount
                    implemented_total_qty = implemented_total_qty + basket_line.qty
                    if implemented_total_qty > action_qty:
                        tmp_action_amount = (basket_line.qty - (implemented_total_qty - action_qty)) * tmp_action_amount / basket_line.qty
                        implemented_total_qty = action_qty

                    discount_amount = basket_line.line_amount * tmp_action_amount
                    basket_line.line_amount = basket_line.line_amount - discount_amount
                    basket_line.discount_amount = discount_amount
                    implemented_total_discount = implemented_total_discount + discount_amount

                    if implemented_total_discount > max_discount:
                        distance = (implemented_total_discount - max_discount)
                        basket_line.line_amount = basket_line.line_amount + distance
                        basket_line.discount_amount = basket_line.discount_amount - distance
                        implemented_total_discount = max_discount

                    basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": basket_line.discount_amount})
                    basket_line.is_used = True
            else:
                break

    # her bir ürüne ayrı ayrı rate kadar indirim uygula max discountu geçmesin f8()
    def f8(self):
        implemented_total_discount: float = 0.0
        action_amount: float = self.campaign.action_amount
        max_discount: float = self.get_real_max_discount()
        for basket_line in self.basket.basket_lines:
            if implemented_total_discount < max_discount:
                if basket_line.is_used is False:
                    discount_amount = basket_line.line_amount * action_amount
                    basket_line.line_amount = basket_line.line_amount - discount_amount
                    basket_line.discount_amount = discount_amount
                    basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": discount_amount})
                    basket_line.is_used = True
                    implemented_total_discount = implemented_total_discount + discount_amount

                    if implemented_total_discount > max_discount:
                        distance = (implemented_total_discount - max_discount)
                        basket_line.line_amount = basket_line.line_amount + distance
                        basket_line.discount_amount = basket_line.discount_amount - distance
                        basket_line.discount_lines[len(basket_line.discount_lines)-1]["discount_amount"] = basket_line.discount_amount
                        basket_line.is_used = True
                        implemented_total_discount = max_discount
            else:
                break

    # her bir üründen action_qty kadar ürüne ayrı ayrı rate kadar indirim uygula f9()
    def f9(self):
        implemented_total_qty: int = 0
        action_amount: float = self.campaign.action_amount
        action_qty: int = self.get_real_action_qty()
        for basket_line in self.basket.basket_lines:
            if implemented_total_qty < action_qty:
                if basket_line.is_used is False:
                    implemented_total_qty = implemented_total_qty + basket_line.qty
                    tmp_action_amount = action_amount
                    if implemented_total_qty > action_qty:
                        distance = implemented_total_qty - action_qty
                        tmp_action_amount = (basket_line.qty - distance) * tmp_action_amount / basket_line.qty
                        implemented_total_qty = action_qty

                    discount_amount = basket_line.line_amount * tmp_action_amount
                    basket_line.line_amount = basket_line.line_amount - discount_amount
                    basket_line.discount_amount = discount_amount
                    basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": discount_amount})
                    basket_line.is_used = True
            else:
                break

    # her bir ürüne ayrı ayrı rate kadar indirim uygula f10()
    def f10(self):
        action_amount: float = self.campaign.action_amount
        for basket_line in self.basket.basket_lines:
            if basket_line.is_used is False:
                discount_amount = basket_line.line_amount * action_amount
                basket_line.line_amount = basket_line.line_amount - discount_amount
                basket_line.discount_amount = discount_amount
                basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": discount_amount})
                basket_line.is_used = True

    # kampanya ürünlerinden action_qty kadar ürüne ayrı ayrı rate kadar indirim uygula max discountu geçmesin f11()
    def f11(self):
        implemented_total_discount: float = 0.0
        implemented_total_qty: int = 0
        action_amount: float = self.campaign.action_amount
        max_discount: float = self.get_real_max_discount()
        action_qty: int = self.get_real_action_qty()
        for index, basket_line in enumerate(self.basket.basket_lines, start=0):
            if implemented_total_discount < max_discount and implemented_total_qty < action_qty:
                if self.campaign.id in self.basket.product_list[index].action_campaign_list and basket_line.is_used is False:
                    tmp_action_amount = action_amount
                    implemented_total_qty = implemented_total_qty + basket_line.qty
                    if implemented_total_qty > action_qty:
                        tmp_action_amount = (basket_line.qty - (implemented_total_qty - action_qty)) * tmp_action_amount / basket_line.qty
                        implemented_total_qty = action_qty

                    discount_amount = basket_line.line_amount * tmp_action_amount
                    basket_line.line_amount = basket_line.line_amount - discount_amount
                    basket_line.discount_amount = discount_amount
                    implemented_total_discount = implemented_total_discount + discount_amount

                    if implemented_total_discount > max_discount:
                        distance = (implemented_total_discount - max_discount)
                        basket_line.line_amount = basket_line.line_amount + distance
                        basket_line.discount_amount = basket_line.discount_amount - distance
                        implemented_total_discount = max_discount

                    basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": basket_line.discount_amount})
                    basket_line.is_used = True
            else:
                break

    # kampanya ürünlerine ayrı ayrı rate kadar indirim uygula max discountu geçmesin f12()
    def f12(self):
        implemented_total_discount: float = 0.0
        action_amount: float = self.campaign.action_amount
        max_discount: float = self.get_real_max_discount()
        for index, basket_line in enumerate(self.basket.basket_lines, start=0):
            if implemented_total_discount < max_discount:
                if self.campaign.id in self.basket.product_list[index].action_campaign_list and basket_line.is_used is False:
                    discount_amount = basket_line.line_amount * action_amount
                    basket_line.line_amount = basket_line.line_amount - discount_amount
                    basket_line.discount_amount = discount_amount
                    basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": discount_amount})
                    basket_line.is_used = True
                    implemented_total_discount = implemented_total_discount + discount_amount

                    if implemented_total_discount > max_discount:
                        distance = (implemented_total_discount - max_discount)
                        basket_line.line_amount = basket_line.line_amount + distance
                        basket_line.discount_amount = basket_line.discount_amount - distance
                        basket_line.discount_lines[len(basket_line.discount_lines)-1]["discount_amount"] = basket_line.discount_amount
                        basket_line.is_used = True
                        implemented_total_discount = max_discount
            else:
                break

    # kampanya ürünlerinden action_qty kadar ürüne ayrı ayrı rate kadar indirim uygula f13()
    def f13(self):
        implemented_total_qty: int = 0
        action_amount: float = self.campaign.action_amount
        action_qty: int = self.get_real_action_qty()
        for index, basket_line in enumerate(self.basket.basket_lines, start=0):
            if implemented_total_qty < action_qty:
                if self.campaign.id in self.basket.product_list[index].action_campaign_list and basket_line.is_used is False:
                    implemented_total_qty = implemented_total_qty + basket_line.qty
                    tmp_action_amount = action_amount
                    if implemented_total_qty > action_qty:
                        distance = implemented_total_qty - action_qty
                        tmp_action_amount = (basket_line.qty - distance) * tmp_action_amount / basket_line.qty
                        implemented_total_qty = action_qty

                    discount_amount = basket_line.line_amount * tmp_action_amount
                    basket_line.line_amount = basket_line.line_amount - discount_amount
                    basket_line.discount_amount = discount_amount
                    basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": discount_amount})
                    basket_line.is_used = True
            else:
                break

    # kampanya ayrı ayrı rate kadar indirim uygula f14()
    def f14(self):
        action_amount: float = self.campaign.action_amount
        for index, basket_line in enumerate(self.basket.basket_lines, start=0):
            if self.campaign.id in self.basket.product_list[index].action_campaign_list and basket_line.is_used is False:
                discount_amount = basket_line.line_amount * action_amount
                basket_line.line_amount = basket_line.line_amount - discount_amount
                basket_line.discount_amount = discount_amount
                basket_line.discount_lines.append({"campaign_id": self.campaign.id, "discount_amount": discount_amount})
                basket_line.is_used = True

    def apply_campaign(self) -> Optional[Basket]:
        current_date: str = Date.get_current_date()
        if self.basket is not None and self.campaign is not None and Date.compare_date(self.campaign.start_date, current_date) <= 0 and Date.compare_date(self.campaign.end_date, current_date) >= 0 and self.campaign.is_active:
            self.set_criteria_product_list_for_campaign()
            self.set_action_product_list_for_campaign()
            self.sort_criteria_product_list()
            self.sort_action_product_list()

            if self.campaign.min_qty is not None:
                if self.campaign.all_product_criteria == AllProductCriteria.YES:
                    if self.get_basket_product_count() < self.campaign.min_qty:
                        return self.basket
                else:
                    if self.get_criteria_product_count() < self.campaign.min_qty:
                        return self.basket

            if self.campaign.min_amount is not None:
                if self.campaign.all_product_criteria == AllProductCriteria.YES:
                    if Operator.evaluate_basket_amount(self.basket) < self.campaign.min_amount:
                        return self.basket
                else:
                    if self.get_criteria_product_amount() < self.campaign.min_amount:
                        return self.basket

            if self.campaign.action_type == ActionType.AMOUNT:
                if self.campaign.all_product_action == AllProductAction.YES:
                    if self.campaign.max_discount is not None:
                        #her bir ürüne ayrı ayrı amount kadar indirim uygula max discountu geçmesin f1()
                        self.f1()
                        pass
                    elif self.campaign.action_qty is not None:
                        #action_qty kadar ürüne ayrı ayrı amount kadar indirim uygula f2()
                        self.f2()
                    else:
                        #her bir ürüne toplamda amount kadar indirim uygula f3()
                        self.f3()
                        pass
                else:
                    if self.campaign.max_discount is not None:
                        #kampanya ürünlerine ayrı ayrı amount kadar indirim uygula max discountu geçmesin f4()
                        self.f4()
                    elif self.campaign.action_qty is not None:
                        #kampanya ürünlerinden action_qty kadar ürüne ayrı ayrı amount kadar indirim uygula f5()
                        self.f5()
                    else:
                        #kampanya ürünlerine toplamda amount kadar indirim uygula f6()
                        self.f6()
            elif self.campaign.action_type == ActionType.PERCENT:
                if self.campaign.all_product_action == AllProductAction.YES:
                    if self.campaign.max_discount is not None:
                        if self.campaign.action_qty is not None:
                            #her bir üründen action_qty kadar ürüne ayrı ayrı rate kadar indirim uygula max discountu geçmesin f7()
                            self.f7()
                        else:
                            #her bir ürüne ayrı ayrı rate kadar indirim uygula max discountu geçmesin f8()
                            self.f8()
                    elif self.campaign.action_qty is not None:
                        #her bir üründen action_qty kadar ürüne ayrı ayrı rate kadar indirim uygula f9()
                        self.f9()
                    else:
                        #her bir ürüne ayrı ayrı rate kadar indirim uygula f10()
                        self.f10()
                else:
                    if self.campaign.max_discount is not None:
                        if self.campaign.action_qty is not None:
                            #kampanya ürünlerinden action_qty kadar ürüne ayrı ayrı rate kadar indirim uygula max discountu geçmesin f11()
                            self.f11()
                        else:
                            #kampanya ürünlerine ayrı ayrı rate kadar indirim uygula max discountu geçmesin f12()
                            self.f12()
                    elif self.campaign.action_qty is not None:
                        #kampanya ürünlerinden action_qty kadar ürüne ayrı ayrı rate kadar indirim uygula f13()
                        self.f13()
                    else:
                        #kampanya ayrı ayrı rate kadar indirim uygula f14()
                        self.f14()


            return self.basket
        else:
            return self.basket
