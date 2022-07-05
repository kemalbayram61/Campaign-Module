from Abstract.AllCustomer import AllCustomer
from Abstract.AllPaymentType import AllPaymentType
from Abstract.AllPaymentChannel import AllPaymentChannel
from Abstract.AllProductCriteria import AllProductCriteria
from Abstract.AllProductAction import AllProductAction
from Abstract.ActionType import ActionType

class Campaign:
    id: str
    allPaymentChannel: AllPaymentChannel
    allCustomer: AllCustomer
    allPaymentType: AllPaymentType
    allProductCriteria: AllProductCriteria
    allProductAction: AllProductAction
    level: int
    minQty: int
    minAmount: float
    maxDiscount: float
    maxOccurrence: int
    actionType: ActionType
    actionAmount: float
    actionQty: int
    startDate: str
    endDate: str
    isActive: bool

    def __init__(self, id: str = None,
                    allPaymentChannel: AllPaymentChannel = None,
                    allCustomer: AllCustomer = None,
                    allPaymentType: AllPaymentType = None,
                    allProductCriteria: AllProductCriteria = None,
                    allProductAction: AllProductAction = None,
                    level: int = None,
                    minQty: int = None,
                    minAmount: float = None,
                    maxDiscount: float = None,
                    maxOccurrence: int = None,
                    actionType: ActionType = None,
                    actionAmount: float = None,
                    actionQty: int = None,
                    startDate: str = None,
                    endDate: str = None,
                    isActive: bool = None):
        self.id = id
        self.allPaymentChannel = allPaymentChannel
        self.allCustomer = allCustomer
        self.allPaymentType = allPaymentType
        self.allProductAction = allProductAction
        self.allProductCriteria = allProductCriteria
        self.level = level
        self.minQty = minQty
        self.minAmount = minAmount
        self.maxDiscount = maxDiscount
        self.maxOccurrence = maxOccurrence
        self.actionType = actionType
        self.actionAmount = actionAmount
        self.actionQty = actionQty
        self.startDate = startDate
        self.endDate = endDate
        self.isActive = isActive