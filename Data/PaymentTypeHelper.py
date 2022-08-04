from Abstract.DBObject import DBObject
from Abstract.DBObjectRole import DBObjectRole
from Object.PaymentType import PaymentType
from Data.DBHelper import DBHelper
from Data.RedisHelper import RedisHelper

class PaymentTypeHelper(DBObject):
    id:str = None
    payment_type: PaymentType = None
    role: DBObjectRole = None

    def __init__(self, id:str, role: DBObjectRole):
        self.id = id
        self.role = role
        if role == DBObjectRole.DATABASE:
            self.__fetch_on_db()
        elif role == DBObjectRole.REDIS:
            self.__fetch_on_redis()

    def __fetch_on_db(self) ->None:
        db_helper = DBHelper()
        db_object = db_helper.find_by_id("payment_channel", self.id)
        if db_object is not None:
            self.payment_type = PaymentType(id=db_object[0],
                                            campaign_list=[] if db_object[1] is None else db_object[1].split(','))

    def __fetch_on_redis(self) ->None:
        redis_helper: RedisHelper = RedisHelper()
        payment_type_list: list[PaymentType] = self.get_all("-1")
        for payment_type in payment_type_list:
            if payment_type.id == self.id:
                self.payment_type = payment_type
                break

    def get(self) ->PaymentType:
        return self.payment_type

    def load_data(self) -> None:
        pass

    def get_all(self, org_id: str) -> list[PaymentType]:
        pass