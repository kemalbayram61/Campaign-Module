from Abstract.MockObject import MockObject


class PaymentTypeMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.payment_type
        ("campaign_list")
        VALUES('1,2,3,4,5,6,7,8,9');

        INSERT INTO public.payment_type
        ("campaign_list")
        VALUES('1,5');
        '''
        return response