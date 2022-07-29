class Customer:
    id: str
    campaign_list: list[str]

    def __init__(self, id: str = None,
                 campaign_list: list[str] = None):
        self.id = id
        self.campaign_list = [] if campaign_list is None else campaign_list
