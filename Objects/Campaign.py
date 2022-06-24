from Abstracts.ActionTypes import ActionTypes
from Objects.Criteria import Criteria
class Campaign:
    id: str
    name: str
    productCriteria: list[Criteria]
    actionCriteria: list[Criteria]
    actionType: ActionTypes
    actionAmount: float
    actionQty: int
    maxDiscount: float

    def __init__(self, id:str = None,
                 name: str = None,
                 productCriteria: list[Criteria] = None,
                 actionCriteria: list[Criteria] = None,
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