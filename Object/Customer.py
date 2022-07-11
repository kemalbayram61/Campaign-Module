class Customer:
    id: str
    name: str
    property: dict
    campaign_list: list[str]

    def __init__(self, id: str = None,
                 name: str = None,
                 property: dict = None,
                 campaign_list: list[str] = None):
        self.id = id
        self.name = name
        self.property = {} if property is None else property
        self.campaign_list = [] if campaign_list is None else campaign_list
