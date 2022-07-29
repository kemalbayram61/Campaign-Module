from pydantic import BaseModel
from Object.RequestBasketLine import RequestBasketLine


class RequestBasket(BaseModel):
    order_id: str
    org_id: str
    customer_id: str
    basket_lines: list[RequestBasketLine]
    payment_type_id: str
    payment_channel_id: str
