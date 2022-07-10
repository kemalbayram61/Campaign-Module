class ProductMock:
    def get_mock_sql(self) ->str:
        response = '''
        INSERT INTO public.product
        ("name", "barcode", "property", "criteria", "action", "amount")
        VALUES('Tükenmez Kalem', '283746328746123', '{"Kategori":"Kırtasiye", "Alt Kategori": "Kalem"}', 'c1,c5', NULL, 50);
        
        INSERT INTO public.product
        ("name", "barcode", "property", "criteria", "action", "amount")
        VALUES('Resim Defteri', '283746328746124', '{"Kategori":"Kırtasiye", "Alt Kategori": "Defter"}', 'c1,c8', 'c1,c2', 25);
        
        INSERT INTO public.product
        ("name", "barcode", "property", "criteria", "action", "amount")
        VALUES('Silgi', '283746328746124', '{"Kategori":"Kırtasiye", "Alt Kategori": "Silgi"}', 'c3,c8', NULL, 10);
        '''
        return response