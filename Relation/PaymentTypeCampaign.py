class PaymentTypeCampaign:
    paymentTypeID: str
    campaignList: list[str]

    def __init__(self, paymentTypeID: str = None,
                 campaignList: list[str] = None):
        self.campaignList = [] if campaignList == None else campaignList
        self.paymentTypeID = paymentTypeID