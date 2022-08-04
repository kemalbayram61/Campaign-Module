from Abstract.AllCustomer import AllCustomer
from Abstract.AllPaymentType import AllPaymentType
from Abstract.AllPaymentChannel import AllPaymentChannel
from Abstract.AllProductCriteria import AllProductCriteria
from Abstract.AllProductAction import AllProductAction
from Abstract.DBObjectRole import DBObjectRole
from Object.Basket import Basket
from Object.Product import Product
from Object.Customer import Customer
from Object.PaymentType import PaymentType
from Object.PaymentChannel import PaymentChannel
from Object.Campaign import Campaign
from Data.CampaignHelper import CampaignHelper


class Finder:
    basked: Basket
    customer: Customer
    payment_channel: PaymentChannel
    payment_type: PaymentType
    campaign_helper: CampaignHelper

    def __init__(self, customer: Customer = None,
                 basket: Basket = None,
                 payment_channel: PaymentChannel = None,
                 payment_type: PaymentType = None):
        self.customer = customer
        self.basked = basket
        self.payment_type = payment_type
        self.payment_channel = payment_channel
        self.campaign_helper = CampaignHelper("-1", DBObjectRole.REDIS)

    def __get_campaign_list_of_id_list(self, id_list: list[str]) ->list[Campaign]:
        response: list[Campaign] = []
        for id in id_list:
            campaign_helper: CampaignHelper = CampaignHelper(id, DBObjectRole.REDIS)
            response.append(campaign_helper.get())
        return response

    def discover_campaign_list(self) -> list[str]:
        if self.customer is not None and self.basked is not None and self.payment_type is not None and self.payment_channel is not None:
            product_list: list[Product] = self.basked.product_list
            criteria_campaign_id_list: list[str] = []
            action_campaign_id_list: list[str] = []
            response: list[str] = []
            for product in product_list:
                criteria_campaign_id_list = criteria_campaign_id_list + product.criteria_campaign_list
                action_campaign_id_list = action_campaign_id_list + product.action_campaign_list

            criteria_campaign_list: list[Campaign] = self.__get_campaign_list_of_id_list(criteria_campaign_id_list)
            all_campaign_list: list[Campaign] = self.campaign_helper.get_all("-1")

            for criteria_campaign in criteria_campaign_list:
                if criteria_campaign.id in action_campaign_id_list:
                    if criteria_campaign.all_customer == AllCustomer.YES or criteria_campaign.id in self.customer.campaign_list:
                        if criteria_campaign.all_payment_channel == AllPaymentChannel.YES or criteria_campaign.id in self.payment_channel.campaign_list:
                            if criteria_campaign.all_payment_type == AllPaymentType.YES or criteria_campaign.id in self.payment_type.campaign_list:
                                if criteria_campaign.id not in response:
                                    response.append(criteria_campaign.id)

            for campaign in all_campaign_list:
                if campaign.all_product_action == AllProductAction.YES and campaign.all_product_criteria == AllProductCriteria.YES and campaign.all_customer == AllCustomer.YES and campaign.all_payment_type == AllPaymentType.YES and campaign.all_payment_channel == AllPaymentChannel.YES and campaign.id not in response:
                    response.append(campaign.id)

            return response
        return []

    @staticmethod
    def filter_campaign_on_basket(basket: Basket) -> list[Campaign]:
        product_list: list[Product] = basket.product_list
        criteria_campaign_list: list[str] = []
        action_campaign_list: list[str] = []
        response_id_list: list[str] = []
        response: list[Campaign] = []
        for index, product in enumerate(product_list, start=0):
            if basket.basket_lines[index].is_used is False:
                criteria_campaign_list = criteria_campaign_list + product.criteria_campaign_list
                action_campaign_list = action_campaign_list + product.action_campaign_list

        for criteria_campaign in criteria_campaign_list:
            if criteria_campaign in action_campaign_list:
                response_id_list.append(criteria_campaign)

        for campaign_id in response_id_list:
            campaign_helper: CampaignHelper = CampaignHelper(campaign_id, DBObjectRole.REDIS)
            response.append(campaign_helper.get())

        return response
