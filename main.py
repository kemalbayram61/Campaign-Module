from Abstract.DBObjectRole import DBObjectRole
from Data.ProductHelper import ProductHelper
from Data.CustomerHelper import CustomerHelper
from Data.PaymentTypeHelper import PaymentTypeHelper
from Data.PaymentChannelHelper import PaymentChannelHelper
from Data.CampaignHelper import CampaignHelper
from Data.DBHelper import DBHelper
from Data.Config import Config
from Data.ApplicationCacheHelper import ApplicationCacheHelper
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


ApplicationCacheHelper()
config = Config()
db_helper = DBHelper()
redis_helper = RedisHelper()

if config.get_reset_table_on_init():
    db_helper.reset_tables()
    redis_helper.reset()

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


def load_data(org_id: str):
    campaign_helper: CampaignHelper = CampaignHelper("-1", DBObjectRole.DATABASE, org_id)
    campaign_helper.load_data()
    customer_helper: CustomerHelper = CustomerHelper(id="-1", role=DBObjectRole.DATABASE, org_id=org_id)
    customer_helper.load_data()
    payment_channel_helper: PaymentChannelHelper = PaymentChannelHelper(id="-1", role=DBObjectRole.DATABASE, org_id=org_id)
    payment_channel_helper.load_data()
    payment_type_helper: PaymentTypeHelper = PaymentTypeHelper(id="-1", role=DBObjectRole.DATABASE, org_id=org_id)
    payment_type_helper.load_data()
    product_helper: ProductHelper = ProductHelper(id="-1", role=DBObjectRole.DATABASE, org_id=org_id)
    product_helper.load_data()

app = FastAPI()


def get_basked(request: RequestBasket) -> Basket:
    product_list: list[Product] = []
    basket_lines: list[BasketLine] = []
    for request_basket_line in request.basket_lines:
        product_helper = ProductHelper(barcode=request_basket_line.barcode, role=DBObjectRole.REDIS, org_id=request.org_id)
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
                            customer_external_code=request.customer_external_code,
                            payment_channel_external_code=request.payment_channel_external_code,
                            payment_type_external_code=request.payment_type_external_code,
                            product_list=product_list,
                            basket_lines=basket_lines)

    return basket


def get_response_basket(applied_basket: Basket, applied_campaign_list: list[Campaign]) -> ResponseBasket:
    response: ResponseBasket = ResponseBasket()
    response.order_id = applied_basket.order_id
    response.customer_external_code = applied_basket.customer_external_code
    response.payment_type_external_code = applied_basket.payment_type_external_code
    response.payment_channel_external_code = applied_basket.payment_channel_external_code
    response_basket_lines: list[ResponseBasketLine] = []
    for basket_line in applied_basket.basket_lines:
        response_basket_line: ResponseBasketLine = ResponseBasketLine()
        response_basket_line.qty = basket_line.qty
        response_basket_line.amount = basket_line.amount
        response_basket_line.barcode = basket_line.barcode
        response_basket_line.unit_price = basket_line.unit_price
        response_basket_line.discount_amount = basket_line.discount_amount
        response_basket_line.line_amount = basket_line.line_amount
        response_basket_line.discount_lines = basket_line.discount_lines
        response_basket_lines.append(response_basket_line)
    response.basket_lines = response_basket_lines
    campaign_list: list[str] = []
    for campaign in applied_campaign_list:
        campaign_list.append(campaign.external_code)
    response.campaign_list = campaign_list
    return response


@app.post("/find_campaign_list")
def find_campaign_list(request: RequestBasket) -> ResponseBasket:
    load_data(request.org_id)
    basket: Basket = get_basked(request)
    customer_helper: CustomerHelper = CustomerHelper(external_code=request.customer_external_code, role=DBObjectRole.DATABASE, org_id=request.org_id)
    payment_type_helper: PaymentTypeHelper = PaymentTypeHelper(external_code=request.payment_type_external_code, role=DBObjectRole.REDIS, org_id=request.org_id)
    payment_channel_helper: PaymentChannelHelper = PaymentChannelHelper(external_code=request.payment_channel_external_code, role=DBObjectRole.REDIS, org_id=request.org_id)
    customer: Customer = customer_helper.get()
    payment_type: PaymentType = payment_type_helper.get()
    payment_channel: PaymentChannel = payment_channel_helper.get()
    finder: Finder = Finder(customer=customer,
                            basket=basket,
                            payment_type=payment_type,
                            payment_channel=payment_channel)

    campaign_list: list[Campaign] = finder.discover_campaign_list()

    optimizer: Optimizer = Optimizer(basket=basket,
                                     campaign_list=campaign_list)

    optimum_result = optimizer.optimize_basket()
    response: ResponseBasket = get_response_basket(optimum_result[0], optimum_result[1])

    return response
