from Object.Product import Product
from Abstract.PaymentType import PaymentType

class Basket:
    id: str
    customerID: str
    productList: list[Product]
    paymentType: PaymentType
    paymentChannelID: str

    def __init__(self, id:str = None,
                 customerID: str = None,
                 paymentChannelID: str = None,
                 productList: list[Product] = None,
                 paymentType: PaymentType = None):
        self.id = id
        self.customerID = customerID
        self.productList = [] if productList == None else productList
        self.paymentType = paymentType
        self.paymentChannelID = paymentChannelID