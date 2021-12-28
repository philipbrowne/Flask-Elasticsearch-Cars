from app import app
from unittest import TestCase

class CarsTestCase(TestCase):
    def setUp(self):
        self.client = app.test_client()
    def test_app(self):
        with self.client as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)