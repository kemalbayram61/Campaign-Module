from Abstracts.CriteriaTypes import CriteriaTypes
class PreparedBaskedItem:
    feature: CriteriaTypes
    featureValue = None
    qty: int
    amount: float
    baskedItemID: str

    def __init__(self,baskedItemID: str, feature: CriteriaTypes = None, featureValue = None, qty: int = None, amount: float = None):
        self.baskedItemID = baskedItemID
        self.feature = feature
        self.featureValue = featureValue
        self.qty = qty
        self.amount = amount

    def __str__(self):
        return str(self.baskedItemID) + "\t" + str(self.feature) + "\t" + str(self.featureValue) + "\t" + str(self.qty) +"\t" + str(self.amount)

