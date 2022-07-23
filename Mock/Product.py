from Abstract.MockObject import MockObject


class ProductMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.product
        ("name", "barcode", "criteria", "action")
        VALUES('Coca Cola', '283746328746432', '1,2', '1');
        
        INSERT INTO public.product
        ("name", "barcode", "criteria", "action")
        VALUES('Ice Tea', '283746328746936', '1,2', '1,2');
        
        INSERT INTO public.product
        ("name", "barcode", "criteria", "action")
        VALUES('Resim Defteri', '283746328746124', '7,8', '9,12');
        
        INSERT INTO public.product
        ("name", "barcode", "criteria", "action")
        VALUES('Silgi', '283746328746124', '3,8', NULL);
        '''
        return response
