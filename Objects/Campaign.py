from Abstracts.ActionTypes import ActionTypes
class Campaign:
    id: str
    name: str
    productCriteria: list
    actionCriteria: list
    actionType: ActionTypes
    actionAmount: float
    actionQty: int
    maxDiscount: float

    def __init__(self, id:str = None,
                 name: str = None,
                 productCriteria: list = None,
                 actionCriteria: list = None,
                 actionType: ActionTypes = None,
                 actionAmount: float = None,
                 actionQty: int = None,
                 maxDiscount: float = None):
        self.id = id
        self.name = name
        self.productCriteria = productCriteria
        self.actionCriteria = actionCriteria
        self.actionType = actionType
        self.actionAmount = actionAmount
        self.actionQty = actionQty
        self.maxDiscount = maxDiscount