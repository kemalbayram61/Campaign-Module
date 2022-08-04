from Abstract.DBObject import DBObject
from Abstract.DBObjectRole import DBObjectRole
from Object.Customer import Customer
from Data.DBHelper import DBHelper
from Data.RedisHelper import RedisHelper
import json

class CustomerHelper(DBObject):
    id: str = None
    customer: Customer = None
    role: DBObjectRole = None

    def __init__(self, id: str, role: DBObjectRole):
        self.id = id
        self.role = role
        if role == DBObjectRole.DATABASE and id != "-1":
            self.__fetch_on_db()
        elif role == DBObjectRole.REDIS and id != "-1":
            self.__fetch_on_redis()

    def __fetch_on_db(self) -> None:
        db_helper: DBHelper = DBHelper()
        db_object = db_helper.find_by_id("customer", self.id)
        if db_object is not None:
            self.customer = Customer(id=db_object[0],
                                     campaign_list=[] if db_object[1] is None else db_object[1].split(','))

    def __fetch_on_redis(self) -> None:
        customer_list: list[Customer] = self.get_all("-1")
        for customer in customer_list:
            if customer.id == self.id:
                self.customer = customer
                break

    def get(self) -> Customer:
        return self.customer

    def load_data(self, org_id: str) -> None:
        self.role = DBObjectRole.DATABASE
        redis_helper: RedisHelper = RedisHelper()
        customer_list: list[Customer] = self.get_all(org_id)
        customer_list_str: str = "[" + ",".join(list(map(lambda customer: str(customer), customer_list))) + "]"
        redis_helper.set("customer_list", customer_list_str)

    def get_all(self, org_id: str) -> list[Customer]:
        response: list[Customer] = []
        if self.role == DBObjectRole.DATABASE:
            db_helper: DBHelper = DBHelper()
            db_object_list = db_helper.select_all("customer")
            if db_object_list is not None:
                for db_object in db_object_list:
                    customer = Customer(id=str(db_object[0]),
                                        campaign_list=[] if db_object[1] is None else db_object[1].split(','))
                    response.append(customer)
        elif self.role == DBObjectRole.REDIS:
            redis_helper: RedisHelper = RedisHelper()
            customer_list_str: str = str(redis_helper.get("customer_list"))
            customer_list_str = customer_list_str[2:len(customer_list_str)-1].replace("\\n","")
            customer_dict_list: list[dict] = json.loads(customer_list_str)
            for customer_dict in customer_dict_list:
                response.append(Customer.dict_to_customer(customer_dict))
        return response
