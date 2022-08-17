from Abstract.DBObject import DBObject
from Abstract.DBObjectRole import DBObjectRole
from Object.PaymentType import PaymentType
from Data.DBHelper import DBHelper
from Data.RedisHelper import RedisHelper
from Data.ApplicationCacheHelper import ApplicationCacheHelper
import json


class PaymentTypeHelper(DBObject):
    id: str = None
    org_id: str = None
    payment_type: PaymentType = None
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
        db_helper = DBHelper()
        db_object = db_helper.find_by_id("payment_type", self.id)
        if db_object is not None:
            self.payment_type = PaymentType(id=db_object[0],
                                            campaign_list=[] if db_object[1] is None else db_object[1].split(','),
                                            org_id=str(db_object[2]))

    def __fetch_on_redis(self) -> None:
        payment_type_list: list[PaymentType] = self.get_all(self.org_id)
        for payment_type in payment_type_list:
            if payment_type.id == self.id:
                self.payment_type = payment_type
                break

    def __fetch_on_application_cache(self) -> None:
        payment_type_list: list[PaymentType] = self.get_all(self.org_id)
        for payment_type in payment_type_list:
            if payment_type.id == self.id:
                self.payment_type = payment_type
                break

    def get(self) ->PaymentType:
        return self.payment_type

    def load_data(self) -> None:
        self.role = DBObjectRole.DATABASE
        redis_helper: RedisHelper = RedisHelper()
        payment_type_list: list[PaymentType] = self.get_all(self.org_id)
        payment_type_list_str: str = "[" + ",".join(list(map(lambda payment_type: str(payment_type), payment_type_list))) + "]"
        redis_helper.set("payment_type_list_" + self.org_id, payment_type_list_str)
        ApplicationCacheHelper.get_instance().store_data("payment_type_list_" + self.org_id, payment_type_list)

    def get_all(self, org_id: str) -> list[PaymentType]:
        response: list[PaymentType] = []
        if self.role == DBObjectRole.DATABASE:
            db_helper: DBHelper = DBHelper()
            db_object_list = db_helper.select_all("payment_type", org_id)
            if db_object_list is not None:
                for db_object in db_object_list:
                    payment_type = PaymentType(id=str(db_object[0]),
                                               campaign_list=[] if db_object[1] is None else db_object[1].split(','),
                                               org_id=str(db_object[2]))
                    response.append(payment_type)
        elif self.role == DBObjectRole.REDIS:
            redis_helper: RedisHelper = RedisHelper()
            payment_type_list_str: str = str(redis_helper.get("payment_type_list_" + org_id))
            payment_type_list_str = payment_type_list_str[2:len(payment_type_list_str)-1].replace("\\n","").replace('None', 'null')
            payment_type_dict_list: list[dict] = json.loads(payment_type_list_str)
            for payment_type_dict in payment_type_dict_list:
                response.append(PaymentType.dict_to_payment_type(payment_type_dict))
        elif self.role == DBObjectRole.APPLICATION_CACHE:
            response = ApplicationCacheHelper.get_instance().get_data("payment_type_list_" + org_id)
        return response