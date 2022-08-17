class Customer:
    id: str
    campaign_list: list[str]
    org_id: str

    def __init__(self, id: str = None,
                 campaign_list: list[str] = None,
                 org_id: str = None):
        self.id = id
        self.campaign_list = [] if campaign_list is None else campaign_list
        self.org_id = org_id

    def __str__(self) -> str:
        response: str = '''
            {{"id":"{0}",
            "campaign_list":{1},
            "org_id":"{2}"}}
        '''.format(self.id,
                   "[" + ",".join(list(map(lambda campaign_id: "\"" + str(campaign_id) + "\"", self.campaign_list))) + "]",
                   self.org_id)
        return response

    @staticmethod
    def dict_to_customer(dict_data: dict) -> object:
        response = Customer(id=str(dict_data["id"]),
                            campaign_list=dict_data["campaign_list"],
                            org_id=str(dict_data["org_id"]))
        return response
