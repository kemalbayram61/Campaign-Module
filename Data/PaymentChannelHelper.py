from Abstract.DBObject import DBObject
from Abstract.DBObjectRole import DBObjectRole
from Object.PaymentChannel import PaymentChannel
from Data.DBHelper import DBHelper
from Data.RedisHelper import RedisHelper
from Data.ApplicationCacheHelper import ApplicationCacheHelper
import json

class PaymentChannelHelper(DBObject):
    id: str = None
    org_id: str = None
    payment_channel: PaymentChannel = None
    role: DBObjectRole = None

    def __init__(self, id: str, role: DBObjectRole, org_id: str):
        self.id = id
        self.role = role
        self.org_id = org_id
        if role == DBObjectRole.DATABASE and id != "-1":
            self.__fetch_on_db()
        elif role == DBObjectRole.REDIS and id != "-1":
            self.__fetch_on_redis()
        elif role == DBObjectRole.APPLICATION_CACHE and id != "-1":
            self.__fetch_on_application_cache()

    def __fetch_on_db(self) -> None:
        db_helper: DBHelper = DBHelper()
        db_object = db_helper.find_by_id("payment_channel", self.id)
        if db_object is not None:
            self.payment_channel = PaymentChannel(id=db_object[0],
                                                  campaign_list=[] if db_object[1] is None else db_object[1].split(','),
                                                  org_id=str(db_object[2]))

    def __fetch_on_redis(self) -> None:
        payment_channel_list: list[PaymentChannel] = self.get_all(self.org_id)
        for payment_channel in payment_channel_list:
            if payment_channel.id == self.id:
                self.payment_channel = payment_channel
                break

    def __fetch_on_application_cache(self) -> None:
        payment_channel_list: list[PaymentChannel] = self.get_all(self.org_id)
        for payment_channel in payment_channel_list:
            if payment_channel.id == self.id:
                self.payment_channel = payment_channel
                break

    def get(self) ->PaymentChannel:
        return self.payment_channel

    def load_data(self) -> None:
        self.role = DBObjectRole.DATABASE
        redis_helper: RedisHelper = RedisHelper()
        payment_channel_list: list[PaymentChannel] = self.get_all(self.org_id)
        payment_channel_list_str: str = "[" + ",".join(list(map(lambda payment_channel: str(payment_channel), payment_channel_list))) + "]"
        redis_helper.set("payment_channel_list_" + self.org_id, payment_channel_list_str)
        ApplicationCacheHelper.get_instance().store_data("payment_channel_list_" + self.org_id, payment_channel_list)

    def get_all(self, org_id: str) -> list[PaymentChannel]:
        response: list[PaymentChannel] = []
        if self.role == DBObjectRole.DATABASE:
            db_helper: DBHelper = DBHelper()
            db_object_list = db_helper.select_all("payment_channel", org_id)
            if db_object_list is not None:
                for db_object in db_object_list:
                    payment_channel = PaymentChannel(id=str(db_object[0]),
                                                     campaign_list=[] if db_object[1] is None else db_object[1].split(','),
                                                     org_id=str(db_object[2]))
                    response.append(payment_channel)
        elif self.role == DBObjectRole.REDIS:
            redis_helper: RedisHelper = RedisHelper()
            payment_channel_list_str: str = str(redis_helper.get("payment_channel_list_" + org_id))
            payment_channel_list_str = payment_channel_list_str[2:len(payment_channel_list_str)-1].replace("\\n","").replace('None', 'null')
            payment_channel_dict_list: list[dict] = json.loads(payment_channel_list_str)
            for payment_channel_dict in payment_channel_dict_list:
                response.append(PaymentChannel.dict_to_payment_channel(payment_channel_dict))
        elif self.role == DBObjectRole.APPLICATION_CACHE:
            response = ApplicationCacheHelper.get_instance().get_data("payment_channel_list_" + org_id)
        return response