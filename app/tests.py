from django.test import TestCase
from app.functions import generate_url
from app.functions import generate_string
from app.functions import generate_qr_code


class TestFunctions(TestCase):

    def test_generate_url(self):
        domain = "127.0.0.1:8000"
        long_url = "https://yandex.ru"
        new_url, img = generate_url(domain, long_url)
        self.assertTrue(len(new_url) > 0)
        self.assertTrue(len(img) > 0)
        new_url_2, img_2 = generate_url(domain, long_url)
        self.assertEqual(new_url, new_url_2)
        self.assertEqual(img, img_2)

    def test_generate_string(self):
        self.assertEqual(generate_string(1), '1')
        self.assertEqual(generate_string(11), 'a')
        self.assertEqual(generate_string(123456), '77d')

    def test_generate_qr_code(self):
        img = generate_qr_code("http://127.0.0.1:8000/123", "123")
        self.assertEqual(img, 'media/123.png')
        img = generate_qr_code("http://127.0.0.1:8000/77d", "77d")
        self.assertEqual(img, 'media/77d.png')
