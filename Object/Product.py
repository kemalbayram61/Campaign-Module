class Product:
    id: str
    name: str
    barcode: str
    qty: int
    unitPrice: float
    property: dict
    criteriaCampaignList: list[str]
    actionCampaignList: list[str]

    def __init__(self, id: str = None,
                 name: str = None,
                 barcode: str = None,
                 qty: int = None,
                 unitPrice: float = None,
                 property: dict = None,
                 criteriaCampaignList: list[str] = None,
                 actionCampaignList: list[str] = None):
        self.id = id
        self.name = name
        self.barcode = barcode
        self.qty = qty
        self.unitPrice = unitPrice
        self.property = {} if property == None else property
        self.criteriaCampaignList = [] if criteriaCampaignList == None else criteriaCampaignList
        self.actionCampaignList = [] if actionCampaignList == None else actionCampaignList