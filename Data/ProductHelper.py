from Abstract.DBObject import DBObject
from Abstract.DBObjectRole import DBObjectRole
from Object.Product import Product
from Data.DBHelper import DBHelper
from Data.RedisHelper import RedisHelper
import json


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
        product_list: list[Product] = self.get_all("-1")
        for product in product_list:
            if product.id == self.id:
                self.product = product
                break

    def get(self) -> Product:
        return self.product

    def load_data(self, org_id: str) -> None:
        self.role = DBObjectRole.DATABASE
        redis_helper: RedisHelper = RedisHelper()
        product_list: list[Product] = self.get_all(org_id)
        product_list_str: str = "[" + ",".join(list(map(lambda product: str(product), product_list))) + "]"
        redis_helper.set("product_list", product_list_str)

    def get_all(self, org_id: str) -> list[Product]:
        response: list[Product] = []
        if self.role == DBObjectRole.DATABASE:
            db_helper: DBHelper = DBHelper()
            db_object_list = db_helper.select_all("product")
            if db_object_list is not None:
                for db_object in db_object_list:
                    product = Product(id=str(db_object[0]),
                                      barcode=db_object[1],
                                      criteria_campaign_list=[] if db_object[2] is None else db_object[2].split(','),
                                      action_campaign_list=[] if db_object[3] is None else db_object[3].split(','))
                    response.append(product)
        elif self.role == DBObjectRole.REDIS:
            redis_helper: RedisHelper = RedisHelper()
            product_list_str: str = str(redis_helper.get("product_list"))
            product_list_str = product_list_str[2:len(product_list_str)-1].replace("\\n","")
            product_dict_list: list[dict] = json.loads(product_list_str)
            for product_dict in product_dict_list:
                response.append(Product.dict_to_product(product_dict))
        return response