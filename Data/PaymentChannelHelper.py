from Abstract.DBObject import DBObject
from Object.PaymentChannel import PaymentChannel
from Data.DBHelper import DBHelper

class PaymentChannelHelper(DBObject):
    db_helper = None
    id: str = None
    payment_channel: PaymentChannel = None

    def __init__(self, id:str):
        self.db_helper = DBHelper()
        self.id = id
        self.__fetch()

    def __fetch(self) ->None:
        db_object = self.db_helper.find_by_id("payment_channel", self.id)
        if db_object is not None:
            self.payment_channel = PaymentChannel(id=db_object[0],
                                                  campaign_list=[] if db_object[2] is None else db_object[2].split(','))


    def get(self) ->PaymentChannel:
        return self.payment_channel