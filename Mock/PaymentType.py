from Abstract.MockObject import MockObject


class PaymentTypeMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.payment_type
        ("campaign_list", "org_id")
        VALUES('1,2,3,4,5,6,7,8,9', '1');

        INSERT INTO public.payment_type
        ("campaign_list", "org_id")
        VALUES('1,5', '1');
        '''
        return response