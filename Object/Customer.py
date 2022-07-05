class Customer:
    id: str
    name: str
    property: dict

    def __init__(self, id:str = None,
                 name: str = None,
                 property: dict = None):
        self.id = id
        self.name = name
        self.property = {} if property == None else property