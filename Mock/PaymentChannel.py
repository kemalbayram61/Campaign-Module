from Abstract.MockObject import MockObject


class PaymentChannelMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.payment_channel
        ("name", "campaign_list")
        VALUES('{"TR":"Online"}', 'c1,c2,c3,c4,c5,c6,c7,c8,c9');

        INSERT INTO public.payment_channel
        ("name", "campaign_list")
        VALUES('{"TR":"Mağazadan"}', 'c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11');
        '''
        return response