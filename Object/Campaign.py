from Abstract.AllCustomer import AllCustomer
from Abstract.AllPaymentType import AllPaymentType
from Abstract.AllPaymentChannel import AllPaymentChannel
from Abstract.AllProductCriteria import AllProductCriteria
from Abstract.AllProductAction import AllProductAction
from Abstract.ActionType import ActionType


class Campaign:
    id: str
    name: str
    all_payment_channel: AllPaymentChannel
    all_customer: AllCustomer
    all_payment_type: AllPaymentType
    all_product_criteria: AllProductCriteria
    all_product_action: AllProductAction
    level: int
    min_qty: int
    min_amount: float
    max_discount: float
    max_occurrence: int
    action_type: ActionType
    action_amount: float
    action_qty: int
    start_date: str
    end_date: str
    is_active: bool

    def __init__(self, id: str = None,
                 name: str = None,
                 all_payment_channel: AllPaymentChannel = None,
                 all_customer: AllCustomer = None,
                 all_payment_type: AllPaymentType = None,
                 all_product_criteria: AllProductCriteria = None,
                 all_product_action: AllProductAction = None,
                 level: int = None,
                 min_qty: int = None,
                 min_amount: float = None,
                 max_discount: float = None,
                 max_occurrence: int = None,
                 action_type: ActionType = None,
                 action_amount: float = None,
                 action_qty: int = None,
                 start_date: str = None,
                 end_date: str = None,
                 is_active: bool = None):
        self.id = id
        self.name = name
        self.all_payment_channel = all_payment_channel
        self.all_customer = all_customer
        self.all_payment_type = all_payment_type
        self.all_product_action = all_product_action
        self.all_product_criteria = all_product_criteria
        self.level = level
        self.min_qty = min_qty
        self.min_amount = min_amount
        self.max_discount = max_discount
        self.max_occurrence = max_occurrence
        self.action_type = action_type
        self.action_amount = action_amount
        self.action_qty = action_qty
        self.start_date = start_date
        self.end_date = end_date
        self.is_active = is_active
