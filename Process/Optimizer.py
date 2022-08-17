from Object.Basket import Basket
from Object.Campaign import Campaign
from Process.Operator import Operator
from Process.Finder import Finder
import copy


class Optimizer:
    basket: Basket
    campaign_list: list[Campaign]

    def __init__(self, basket: Basket = None,
                 campaign_list: list[Campaign] = None):
        self.basket = basket
        self.campaign_list = campaign_list

    def is_exist_campaign(self, campaign: Campaign, campaign_list: list[Campaign]) -> bool:
        for cmp in campaign_list:
            if cmp.id == campaign.id:
                return True
        return False

    def filter_list(self, list1: list[Campaign], list2: [Campaign]) -> list[Campaign]:
        response: list[Campaign] = []
        for campaign in list2:
            if self.is_exist_campaign(campaign, list1) is False:
                response.append(campaign)
        return response

    def get_optimum_campaign(self, executed_stack: list[dict]) -> dict:
        minimum_amount: dict = None
        for executed in executed_stack:
            if minimum_amount is None or minimum_amount["basket_amount"] > executed["basket_amount"]:
                minimum_amount = executed
        return minimum_amount

    def optimize_basket(self) -> (Basket, list[Campaign]):
        applicable_list: list[Campaign] = self.campaign_list
        executed_list: list[Campaign] = []
        executed_stack: list[dict] = []

        #sort all campaigns with different combinations and assign to applicable_list object
        while len(applicable_list) != 0:
            executed_list.append(applicable_list[0])
            temp_basket = copy.deepcopy(self.basket)
            for campaign in executed_list:
                operator: Operator = Operator(basket=temp_basket,
                                              campaign=campaign)
                temp_basket = operator.apply_campaign()

            executed_stack.append(
                {"campaign_list": copy.deepcopy(executed_list), "basket_amount": Operator.evaluate_basket_amount(temp_basket), "basket": copy.copy(temp_basket)})
            applicable_list = Finder.filter_campaign_on_basket(temp_basket, self.campaign_list[0].org_id)
            applicable_list = self.filter_list(executed_list, applicable_list)

        optimum_campaign = self.get_optimum_campaign(executed_stack)

        return optimum_campaign["basket"], optimum_campaign["campaign_list"] if optimum_campaign is not None else []
