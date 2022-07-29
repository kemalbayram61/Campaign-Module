from Object.ResponseBasketLine import ResponseBasketLine


class ResponseBasket:
    order_id: str
    customer_id: str
    basket_lines: list[ResponseBasketLine]
    payment_type_id: str
    payment_channel_id: str
    campaign_list: list[str]