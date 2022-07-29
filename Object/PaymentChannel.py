class PaymentChannel:
    id: str
    campaign_list: list[str]

    def __init__(self, id: str = None,
                 campaign_list: list[str] = None):
        self.id = id
        self.campaign_list = [] if campaign_list == None else campaign_list