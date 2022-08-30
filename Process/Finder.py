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
        self.campaign_helper = CampaignHelper("-1", DBObjectRole.REDIS, customer.org_id)

    @staticmethod
    def get_campaign_list_of_id_list(id_list: list[str], org_id: str) -> list[Campaign]:
        response: list[Campaign] = []
        for id in id_list:
            campaign_helper: CampaignHelper = CampaignHelper(id, DBObjectRole.REDIS, org_id)
            if campaign_helper.get() is not None:
                response.append(campaign_helper.get())
        return response

    def discover_campaign_list(self) -> list[Campaign]:
        if self.customer is not None and self.basked is not None and self.payment_type is not None and self.payment_channel is not None:
            product_list: list[Product] = self.basked.product_list
            criteria_campaign_id_list: list[str] = []
            action_campaign_id_list: list[str] = []
            response: list[str] = []

            all_campaign_list: list[Campaign] = self.campaign_helper.get_all(self.customer.org_id)
            for campaign in all_campaign_list:
                if campaign.all_customer == AllCustomer.YES or campaign.id in self.customer.campaign_list:
                    criteria_campaign_id_list.append(campaign.id)
                    action_campaign_id_list.append(campaign.id)

            for product in product_list:
                criteria_campaign_id_list = criteria_campaign_id_list + product.criteria_campaign_list
                action_campaign_id_list = action_campaign_id_list + product.action_campaign_list

            criteria_campaign_list: list[Campaign] = Finder.get_campaign_list_of_id_list(criteria_campaign_id_list, self.customer.org_id)

            for criteria_campaign in criteria_campaign_list:
                if criteria_campaign.id in action_campaign_id_list:
                    if criteria_campaign.all_customer == AllCustomer.YES or criteria_campaign.id in self.customer.campaign_list:
                        if criteria_campaign.all_payment_channel == AllPaymentChannel.YES or criteria_campaign.id in self.payment_channel.campaign_list:
                            if criteria_campaign.all_payment_type == AllPaymentType.YES or criteria_campaign.id in self.payment_type.campaign_list:
                                if criteria_campaign.id not in response:
                                    response.append(criteria_campaign.id)

            return Finder.get_campaign_list_of_id_list(response, self.customer.org_id)
        return []

    @staticmethod
    def filter_campaign_on_basket(basket: Basket, org_id: str) -> list[Campaign]:
        product_list: list[Product] = basket.product_list
        criteria_campaign_id_list: list[str] = []
        action_campaign_id_list: list[str] = []
        response_id_list: list[str] = []
        response: list[Campaign] = []
        campaign_helper: CampaignHelper = CampaignHelper("-1", DBObjectRole.REDIS, org_id)

        for index, product in enumerate(product_list, start=0):
            if basket.basket_lines[index].is_used is False:
                criteria_campaign_id_list = criteria_campaign_id_list + product.criteria_campaign_list
                action_campaign_id_list = action_campaign_id_list + product.action_campaign_list

        for criteria_campaign_id in criteria_campaign_id_list:
            if criteria_campaign_id in action_campaign_id_list:
                if criteria_campaign_id not in response:
                    response_id_list.append(criteria_campaign_id)

        if len(criteria_campaign_id_list) != 0:
            all_campaign_list: list[Campaign] = campaign_helper.get_all(org_id)
            for campaign in all_campaign_list:
                if campaign.all_product_action == AllProductAction.YES and campaign.all_product_criteria == AllProductCriteria.YES and campaign.all_customer == AllCustomer.YES and campaign.all_payment_type == AllPaymentType.YES and campaign.all_payment_channel == AllPaymentChannel.YES and campaign.id not in response:
                    response_id_list.append(campaign.id)

        response = Finder.get_campaign_list_of_id_list(response_id_list, org_id)

        return response
