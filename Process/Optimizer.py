from Object.Basket import Basket
from Object.Campaign import Campaign
from Process.Operator import Operator
from Process.Finder import Finder
from threading import Thread
import copy

class Optimizer:
    basket: Basket
    campaign_list: list[Campaign]
    executed_stack: list[dict]

    def __init__(self, basket: Basket = None,
                 campaign_list: list[Campaign] = None):
        self.basket = basket
        self.campaign_list = campaign_list
        self.executed_stack = []

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

    def permutation(self, lst):

        if len(lst) == 0:
            return []

        if len(lst) == 1:
            return [lst]

        l = []

        for i in range(len(lst)):
            m = lst[i]
            remLst = lst[:i] + lst[i + 1:]
            for p in self.permutation(remLst):
                l.append([m] + p)
        return l

    def thread(self, applicable_list: list[Campaign]) -> list[dict]:
        applicable_list: applicable_list
        executed_list: list[Campaign] = []

        while len(applicable_list) != 0:
            executed_list.append(applicable_list[0])
            temp_basket = copy.deepcopy(self.basket)
            for campaign in executed_list:
                operator: Operator = Operator(basket=temp_basket,
                                              campaign=campaign)
                temp_basket = operator.apply_campaign()

            self.executed_stack.append(
                {"campaign_list": copy.deepcopy(executed_list),
                 "basket_amount": Operator.evaluate_basket_amount(temp_basket), "basket": copy.copy(temp_basket)})
            applicable_list = Finder.filter_campaign_on_basket(temp_basket, self.campaign_list[0].org_id)
            applicable_list = self.filter_list(executed_list, applicable_list)

    def optimize_basket(self) -> (Basket, list[Campaign]):
        #TODO sınırlamayı kaldırmayı unutma
        if len(self.campaign_list) > 3:
            self.campaign_list = self.campaign_list[:3]
        campaign_permutation_list: list[list[Campaign]] = self.permutation(copy.deepcopy(self.campaign_list))
        thread_list: list[Thread] = []
        for permutation in campaign_permutation_list:
            thread_list.append(Thread(target=self.thread, args=(permutation,)))

        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
        optimum_campaign = self.get_optimum_campaign(self.executed_stack)

        return optimum_campaign["basket"], optimum_campaign["campaign_list"] if optimum_campaign is not None else []
