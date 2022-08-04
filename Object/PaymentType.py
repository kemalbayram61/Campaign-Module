class PaymentType:
    id: str
    campaign_list: list[str]

    def __init__(self, id: str = None,
                 campaign_list: list[str] = None):
        self.id = id
        self.campaign_list = [] if campaign_list == None else campaign_list

    def __str__(self) -> str:
        response: str = '''
            {{id:{0},
            campaign_list:{1}}}
        '''.format(self.id, "[" + ','.join(self.campaign_list) + "]")
        return response

    @staticmethod
    def dict_to_payment_type(dict_data: dict) -> object:
        response = PaymentType(id=str(dict_data["id"]),
                               campaign_list=dict_data["campaign_list"])
        return response
