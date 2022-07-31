from Object.Product import Product
from Object.BasketLine import BasketLine


class Basket:
    order_id: str
    customer_id: str
    product_list: list[Product]
    basket_lines: list[BasketLine]
    payment_type_id: str
    payment_channel_id: str

    def __init__(self, order_id: str = None,
                 customer_id: str = None,
                 payment_channel_id: str = None,
                 product_list: list[Product] = None,
                 basket_lines: list[BasketLine] = None,
                 payment_type_id: str = None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_list = [] if product_list is None else product_list
        self.basket_lines = [] if basket_lines is None else basket_lines
        self.payment_type_id = payment_type_id
        self.payment_channel_id = payment_channel_id
