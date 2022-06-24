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

    def getFeaturesStr(self):
        if(self.features is not None):
            return  str(",".join(str(x) for x in self.features))
        return ""

    def __str__(self):
        return self.id + "\t" + self.name + "\t" + self.barcode + "\t[" + self.getFeaturesStr() + "]\t" + str(self.qty) + "\t" + str(self.amount)