from Abstract.DBObject import DBObject
from Abstract.DBObjectRole import DBObjectRole
from Object.PaymentChannel import PaymentChannel
from Data.DBHelper import DBHelper
from Data.RedisHelper import RedisHelper


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
        redis_helper: RedisHelper = RedisHelper()
        payment_channel_list: list[PaymentChannel] = redis_helper.get("payment_channel_list")
        for payment_channel in payment_channel_list:
            if payment_channel.id == self.id:
                self.payment_channel = payment_channel
                break

    def get(self) ->PaymentChannel:
        return self.payment_channel

    def load_data(self) -> None:
        pass

    def get_all(self, org_id: str) -> list[PaymentChannel]:
        pass