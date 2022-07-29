from Abstract.DBObject import DBObject
from Abstract.ActionType import ActionType
from Abstract.AllPaymentType import AllPaymentType
from Abstract.AllCustomer import AllCustomer
from Abstract.AllPaymentChannel import AllPaymentChannel
from Abstract.AllProductAction import AllProductAction
from Abstract.AllProductCriteria import AllProductCriteria
from Object.Campaign import Campaign
from Data.DBHelper import DBHelper

class CampaignHelper(DBObject):
    db_helper = None
    id:str = None
    campaign: Campaign = None

    def __init__(self, id:str):
        self.db_helper = DBHelper()
        self.id = id
        self.__fetch()

    def __fetch(self) ->None:
        db_object = self.db_helper.find_by_id("campaign", self.id)
        if db_object is not None:
            self.campaign = Campaign(id=str(db_object[0]),
                                     level=db_object[2],
                                     start_date=db_object[3],
                                     end_date=db_object[4],
                                     min_qty=db_object[5],
                                     min_amount=db_object[6],
                                     max_occurrence=db_object[7],
                                     action_type=ActionType.AMOUNT if db_object[8] == 0 else ActionType.PERCENT,
                                     action_amount=db_object[9],
                                     action_qty=db_object[10],
                                     max_discount=db_object[11],
                                     is_active=False if db_object[12] == 0 else True,
                                     all_payment_channel=AllPaymentChannel.NO if db_object[13] == 0 else AllPaymentChannel.YES,
                                     all_customer=AllCustomer.NO if db_object[13] == 0 else AllCustomer.YES,
                                     all_payment_type=AllPaymentType.NO if db_object[13] == 0 else AllPaymentType.YES,
                                     all_product_criteria=AllProductCriteria.NO if db_object[13] == 0 else AllProductCriteria.YES,
                                     all_product_action=AllProductAction.NO if db_object[13] == 0 else AllProductAction.YES)

    def get(self) ->Campaign:
        return self.campaign

    def get_all(self) ->list[Campaign]:
        response: list[Campaign] = []
        db_object_list = self.db_helper.select_all("campaign")
        if db_object_list is not None:
            for db_object in db_object_list:
                campaign = Campaign(id=str(db_object[0]),
                                    level=db_object[2],
                                    start_date=db_object[3],
                                    end_date=db_object[4],
                                    min_qty=db_object[5],
                                    min_amount=db_object[6],
                                    max_occurrence=db_object[7],
                                    action_type=ActionType.AMOUNT if db_object[8] == 0 else ActionType.PERCENT,
                                    action_amount=db_object[9],
                                    action_qty=db_object[10],
                                    max_discount=db_object[11],
                                    is_active=False if db_object[12] == 0 else True,
                                    all_payment_channel=AllPaymentChannel.NO if db_object[13] == 0 else AllPaymentChannel.YES,
                                    all_customer=AllCustomer.NO if db_object[13] == 0 else AllCustomer.YES,
                                    all_payment_type=AllPaymentType.NO if db_object[13] == 0 else AllPaymentType.YES,
                                    all_product_criteria=AllProductCriteria.NO if db_object[13] == 0 else AllProductCriteria.YES,
                                    all_product_action=AllProductAction.NO if db_object[13] == 0 else AllProductAction.YES)
                response.append(campaign)
        return response