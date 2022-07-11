class PaymentType:
    id: str
    name: dict # {"TR": "Türkçe tanım", "EN": "English Definition"}
    campaign_list: list[str]

    def __init__(self, id: str = None,
                 name: dict = None,
                 campaign_list: list[str] = None):
        self.id = id
        self.name = {} if name == None else name
        self.campaign_list = [] if campaign_list == None else campaign_list