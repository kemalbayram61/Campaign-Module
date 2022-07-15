from Abstract.MockObject import MockObject


class ProductMock(MockObject):
    def get_mock_sql(self) -> str:
        response = '''
        INSERT INTO public.product
        ("name", "barcode", "property", "criteria", "action", "amount")
        VALUES('Tükenmez Kalem', '283746328746123', '{"Kategori":"Kırtasiye", "Alt Kategori": "Kalem"}', '1,5', NULL, 50);
        
        INSERT INTO public.product
        ("name", "barcode", "property", "criteria", "action", "amount")
        VALUES('Resim Defteri', '283746328746124', '{"Kategori":"Kırtasiye", "Alt Kategori": "Defter"}', '1,8', '1,2', 25);
        
        INSERT INTO public.product
        ("name", "barcode", "property", "criteria", "action", "amount")
        VALUES('Silgi', '283746328746124', '{"Kategori":"Kırtasiye", "Alt Kategori": "Silgi"}', '3,8', NULL, 10);
        '''
        return response
