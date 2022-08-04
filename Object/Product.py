class Product:
    id: str
    barcode: str
    criteria_campaign_list: list[str]
    action_campaign_list: list[str]

    def __init__(self, id: str = None,
                 barcode: str = None,
                 criteria_campaign_list: list[str] = None,
                 action_campaign_list: list[str] = None, ):
        self.id = id
        self.barcode = barcode
        self.criteria_campaign_list = [] if criteria_campaign_list is None else criteria_campaign_list
        self.action_campaign_list = [] if action_campaign_list is None else action_campaign_list

    def __str__(self) -> str:
        response: str = '''
            {{"id":"{0}",
            "barcode":"{1}",
            "criteria_campaign_list":{2},
            "action_campaign_list":{3}}}
        '''.format(self.id,
                   self.barcode,
                   "[" + ",".join(list(map(lambda campaign_id: "\"" + str(campaign_id) + "\"", self.criteria_campaign_list))) + "]",
                   "[" + ",".join(list(map(lambda campaign_id: "\"" + str(campaign_id) + "\"", self.action_campaign_list))) + "]")
        return response

    @staticmethod
    def dict_to_product(dict_data: dict) -> object:
        response = Product(id=str(dict_data["id"]),
                           barcode=str(dict_data["barcode"]),
                           criteria_campaign_list=dict_data["criteria_campaign_list"],
                           action_campaign_list=dict_data["action_campaign_list"])
        return response
