class BasketLine:
    barcode: str
    qty: int
    unit_price: float
    amount: float
    is_used: bool
    discount_amount: float
    line_amount: float
    discount_lines: list[dict]

    def __init__(self, barcode: str = None,
                 qty: int = None,
                 unit_price: float = None,
                 amount: float = None,
                 is_used: bool = None,
                 discount_amount: float = None,
                 line_amount: float = None,
                 discount_lines: list[dict] = None):
        self.id = id
        self.barcode = barcode
        self.qty = qty
        self.unit_price = unit_price
        self.amount = amount
        self.is_used = False if is_used is None else is_used
        self.discount_amount = discount_amount
        self.line_amount = line_amount
        self.discount_lines = [] if discount_lines is None else discount_lines