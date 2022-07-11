from Abstract.MockObject import MockObject


class PaymentTypeMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.payment_type
        ("name", "campaign_list")
        VALUES('{"TR":"Kapıda Ödeme"}', 'c1,c2,c3,c4,c5,c6,c7,c8,c9');

        INSERT INTO public.payment_type
        ("name", "campaign_list")
        VALUES('{"TR":"Online Ödeme"}', 'c1,c5');
        '''
        return response