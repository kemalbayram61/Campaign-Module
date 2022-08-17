class PaymentChannel:
    id: str
    campaign_list: list[str]
    org_id: str
    external_code: str

    def __init__(self, id: str = None,
                 campaign_list: list[str] = None,
                 org_id: str = None,
                 external_code: str = None):
        self.id = id
        self.campaign_list = [] if campaign_list is None else campaign_list
        self.org_id = org_id
        self.external_code = external_code

    def __str__(self) -> str:
        response: str = '''
            {{"id":"{0}",
            "campaign_list":{1},
            "org_id":"{2}",
            "external_code": "{3}"}}
        '''.format(self.id,
                   "[" + ",".join(list(map(lambda campaign_id: "\"" + str(campaign_id) + "\"", self.campaign_list))) + "]",
                   self.org_id,
                   self.external_code)
        return response

    @staticmethod
    def dict_to_payment_channel(dict_data: dict) -> object:
        response = PaymentChannel(id=str(dict_data["id"]),
                                  campaign_list=dict_data["campaign_list"],
                                  org_id=str(dict_data["org_id"]),
                                  external_code=str(dict_data["external_code"]))
        return response
