class PaymentChannel:
    id: str
    name: dict # {"TR": "Türkçe tanım", "EN": "English Definition"}
    campaignList: list[str]

    def __init__(self, id: str = None,
                 name: dict = None,
                 campaignList: list[str] = None):
        self.id = id
        self.name = {} if name == None else name
        self.campaignList = [] if campaignList == None else campaignList