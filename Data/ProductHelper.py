from Abstract.DBObject import DBObject
from Object.Product import Product
from Data.DBHelper import DBHelper

class ProductHelper(DBObject):
    db_helper = None
    id:str = None
    product: Product = None

    def __init__(self, id:str):
        self.db_helper = DBHelper()
        self.id = id
        self.__fetch()

    def __fetch(self) ->None:
        db_object = self.db_helper.find_by_id("product", self.id)
        if(db_object is not None):
            self.product = Product(id=db_object[0],
                                   name=db_object[1],
                                   barcode=db_object[2],
                                   property=db_object[3],
                                   criteriaCampaignList=[] if db_object[4] is None else db_object[4].split(','),
                                   actionCampaignList=[] if db_object[5] is None else db_object[5].split(','),
                                   unitPrice=db_object[6])


    def get(self) ->Product:
        return self.product