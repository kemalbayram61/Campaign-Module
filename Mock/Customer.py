class CustomerMock:
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.customer
        ("name", "property", "campaign_list")
        VALUES('Kemal Bayram', '{"Müşteri Tipi":"1"}', 'c1,c2,c3,c4,c5');

        INSERT INTO public.customer
        ("name", "property", "campaign_list")
        VALUES('Emrah Kabacaoğlu', '{"Müşteri Tipi":"1"}', 'c1,c2,c3,c4,c5,c6,c7,c8,c9,c10');

        INSERT INTO public.customer
        ("name", "property", "campaign_list")
        VALUES('Hasan Akay', '{"Müşteri Tipi":"1"}', 'c1,c5,c6,c7,c8,c9,c10,c11,c12');
        '''
        return response