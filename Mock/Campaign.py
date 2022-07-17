from Abstract.MockObject import MockObject


class CampaignMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.campaign
        ("name", "level", "start_date", "end_date", "min_qty", "min_amount", "max_occurrence", "action_type", "action_amount", "action_qty", "max_discount", "is_active")
        VALUES('3 adet içecek siparişinize 1 tanesi bizden hediye', 1, '20220715', '20230715', 3, 0, 0, 1, 1, 0, 1, 1);

        INSERT INTO public.campaign
        ("name", "level", "start_date", "end_date", "min_qty", "min_amount", "max_occurrence", "action_type", "action_amount", "action_qty", "max_discount", "is_active")
        VALUES('Test Kampanya 2', 1, '20220715', '20230715', 1, 400, 1, 0, 20, 0, 0, 0);

        INSERT INTO public.campaign
        ("name", "level", "start_date", "end_date", "min_qty", "min_amount", "max_occurrence", "action_type", "action_amount", "action_qty", "max_discount", "is_active")
        VALUES('Test Kampanya 3', 1, '20220715', '20230715', 1, 400, 1, 0, 20, 0, 0, 0);
        '''
        return response