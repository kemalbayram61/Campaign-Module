from Abstract.MockObject import MockObject


class ProductMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.product
        ("name", "barcode", "property", "criteria", "action", "amount")
        VALUES('Coca Cola', '283746328746432', '{"Kategori":"İçececek", "Alt Kategori": "Asitli İçecek"}', '1,2', '1', 9.90);
        
        INSERT INTO public.product
        ("name", "barcode", "property", "criteria", "action", "amount")
        VALUES('Ice Tea', '283746328746936', '{"Kategori":"İçececek", "Alt Kategori": "Asisiz İçecek"}', '1,2', '1,2', 12.50);
        
        INSERT INTO public.product
        ("name", "barcode", "property", "criteria", "action", "amount")
        VALUES('Resim Defteri', '283746328746124', '{"Kategori":"Kırtasiye", "Alt Kategori": "Defter"}', '1,8', '1,2', 25);
        
        INSERT INTO public.product
        ("name", "barcode", "property", "criteria", "action", "amount")
        VALUES('Silgi', '283746328746124', '{"Kategori":"Kırtasiye", "Alt Kategori": "Silgi"}', '3,8', NULL, 10);
        '''
        return response
