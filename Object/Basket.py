from Object.Product import Product

class Basket:
    id: str
    customerID: str
    productList: list[Product]
    paymentTypeID: str
    paymentChannelID: str

    def __init__(self, id:str = None,
                 customerID: str = None,
                 paymentChannelID: str = None,
                 productList: list[Product] = None,
                 paymentTypeID: str = None):
        self.id = id
        self.customerID = customerID
        self.productList = [] if productList == None else productList
        self.paymentTypeID = paymentTypeID
        self.paymentChannelID = paymentChannelID