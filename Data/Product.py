from Abstract.DBObject import DBObject
from Object.Product import Product as product_object
from Data.DBHelper import DBHelper
class ProductHelper(DBObject):
    db_helper = None
    def __init__(self):
        self.db_helper = DBHelper()

    def get(self) ->product_object:
        pass