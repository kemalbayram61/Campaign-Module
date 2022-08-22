from Object.Product import Product
from Object.BasketLine import BasketLine


class Basket:
    order_id: str
    customer_external_code: str
    product_list: list[Product]
    basket_lines: list[BasketLine]
    payment_type_external_code: str
    payment_channel_external_code: str

    def __init__(self, order_id: str = None,
                 customer_external_code: str = None,
                 payment_channel_external_code: str = None,
                 product_list: list[Product] = None,
                 basket_lines: list[BasketLine] = None,
                 payment_type_external_code: str = None):
        self.order_id = order_id
        self.customer_external_code = customer_external_code
        self.product_list = [] if product_list is None else product_list
        self.basket_lines = [] if basket_lines is None else basket_lines
        self.payment_type_external_code = payment_type_external_code
        self.payment_channel_external_code = payment_channel_external_code
