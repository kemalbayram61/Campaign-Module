from Abstract.MockObject import MockObject


class CampaignMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        
        /*f1()*/
        INSERT INTO public.campaign
        ("level", "start_date", "end_date", "min_qty", "min_amount", "max_occurrence", "action_type", "action_amount", "action_qty", "max_discount", "is_active", "all_payment_channel", "all_customer", "all_payment_type", "all_product_criteria", "all_product_action", "org_id", "external_code")
        VALUES(1, '20200101', '20240101', NULL, NULL, NULL, 0, 2, NULL, 10, 1, 1, 1, 1, 1, 1, '1', '1');

        /*f2()*/        
        INSERT INTO public.campaign
        ("level", "start_date", "end_date", "min_qty", "min_amount", "max_occurrence", "action_type", "action_amount", "action_qty", "max_discount", "is_active", "all_payment_channel", "all_customer", "all_payment_type", "all_product_criteria", "all_product_action", "org_id", "external_code")
        VALUES(1, '20200101', '20240101', NULL, NULL, NULL, 0, 2, 5, NULL, 1, 1, 1, 1, 1, 1, '1', '2');

        /*f3()*/
        INSERT INTO public.campaign
        ("level", "start_date", "end_date", "min_qty", "min_amount", "max_occurrence", "action_type", "action_amount", "action_qty", "max_discount", "is_active", "all_payment_channel", "all_customer", "all_payment_type", "all_product_criteria", "all_product_action", "org_id", "external_code")
        VALUES(1, '20200101', '20240101', NULL, NULL, NULL, 0, 10, NULL, NULL, 1, 1, 1, 1, 1, 1, '1', '3');

        /*f7()*/
        INSERT INTO public.campaign
        ("level", "start_date", "end_date", "min_qty", "min_amount", "max_occurrence", "action_type", "action_amount", "action_qty", "max_discount", "is_active", "all_payment_channel", "all_customer", "all_payment_type", "all_product_criteria", "all_product_action", "org_id", "external_code")
        VALUES(1, '20200101', '20240101', NULL, NULL, NULL, 1, 1, 1, 30, 1, 1, 1, 1, 1, 1, '1', '4');

        /*f8()*/
        INSERT INTO public.campaign
        ("level", "start_date", "end_date", "min_qty", "min_amount", "max_occurrence", "action_type", "action_amount", "action_qty", "max_discount", "is_active", "all_payment_channel", "all_customer", "all_payment_type", "all_product_criteria", "all_product_action", "org_id", "external_code")
        VALUES(1, '20200101', '20240101', NULL, NULL, NULL, 1, 0.2, NULL, 30, 1, 1, 1, 1, 1, 1, '1', '5');

        /*f9()*/
        INSERT INTO public.campaign
        ("level", "start_date", "end_date", "min_qty", "min_amount", "max_occurrence", "action_type", "action_amount", "action_qty", "max_discount", "is_active", "all_payment_channel", "all_customer", "all_payment_type", "all_product_criteria", "all_product_action", "org_id", "external_code")
        VALUES(1, '20200101', '20240101', NULL, NULL, NULL, 1, 0.2, 2, NULL, 1, 1, 1, 1, 1, 1, '1', '6');

        /*f10()*/
        INSERT INTO public.campaign
        ("level", "start_date", "end_date", "min_qty", "min_amount", "max_occurrence", "action_type", "action_amount", "action_qty", "max_discount", "is_active", "all_payment_channel", "all_customer", "all_payment_type", "all_product_criteria", "all_product_action", "org_id", "external_code")
        VALUES(1, '20200101', '20240101', NULL, NULL, NULL, 1, 0.2, NULL, NULL, 1, 1, 1, 1, 1, 1, '1', '7');

        '''
        return response