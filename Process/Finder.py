from Data.CampaignHelper import CampaignHelper
from Object.Basket import Basket
from Object.Product import Product
from Object.Customer import Customer
from Object.PaymentType import PaymentType
from Object.PaymentChannel import PaymentChannel
from Object.Campaign import Campaign


class Finder:
    basked: Basket
    customer: Customer
    payment_channel: PaymentChannel
    payment_type: PaymentType

    def __init__(self, customer: Customer = None,
                 basket: Basket = None,
                 payment_channel: PaymentChannel = None,
                 payment_type: PaymentType = None):
        self.customer = customer
        self.basked = basket
        self.payment_type = payment_type
        self.payment_channel = payment_channel

    def discover_campaign_list(self) -> list[str]:
        if self.customer is not None and self.basked is not None and self.payment_type is not None and self.payment_channel is not None:
            product_list: list[Product] = self.basked.product_list
            criteria_campaign_list: list[str] = []
            action_campaign_list: list[str] = []
            response: list[str] = []
            for product in product_list:
                criteria_campaign_list = criteria_campaign_list + product.criteria_campaign_list
                action_campaign_list = action_campaign_list + product.action_campaign_list

            for criteria in criteria_campaign_list:
                if criteria in action_campaign_list and criteria in self.customer.campaign_list and criteria not in response and criteria in self.payment_channel.campaign_list and criteria in self.payment_type.campaign_list:
                    response.append(criteria)

            return response
        return []

    @staticmethod
    def filter_campaign_on_basket(basket: Basket) -> list[Campaign]:
        product_list: list[Product] = basket.product_list
        criteria_campaign_list: list[str] = []
        action_campaign_list: list[str] = []
        response_id_list: list[str] = []
        response: list[Campaign] = []
        for product in product_list:
            if product.is_used is False:
                criteria_campaign_list = criteria_campaign_list + product.criteria_campaign_list
                action_campaign_list = action_campaign_list + product.action_campaign_list

        for criteria_campaign in criteria_campaign_list:
            if criteria_campaign in action_campaign_list:
                response_id_list.append(criteria_campaign)

        for campaign_id in response_id_list:
            campaign_helper: CampaignHelper = CampaignHelper(campaign_id)
            response.append(campaign_helper.get())

        return response
