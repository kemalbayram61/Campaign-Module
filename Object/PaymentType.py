class PaymentType:
    id: str
    campaign_list: list[str]

    def __init__(self, id: str = None,
                 campaign_list: list[str] = None):
        self.id = id
        self.campaign_list = [] if campaign_list == None else campaign_list

    def __str__(self) -> str:
        response: str = '''
            {id:{0},
            campaign_list:{1}}
        '''.format(self.id, ','.join(self.campaign_list))
        return response
