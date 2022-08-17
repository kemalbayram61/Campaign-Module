from Abstract.MockObject import MockObject


class PaymentChannelMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.payment_channel
        ("campaign_list", "org_id", "external_code")
        VALUES('1,2,3,4,5,6,7,8,9', '1', '1');

        INSERT INTO public.payment_channel
        ("campaign_list", "org_id", "external_code")
        VALUES('1,2,3,4,5,6,7,8,9,10,11', '1', '2');
        '''
        return response