from Abstract.DBObject import DBObject
from Abstract.ActionType import ActionType
from Abstract.AllPaymentType import AllPaymentType
from Abstract.AllCustomer import AllCustomer
from Abstract.AllPaymentChannel import AllPaymentChannel
from Abstract.AllProductAction import AllProductAction
from Abstract.AllProductCriteria import AllProductCriteria
from Abstract.DBObjectRole import DBObjectRole
from Object.Campaign import Campaign
from Data.DBHelper import DBHelper
from Data.RedisHelper import RedisHelper
import json


class CampaignHelper(DBObject):
    id: str = None
    campaign: Campaign = None
    role: DBObjectRole = None

    def __init__(self, id: str, role: DBObjectRole):
        self.id = id
        self.role = role
        if role == DBObjectRole.DATABASE:
            self.__fetch_on_db()
        elif role == DBObjectRole.REDIS:
            self.__fetch_on_redis()

    def __fetch_on_db(self) -> None:
        db_helper: DBHelper = DBHelper()
        db_object = db_helper.find_by_id("campaign", self.id)
        if db_object is not None:
            self.campaign = Campaign(id=str(db_object[0]),
                                     level=db_object[1],
                                     start_date=db_object[2],
                                     end_date=db_object[3],
                                     min_qty=db_object[4],
                                     min_amount=db_object[5],
                                     max_occurrence=db_object[6],
                                     action_type=ActionType.AMOUNT if db_object[7] == 0 else ActionType.PERCENT,
                                     action_amount=db_object[8],
                                     action_qty=db_object[9],
                                     max_discount=db_object[10],
                                     is_active=False if db_object[11] == 0 else True,
                                     all_payment_channel=AllPaymentChannel.NO if db_object[12] == 0 else AllPaymentChannel.YES,
                                     all_customer=AllCustomer.NO if db_object[13] == 0 else AllCustomer.YES,
                                     all_payment_type=AllPaymentType.NO if db_object[14] == 0 else AllPaymentType.YES,
                                     all_product_criteria=AllProductCriteria.NO if db_object[15] == 0 else AllProductCriteria.YES,
                                     all_product_action=AllProductAction.NO if db_object[16] == 0 else AllProductAction.YES)

    def __fetch_on_redis(self) -> None:
        redis_helper: RedisHelper = RedisHelper()
        campaign_list_str: str = str(redis_helper.get("campaign_list"))
        campaign_list_str = campaign_list_str[2:len(campaign_list_str)-1]
        campaign_dict_list: list[dict] = json.loads(campaign_list_str)
        for campaign_dict in campaign_dict_list:
            campaign_object: Campaign = Campaign.dict_to_campaign(campaign_dict)
            if campaign_object.id == self.id:
                self.campaign = campaign_object
                break

    def get(self) -> Campaign:
        return self.campaign

    def get_all(self, org_id: str) -> list[Campaign]:
        response: list[Campaign] = []
        if self.role == DBObjectRole.DATABASE:
            db_helper: DBHelper = DBHelper()
            db_object_list = db_helper.select_all("campaign")
            if db_object_list is not None:
                for db_object in db_object_list:
                    campaign = Campaign(id=str(db_object[0]),
                                        level=db_object[1],
                                        start_date=db_object[2],
                                        end_date=db_object[3],
                                        min_qty=db_object[4],
                                        min_amount=db_object[5],
                                        max_occurrence=db_object[6],
                                        action_type=ActionType.AMOUNT if db_object[7] == 0 else ActionType.PERCENT,
                                        action_amount=db_object[8],
                                        action_qty=db_object[9],
                                        max_discount=db_object[10],
                                        is_active=False if db_object[11] == 0 else True,
                                        all_payment_channel=AllPaymentChannel.NO if db_object[12] == 0 else AllPaymentChannel.YES,
                                        all_customer=AllCustomer.NO if db_object[13] == 0 else AllCustomer.YES,
                                        all_payment_type=AllPaymentType.NO if db_object[14] == 0 else AllPaymentType.YES,
                                        all_product_criteria=AllProductCriteria.NO if db_object[15] == 0 else AllProductCriteria.YES,
                                        all_product_action=AllProductAction.NO if db_object[16] == 0 else AllProductAction.YES)
                    response.append(campaign)
        elif self.role == DBObjectRole.REDIS:
            redis_helper: RedisHelper = RedisHelper()
            response: list[Campaign] = []
            campaign_list_str: str = str(redis_helper.get("campaign_list"))
            campaign_list_str = campaign_list_str[2:len(campaign_list_str)-1]
            campaign_dict_list: list[dict] = json.loads(campaign_list_str)
            for campaign_dict in campaign_dict_list:
                response.append(Campaign.dict_to_campaign(campaign_dict))
        return response

    def load_data(self, org_id: str) -> None:
        self.role = DBObjectRole.DATABASE
        redis_helper: RedisHelper = RedisHelper()
        campaign_list: list[Campaign] = self.get_all(org_id)
        campaign_list_str: str = "[" + ",".join(list(map(lambda campaign: str(campaign), campaign_list))) + "]"
        redis_helper.set("campaign_list", campaign_list_str)


