from Objects.Criteria import Criteria
class BaskedItem:
    id: str
    name: str
    barcode: str
    features: list[Criteria]
    qty: int
    amount: float

    def __init__(self, id:str = None,
                 name: str = None,
                 barcode: str = None,
                 features: list[Criteria] = None,
                 qty: int = None,
                 amount: float = None):
        self.id = id
        self.name = name
        self.barcode = barcode
        self.features = features
        self.qty = qty
        self.amount = amount