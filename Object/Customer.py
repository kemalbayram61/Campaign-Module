class Customer:
    id: str
    name: str
    property: dict
    campaignList: list[str]

    def __init__(self, id:str = None,
                 name: str = None,
                 property: dict = None,
                 campaignList: list[str] = None):
        self.id = id
        self.name = name
        self.property = {} if property == None else property
        self.campaignList = [] if campaignList == None else campaignList