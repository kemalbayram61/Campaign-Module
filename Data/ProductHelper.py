from Abstract.DBObject import DBObject
from Abstract.DBObjectRole import DBObjectRole
from Object.Product import Product
from Data.DBHelper import DBHelper
from Data.RedisHelper import RedisHelper


class ProductHelper(DBObject):
    id: str = None
    barcode: str = None
    product: Product = None
    role: DBObjectRole = None

    def __init__(self, id: str = None,
                 barcode: str = None,
                 role: DBObjectRole = None):
        self.id = id
        self.barcode = barcode
        self.role = role
        if role == DBObjectRole.DATABASE:
            self.__fetch_on_db()
        elif role == DBObjectRole.REDIS:
            self.__fetch_on_redis()

    def __fetch_on_db(self) -> None:
        db_helper: DBHelper = DBHelper()
        db_object = None
        if self.id is not None:
            db_object = db_helper.find_by_id("product", self.id)
        elif self.barcode is not None:
            db_object = db_helper.find_product_by_barcode(self.barcode)
        if db_object is not None:
            self.product = Product(id=str(db_object[0]),
                                   barcode=db_object[1],
                                   criteria_campaign_list=[] if db_object[2] is None else db_object[2].split(','),
                                   action_campaign_list=[] if db_object[3] is None else db_object[3].split(','))

    def __fetch_on_redis(self) -> None:
        redis_helper: RedisHelper = RedisHelper()
        product_list: list[Product] = redis_helper.get("product_list")
        for product in product_list:
            if product.id == self.id:
                self.product = product
                break

    def get(self) -> Product:
        return self.product
