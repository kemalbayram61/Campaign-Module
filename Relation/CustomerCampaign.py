class CustomerCampaign:
    customerID: str
    campaignList: list[str]

    def __init__(self, customerID: str = None,
                 campaignList: list[str] = None):
        self.campaignList = [] if campaignList == None else campaignList
        self.customerID = customerID