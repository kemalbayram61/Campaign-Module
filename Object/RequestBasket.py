from pydantic import BaseModel
from Object.RequestBasketLine import RequestBasketLine


class RequestBasket(BaseModel):
    order_id: str
    org_id: str
    customer_external_code: str
    basket_lines: list[RequestBasketLine]
    payment_type_external_code: str
    payment_channel_external_code: str
