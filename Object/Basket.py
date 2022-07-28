from Object.Product import Product


class Basket:
    order_id: str
    customer_id: str
    product_list: list[Product]
    payment_type_id: str
    payment_channel_id: str

    def __init__(self, order_id: str = None,
                 customer_id: str = None,
                 payment_channel_id: str = None,
                 product_list: list[Product] = None,
                 payment_type_id: str = None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_list = [] if product_list is None else product_list
        self.payment_type_id = payment_type_id
        self.payment_channel_id = payment_channel_id
