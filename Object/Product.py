class Product:
    id: str
    barcode: str
    qty: int
    unit_price: float
    amount: float
    criteria_campaign_list: list[str]
    action_campaign_list: list[str]
    is_used: bool
    discount_amount: float
    line_amount: float
    discount_lines: list[dict]

    def __init__(self, id: str = None,
                 barcode: str = None,
                 qty: int = None,
                 unit_price: float = None,
                 amount: float = None,
                 is_used: bool = None,
                 criteria_campaign_list: list[str] = None,
                 action_campaign_list: list[str] = None,
                 discount_amount: float = None,
                 line_amount: float = None,
                 discount_lines: list[dict] = None):
        self.id = id
        self.barcode = barcode
        self.qty = qty
        self.unit_price = unit_price
        self.amount = amount
        self.is_used = False if is_used is None else is_used
        self.criteria_campaign_list = [] if criteria_campaign_list is None else criteria_campaign_list
        self.action_campaign_list = [] if action_campaign_list is None else action_campaign_list
        self.discount_amount = discount_amount
        self.line_amount = line_amount
        self.discount_lines = [] if discount_lines is None else discount_lines

    #todo update
    def __str__(self) -> str:
        response: str = '''
            id:{0},
            barcode:{1},
            qty:{2},
            unit_price:{3},
            amount:{4},
            is_used:{5},
            criteria_campaign_list:{6},
            action_campaign_list:{7},
            discount_amount:{8},
            line_amount:{9},
            discount_lines:{10},
        '''.format(self.id,
                   self.barcode,
                   self.qty,
                   self.unit_price,
                   self.amount,
                   self.is_used,
                   ','.join(self.criteria_campaign_list),
                   ','.join(self.action_campaign_list),
                   self.discount_amount,
                   self.line_amount,
                   self.discount_lines)
        return response