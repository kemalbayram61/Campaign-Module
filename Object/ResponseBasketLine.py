class ResponseBasketLine:
    qty: int
    barcode: str
    amount: float
    unit_price: int
    discount_amount: float
    line_amount: float
    discount_lines: list[dict]