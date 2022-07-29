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
from Object.Campaign import Campaign
from Process.Finder import Finder
from Process.Optimizer import Optimizer
from fastapi import FastAPI
from pydantic import BaseModel


class RequestBasketLine(BaseModel):
    qty: int
    barcode: str
    amount: float
    unit_price: int


class RequestBasket(BaseModel):
    order_id: str
    org_id: str
    customer_id: str
    basket_lines: list[RequestBasketLine]
    payment_type_id: str
    payment_channel_id: str


class ResponseBasketLine:
    qty: int
    barcode: str
    amount: float
    unit_price: int
    discount_amount: float


class ResponseBasket:
    order_id: str
    customer_id: str
    basket_lines: list[ResponseBasketLine]
    payment_type_id: str
    payment_channel_id: str
    campaign_list: list[str]


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


def get_basked(request: RequestBasket) -> Basket:
    product_list: list[Product] = []
    for basket_line in request.basket_lines:
        product_helper = ProductHelper(barcode=basket_line.barcode)
        product = product_helper.get()
        if product is not None:
            product.qty = basket_line.qty
            product.amount = basket_line.amount
            product.unit_price = basket_line.unit_price
            product.is_used = False
            product.discount_amount = 0.0
            product_list.append(product)

    basket: Basket = Basket(order_id=request.order_id,
                            customer_id=request.customer_id,
                            payment_channel_id=request.payment_channel_id,
                            payment_type_id=request.payment_type_id,
                            product_list=product_list)

    return basket


def get_response_basket(applied_basket: Basket, applied_campaign_list: list[Campaign]) -> ResponseBasket:
    response: ResponseBasket = ResponseBasket()
    response.order_id = applied_basket.order_id
    response.customer_id = applied_basket.customer_id
    response.payment_type_id = applied_basket.payment_type_id
    response.payment_channel_id = applied_basket.payment_channel_id
    basket_lines: list[ResponseBasketLine] = []
    for product in applied_basket.product_list:
        basket_line: ResponseBasketLine = ResponseBasketLine()
        basket_line.qty = product.qty
        basket_line.amount = product.amount
        basket_line.barcode = product.barcode
        basket_line.unit_price = product.unit_price
        basket_line.discount_amount = product.discount_amount
        basket_lines.append(basket_line)
    response.basket_lines = basket_lines
    campaign_list: list[str] = []
    for campaign in applied_campaign_list:
        campaign_list.append(campaign.id)
    response.campaign_list = campaign_list
    return response


@app.post("/find_campaign_list")
def find_campaign_list(request: RequestBasket) -> ResponseBasket:
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
    campaign_list: list[Campaign] = []
    campaign_id_list: list[str] = finder.discover_campaign_list()
    for campaign_id in campaign_id_list:
        campaign_helper: CampaignHelper = CampaignHelper(campaign_id)
        campaign_list.append(campaign_helper.get())

    optimizer: Optimizer = Optimizer(basket=basket,
                                     campaign_list=campaign_list)

    optimum_result = optimizer.optimize_basket()
    applied_basket: Basket = optimum_result[0]
    applied_campaign_list: list[Campaign] = optimum_result[1]
    response: ResponseBasket = get_response_basket(applied_basket, applied_campaign_list)

    return response
