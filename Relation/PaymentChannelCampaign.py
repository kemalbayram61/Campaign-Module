class PaymentChannelCampaign:
    paymentChannelID: str
    campaignList: list[str]

    def __init__(self, paymentChannelID: str = None,
                 campaignList: list[str] = None):
        self.campaignList = [] if campaignList == None else campaignList
        self.paymentChannelID = paymentChannelID