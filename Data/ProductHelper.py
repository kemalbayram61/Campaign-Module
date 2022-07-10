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
            self.product = Product(self.id)

    def get(self) ->Product:
        return self.product