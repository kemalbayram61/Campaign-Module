from Abstract.MockObject import MockObject


class PaymentChannelMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.payment_channel
        ("campaign_list")
        VALUES('1,2,3,4,5,6,7,8,9');

        INSERT INTO public.payment_channel
        ("campaign_list")
        VALUES('1,2,3,4,5,6,7,8,9,10,11');
        '''
        return response