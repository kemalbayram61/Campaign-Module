from Abstract.MockObject import MockObject


class CustomerMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.customer
        ("name", "property", "campaign_list")
        VALUES('Kemal Bayram', '{"Müşteri Tipi":"1"}', '1,2,3,4,5');

        INSERT INTO public.customer
        ("name", "property", "campaign_list")
        VALUES('Emrah Kabacaoğlu', '{"Müşteri Tipi":"1"}', '1,2,3,4,5,6,7,8,9,10');

        INSERT INTO public.customer
        ("name", "property", "campaign_list")
        VALUES('Hasan Akay', '{"Müşteri Tipi":"1"}', '1,5,6,7,8,9,10,11,12');
        '''
        return response
