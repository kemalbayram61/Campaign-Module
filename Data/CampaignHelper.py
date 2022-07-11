from Abstract.DBObject import DBObject
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

    def get(self) ->Campaign:
        return self.campaign