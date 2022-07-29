from Abstract.DBObject import DBObject
from Object.Customer import Customer
from Data.DBHelper import DBHelper


class CustomerHelper(DBObject):
    db_helper = None
    id: str = None
    customer: Customer = None

    def __init__(self, id: str):
        self.db_helper = DBHelper()
        self.id = id
        self.__fetch()

    def __fetch(self) -> None:
        db_object = self.db_helper.find_by_id("customer", self.id)
        if db_object is not None:
            self.customer = Customer(id=db_object[0],
                                     campaign_list=[] if db_object[3] is None else db_object[3].split(','))

    def get(self) -> Customer:
        return self.customer
