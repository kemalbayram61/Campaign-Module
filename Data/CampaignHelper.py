from Abstract.DBObject import DBObject
from Abstract.ActionType import ActionType
from Object.Campaign import Campaign
from Data.DBHelper import DBHelper

class ProductHelper(DBObject):
    db_helper = None
    id:str = None
    campaign: Campaign = None

    def __init__(self, id:str):
        self.db_helper = DBHelper()
        self.id = id
        self.__fetch()

    def __fetch(self) ->None:
        db_object = self.db_helper.find_by_id("campaign", self.id)
        if db_object is not None:
            self.campaign = Campaign(id=db_object[0],
                                     name=db_object[1],
                                     level=db_object[2],
                                     start_date=db_object[3],
                                     end_date=db_object[4],
                                     min_qty=db_object[5],
                                     min_amount=db_object[6],
                                     max_occurrence=db_object[7],
                                     action_type=ActionType.AMOUNT if db_object[8] == 0 else ActionType.PERCENT,
                                     action_amount=db_object[9],
                                     action_qty=db_object[10],
                                     max_discount=db_object[11],
                                     is_active=False if db_object[12] == 0 else True)

    def get(self) ->Campaign:
        return self.campaign