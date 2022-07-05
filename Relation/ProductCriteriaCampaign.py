class ProductCriteriaCampaign:
    productID: str
    campaignList: list[str]

    def __init__(self, productID: str = None,
                 campaignList: list[str] = None):
        self.campaignList = [] if campaignList == None else campaignList
        self.productID = productID