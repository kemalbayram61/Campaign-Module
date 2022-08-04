from Abstract.DBObject import DBObject
from Abstract.DBObjectRole import DBObjectRole
from Object.PaymentChannel import PaymentChannel
from Data.DBHelper import DBHelper
from Data.RedisHelper import RedisHelper
import json

class PaymentChannelHelper(DBObject):
    id: str = None
    payment_channel: PaymentChannel = None
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
        db_object = db_helper.find_by_id("payment_channel", self.id)
        if db_object is not None:
            self.payment_channel = PaymentChannel(id=db_object[0],
                                                  campaign_list=[] if db_object[1] is None else db_object[1].split(','))

    def __fetch_on_redis(self) -> None:
        payment_channel_list: list[PaymentChannel] = self.get_all("-1")
        for payment_channel in payment_channel_list:
            if payment_channel.id == self.id:
                self.payment_channel = payment_channel
                break

    def get(self) ->PaymentChannel:
        return self.payment_channel

    def load_data(self, org_id: str) -> None:
        self.role = DBObjectRole.DATABASE
        redis_helper: RedisHelper = RedisHelper()
        payment_channel_list: list[PaymentChannel] = self.get_all(org_id)
        payment_channel_list_str: str = "[" + ",".join(list(map(lambda payment_channel: str(payment_channel), payment_channel_list))) + "]"
        redis_helper.set("payment_channel_list", payment_channel_list_str)

    def get_all(self, org_id: str) -> list[PaymentChannel]:
        response: list[PaymentChannel] = []
        if self.role == DBObjectRole.DATABASE:
            db_helper: DBHelper = DBHelper()
            db_object_list = db_helper.select_all("payment_channel")
            if db_object_list is not None:
                for db_object in db_object_list:
                    payment_channel = PaymentChannel(id=str(db_object[0]),
                                                     campaign_list=[] if db_object[1] is None else db_object[1].split(','))
                    response.append(payment_channel)
        elif self.role == DBObjectRole.REDIS:
            redis_helper: RedisHelper = RedisHelper()
            payment_channel_list_str: str = str(redis_helper.get("payment_channel_list"))
            payment_channel_list_str = payment_channel_list_str[2:len(payment_channel_list_str)-1].replace("\\n","")
            payment_channel_dict_list: list[dict] = json.loads(payment_channel_list_str)
            for payment_channel_dict in payment_channel_dict_list:
                response.append(PaymentChannel.dict_to_payment_channel(payment_channel_dict))
        return response