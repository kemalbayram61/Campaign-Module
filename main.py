from Data.ProductHelper import ProductHelper
from Data.CustomerHelper import CustomerHelper
from Data.PaymentTypeHelper import PaymentTypeHelper
from Data.PaymentChannelHelper import PaymentChannelHelper
from Data.CampaignHelper import CampaignHelper
from Data.DBHelper import DBHelper
from Data.Config import Config
from Mock.Product import ProductMock
from Mock.Customer import CustomerMock
from Mock.PaymentType import PaymentTypeMock
from Mock.PaymentChannel import PaymentChannelMock
from Mock.Campaign import CampaignMock
from Object.Basket import Basket
from Object.Product import Product
from Object.Customer import Customer
from Object.PaymentType import PaymentType
from Object.PaymentChannel import PaymentChannel
from Process.Finder import Finder
from fastapi import FastAPI
from pydantic import BaseModel


class RequestProduct(BaseModel):
    id: str
    qty: int


class Request(BaseModel):
    id: str
    customer_id: str
    product_list: list[RequestProduct]
    payment_type_id: str
    payment_channel_id: str


config = Config()
db_helper = DBHelper()

if config.get_reset_table_on_init():
    db_helper.reset_tables()

# add mock
product_mock = ProductMock()
db_helper.execute_command(product_mock.get_mock_sql())
customer_mock = CustomerMock()
db_helper.execute_command(customer_mock.get_mock_sql())
payment_channel_mock = PaymentChannelMock()
db_helper.execute_command(payment_channel_mock.get_mock_sql())
payment_type_mock = PaymentTypeMock()
db_helper.execute_command(payment_type_mock.get_mock_sql())
campaign_mock = CampaignMock()
db_helper.execute_command(campaign_mock.get_mock_sql())

app = FastAPI()


def get_basked(request: Request) -> Basket:
    product_list: list[Product] = []
    for product_req in request.product_list:
        product_helper = ProductHelper(product_req.id)
        product = product_helper.get()
        if product is not None:
            product.qty = product_req.qty
            product_list.append(product)

    basket: Basket = Basket(customer_id=request.customer_id,
                            payment_channel_id=request.payment_channel_id,
                            payment_type_id=request.payment_type_id,
                            product_list=product_list)

    return basket


@app.post("/find_campaign_list")
def find_campaign_list(request: Request):
    basket: Basket = get_basked(request)
    customer_helper: CustomerHelper = CustomerHelper(request.customer_id)
    payment_type_helper: PaymentTypeHelper = PaymentTypeHelper(request.payment_type_id)
    payment_channel_helper: PaymentChannelHelper = PaymentChannelHelper(request.payment_channel_id)
    customer: Customer = customer_helper.get()
    payment_type: PaymentType = payment_type_helper.get()
    payment_channel: PaymentChannel = payment_channel_helper.get()
    finder: Finder = Finder(customer=customer,
                            basket=basket,
                            payment_type=payment_type,
                            payment_channel=payment_channel)
    campaign_helper: CampaignHelper = CampaignHelper(customer.campaign_list[0])
    return finder.discover_campaign_list()
