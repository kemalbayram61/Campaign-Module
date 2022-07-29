from Abstract.DBObject import DBObject
from Object.PaymentType import PaymentType
from Data.DBHelper import DBHelper

class PaymentTypeHelper(DBObject):
    db_helper = None
    id:str = None
    payment_type: PaymentType = None

    def __init__(self, id:str):
        self.db_helper = DBHelper()
        self.id = id
        self.__fetch()

    def __fetch(self) ->None:
        db_object = self.db_helper.find_by_id("payment_channel", self.id)
        if db_object is not None:
            self.payment_type = PaymentType(id=db_object[0],
                                            campaign_list=[] if db_object[1] is None else db_object[1].split(','))


    def get(self) ->PaymentType:
        return self.payment_type