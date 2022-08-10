from Abstract.MockObject import MockObject


class ProductMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.product
        ("barcode", "criteria_campaign_list", "action_campaign_list")
        VALUES('283746328746432', '1,2', '1');
        
        INSERT INTO public.product
        ("barcode", "criteria_campaign_list", "action_campaign_list")
        VALUES('283746328746936', '1,2', '1,2');
        
        INSERT INTO public.product
        ("barcode", "criteria_campaign_list", "action_campaign_list")
        VALUES('283746328746124', '7,8', '9,12');
        
        INSERT INTO public.product
        ("barcode", "criteria_campaign_list", "action_campaign_list")
        VALUES('283746328746125', '3,8', NULL);
        
        INSERT INTO public.product
        ("barcode", "criteria_campaign_list", "action_campaign_list")
        VALUES('283746328746126', '3,8', NULL);
        
        INSERT INTO public.product
        ("barcode", "criteria_campaign_list", "action_campaign_list")
        VALUES('283746328746127', '3,8', NULL);
        
        INSERT INTO public.product
        ("barcode", "criteria_campaign_list", "action_campaign_list")
        VALUES('283746328746128', '3,8', NULL);
        
        INSERT INTO public.product
        ("barcode", "criteria_campaign_list", "action_campaign_list")
        VALUES('283746328746129', '3,8', NULL);
        
        INSERT INTO public.product
        ("barcode", "criteria_campaign_list", "action_campaign_list")
        VALUES('283746328746130', '3,8', NULL);
        '''
        return response
