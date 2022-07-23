class Product:
    id: str
    name: str
    barcode: str
    qty: int
    unit_price: float
    amount: float
    criteria_campaign_list: list[str]
    action_campaign_list: list[str]
    is_used: bool
    discount_amount: float

    def __init__(self, id: str = None,
                 name: str = None,
                 barcode: str = None,
                 qty: int = None,
                 unit_price: float = None,
                 amount: float = None,
                 is_used: bool = None,
                 criteria_campaign_list: list[str] = None,
                 action_campaign_list: list[str] = None,
                 discount_amount: float = None):
        self.id = id
        self.name = name
        self.barcode = barcode
        self.qty = qty
        self.unit_price = unit_price
        self.amount = amount
        self.is_used = False if is_used is None else is_used
        self.criteria_campaign_list = [] if criteria_campaign_list is None else criteria_campaign_list
        self.action_campaign_list = [] if action_campaign_list is None else action_campaign_list
        self.discount_amount = discount_amount
