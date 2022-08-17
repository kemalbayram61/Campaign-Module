from Abstract.MockObject import MockObject


class CustomerMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.customer
        ("campaign_list", "org_id", "external_code")
        VALUES('1,2,3,4,5', '1', '1');

        INSERT INTO public.customer
        ("campaign_list", "org_id", "external_code")
        VALUES('1,2,3,4,5,6,7,8,9,10', '1', '2');

        INSERT INTO public.customer
        ("campaign_list", "org_id", "external_code")
        VALUES('1,5,6,7,8,9,10,11,12', '1', '3');
        '''
        return response
