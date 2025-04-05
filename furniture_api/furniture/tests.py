from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

class URLTests(TestCase):
    def test_home(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
