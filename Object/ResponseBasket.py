from Object.ResponseBasketLine import ResponseBasketLine
from pydantic import BaseModel


class ResponseBasket:
    order_id: str
    customer_external_code: str
    basket_lines: list[ResponseBasketLine]
    payment_type_external_code: str
    payment_channel_external_code: str
    campaign_list: list[str]