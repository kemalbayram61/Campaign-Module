from fastapi import FastAPI
from pydantic import BaseModel
from Data.ProductHelper import ProductHelper
from Data.CustomerHelper import CustomerHelper
from Mock.Product import ProductMock
from Mock.Customer import CustomerMock
from Mock.PaymentType import PaymentTypeMock
from Mock.PaymentChannel import PaymentChannelMock
from Data.DBHelper import DBHelper
from Data.Config import Config
from Object.Basket import Basket
from Object.Product import Product
from Object.Customer import Customer
from Process.Finder import Finder

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
payment_channel_mock = PaymentChannelMock()
db_helper.execute_command(payment_channel_mock.get_mock_sql())
payment_type_mock = PaymentTypeMock()
db_helper.execute_command(payment_type_mock.get_mock_sql())

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
    customer_helper: CustomerHelper = CustomerHelper(request.customerID)
    customer: Customer = customer_helper.get()
    finder: Finder = Finder(customer=customer,
                            basket=basket)
    return finder.discover_campaign_list()