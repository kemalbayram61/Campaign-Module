from Abstract.DBObject import DBObject
from Abstract.DBObjectRole import DBObjectRole
from Object.Customer import Customer
from Data.DBHelper import DBHelper
from Data.RedisHelper import RedisHelper
from Data.ApplicationCacheHelper import ApplicationCacheHelper
import json

class CustomerHelper(DBObject):
    id: str = None
    org_id: str = None
    customer: Customer = None
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
        db_object = db_helper.find_by_id("customer", self.id)
        if db_object is not None:
            self.customer = Customer(id=db_object[0],
                                     campaign_list=[] if db_object[1] is None else db_object[1].split(','),
                                     org_id=str(db_object[2]))

    def __fetch_on_redis(self) -> None:
        customer_list: list[Customer] = self.get_all(self.org_id)
        for customer in customer_list:
            if customer.id == self.id:
                self.customer = customer
                break

    def __fetch_on_application_cache(self) -> None:
        customer_list: list[Customer] = self.get_all(self.org_id)
        for customer in customer_list:
            if customer.id == self.id:
                self.customer = customer
                break

    def get(self) -> Customer:
        return self.customer

    def load_data(self) -> None:
        self.role = DBObjectRole.DATABASE
        redis_helper: RedisHelper = RedisHelper()
        customer_list: list[Customer] = self.get_all(self.org_id)
        customer_list_str: str = "[" + ",".join(list(map(lambda customer: str(customer), customer_list))) + "]"
        redis_helper.set("customer_list_" + self.org_id, customer_list_str)
        ApplicationCacheHelper.get_instance().store_data("customer_list_" + self.org_id, customer_list)

    def get_all(self, org_id: str) -> list[Customer]:
        response: list[Customer] = []
        if self.role == DBObjectRole.DATABASE:
            db_helper: DBHelper = DBHelper()
            db_object_list = db_helper.select_all("customer", org_id)
            if db_object_list is not None:
                for db_object in db_object_list:
                    customer = Customer(id=str(db_object[0]),
                                        campaign_list=[] if db_object[1] is None else db_object[1].split(','),
                                        org_id=str(db_object[2]))
                    response.append(customer)
        elif self.role == DBObjectRole.REDIS:
            redis_helper: RedisHelper = RedisHelper()
            customer_list_str: str = str(redis_helper.get("customer_list_" + org_id))
            customer_list_str = customer_list_str[2:len(customer_list_str)-1].replace("\\n","").replace('None', 'null')
            customer_dict_list: list[dict] = json.loads(customer_list_str)
            for customer_dict in customer_dict_list:
                response.append(Customer.dict_to_customer(customer_dict))
        elif self.role == DBObjectRole.APPLICATION_CACHE:
            response = ApplicationCacheHelper.get_instance().get_data("customer_list_" + org_id)
        return response
