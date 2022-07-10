from fastapi import FastAPI
from pydantic import BaseModel
from Data.ProductHelper import ProductHelper
from Mock.Product import ProductMock
from Mock.Customer import CustomerMock
from Data.DBHelper import DBHelper
from Data.Config import Config
from Object.Basket import Basket
from Object.Product import Product

class RequestProduct(BaseModel):
    id:str
    qty: int

class Request(BaseModel):
    id: str
    customerID: str
    productList: list[RequestProduct]
    paymentTypeID: str
    paymentChannelID: str

config = Config()
db_helper = DBHelper()
if (config.get_reset_table_on_init()):
    db_helper.reset_tables()

#add mock
product_mock = ProductMock()
db_helper.execute_command(product_mock.get_mock_sql())
customer_mock = CustomerMock()
db_helper.execute_command(customer_mock.get_mock_sql())

app = FastAPI()

def get_basked(request: Request)->Basket:
    productList: list[Product] = []
    for product_req in request.productList:
        product_helper = ProductHelper(product_req.id)
        product = product_helper.get()
        if(product is not None):
            product.qty = product_req.qty
            productList.append(product)

    basket: Basket = Basket(customerID=request.customerID,
                            paymentChannelID=request.paymentChannelID,
                            paymentTypeID=request.paymentTypeID,
                            productList=productList)

    return basket

@app.post("/find_campaign_list")
def find_campaign_list(request: Request):
    basket: Basket = get_basked(request)
    return basket