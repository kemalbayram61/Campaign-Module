from Abstract.DBObject import DBObject
from Object.Product import Product
from Data.DBHelper import DBHelper


class ProductHelper(DBObject):
    db_helper = None
    id: str = None
    barcode: str = None
    product: Product = None

    def __init__(self, id: str = None,
                 barcode: str = None):
        self.db_helper = DBHelper()
        self.id = id
        self.barcode = barcode
        self.__fetch()

    def __fetch(self) -> None:
        db_object = None
        if self.id is not None:
            db_object = self.db_helper.find_by_id("product", self.id)
        elif self.barcode is not None:
            db_object = self.db_helper.find_product_by_barcode(self.barcode)
        if db_object is not None:
            self.product = Product(id=str(db_object[0]),
                                   barcode=db_object[2],
                                   criteria_campaign_list=[] if db_object[3] is None else db_object[3].split(','),
                                   action_campaign_list=[] if db_object[4] is None else db_object[4].split(','))

    def get(self) -> Product:
        return self.product
