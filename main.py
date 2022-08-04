from Abstract.DBObjectRole import DBObjectRole
from Data.ProductHelper import ProductHelper
from Data.CustomerHelper import CustomerHelper
from Data.PaymentTypeHelper import PaymentTypeHelper
from Data.PaymentChannelHelper import PaymentChannelHelper
from Data.CampaignHelper import CampaignHelper
from Data.DBHelper import DBHelper
from Data.Config import Config
from Data.RedisHelper import RedisHelper
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
from Object.RequestBasket import RequestBasket
from Object.ResponseBasket import ResponseBasket
from Object.ResponseBasketLine import ResponseBasketLine
from Object.BasketLine import BasketLine
from Process.Finder import Finder
from Process.Optimizer import Optimizer
from fastapi import FastAPI


config = Config()
db_helper = DBHelper()
redis_helper = RedisHelper()

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


#load data on redis
campaign_helper: CampaignHelper = CampaignHelper("-1", DBObjectRole.REDIS)
campaign_helper.load_data("-1")
customer_helper: CustomerHelper = CustomerHelper("-1", DBObjectRole.REDIS)
customer_helper.load_data("-1")
payment_channel_helper: PaymentChannelHelper = PaymentChannelHelper("-1", DBObjectRole.REDIS)
payment_channel_helper.load_data("-1")

app = FastAPI()


def get_basked(request: RequestBasket) -> Basket:
    product_list: list[Product] = []
    basket_lines: list[BasketLine] = []
    for request_basket_line in request.basket_lines:
        product_helper = ProductHelper(barcode=request_basket_line.barcode, role=DBObjectRole.REDIS)
        product = product_helper.get()
        if product is not None:
            basket_line = BasketLine(barcode=request_basket_line.barcode,
                                     qty=request_basket_line.qty,
                                     unit_price=request_basket_line.unit_price,
                                     amount=request_basket_line.amount,
                                     is_used=False,
                                     discount_amount=0,
                                     line_amount=request_basket_line.amount,
                                     discount_lines=[])
            product_list.append(product)
            basket_lines.append(basket_line)

    basket: Basket = Basket(order_id=request.order_id,
                            customer_id=request.customer_id,
                            payment_channel_id=request.payment_channel_id,
                            payment_type_id=request.payment_type_id,
                            product_list=product_list,
                            basket_lines=basket_lines)

    return basket


def get_response_basket(applied_basket: Basket, applied_campaign_list: list[Campaign]) -> ResponseBasket:
    response: ResponseBasket = ResponseBasket()
    response.order_id = applied_basket.order_id
    response.customer_id = applied_basket.customer_id
    response.payment_type_id = applied_basket.payment_type_id
    response.payment_channel_id = applied_basket.payment_channel_id
    response_basket_lines: list[ResponseBasketLine] = []
    for basket_line in applied_basket.basket_lines:
        response_basket_line: ResponseBasketLine = ResponseBasketLine()
        response_basket_line.qty = basket_line.qty
        response_basket_line.amount = basket_line.amount
        response_basket_line.barcode = basket_line.barcode
        response_basket_line.unit_price = basket_line.unit_price
        response_basket_line.discount_amount = basket_line.discount_amount
        response_basket_lines.append(response_basket_line)
    response.basket_lines = response_basket_lines
    campaign_list: list[str] = []
    for campaign in applied_campaign_list:
        campaign_list.append(campaign.id)
    response.campaign_list = campaign_list
    return response


@app.post("/find_campaign_list")
def find_campaign_list(request: RequestBasket) -> ResponseBasket:
    basket: Basket = get_basked(request)
    customer_helper: CustomerHelper = CustomerHelper(request.customer_id, DBObjectRole.DATABASE)
    payment_type_helper: PaymentTypeHelper = PaymentTypeHelper(request.payment_type_id, DBObjectRole.REDIS)
    payment_channel_helper: PaymentChannelHelper = PaymentChannelHelper(request.payment_channel_id, DBObjectRole.REDIS)
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
        campaign_helper: CampaignHelper = CampaignHelper(campaign_id, DBObjectRole.REDIS)
        campaign_list.append(campaign_helper.get())

    optimizer: Optimizer = Optimizer(basket=basket,
                                     campaign_list=campaign_list)

    optimum_result = optimizer.optimize_basket()
    applied_basket: Basket = optimum_result[0]
    applied_campaign_list: list[Campaign] = optimum_result[1]
    response: ResponseBasket = get_response_basket(applied_basket, applied_campaign_list)

    return response
