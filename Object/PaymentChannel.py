class PaymentChannel:
    id: str
    name: dict # {"TR": "Türkçe tanım", "EN": "English Definition"}

    def __init__(self, id: str = None,
                 name: dict = None):
        self.id = id
        self.name = {} if name == None else name