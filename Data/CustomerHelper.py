from Abstract.DBObject import DBObject
from Abstract.DBObjectRole import DBObjectRole
from Object.Customer import Customer
from Data.DBHelper import DBHelper
from Data.RedisHelper import RedisHelper


class CustomerHelper(DBObject):
    id: str = None
    customer: Customer = None
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
        db_object = db_helper.find_by_id("customer", self.id)
        if db_object is not None:
            self.customer = Customer(id=db_object[0],
                                     campaign_list=[] if db_object[1] is None else db_object[1].split(','))

    def __fetch_on_redis(self) -> None:
        redis_helper: RedisHelper = RedisHelper()
        customer_list: list[Customer] = redis_helper.get("customer_list")
        for customer in customer_list:
            if customer.id == self.id:
                self.customer = customer
                break

    def get(self) -> Customer:
        return self.customer

    def load_data(self) -> None:
        pass

    def get_all(self, org_id: str) -> list[Customer]:
        pass
