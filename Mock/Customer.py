from Abstract.MockObject import MockObject


class CustomerMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.customer
        ("campaign_list")
        VALUES('1,2,3,4,5');

        INSERT INTO public.customer
        ("campaign_list")
        VALUES('1,2,3,4,5,6,7,8,9,10');

        INSERT INTO public.customer
        ("campaign_list")
        VALUES('1,5,6,7,8,9,10,11,12');
        '''
        return response
