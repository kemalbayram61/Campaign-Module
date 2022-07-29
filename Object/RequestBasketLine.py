from pydantic import BaseModel


class RequestBasketLine(BaseModel):
    qty: int
    barcode: str
    amount: float
    unit_price: int