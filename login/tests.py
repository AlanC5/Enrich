"""Login tests"""

from django.test import TestCase
from django.test.client import RequestFactory
from .views import index

class LoginTestCase(TestCase):
    """Login tests"""
    def setUp(self):
        self.reqs = RequestFactory()

    def test_login_page_exists(self):
        """Makes sure the login page index returns a 200 OK"""

        get_request = self.reqs.get("/login/")
        response = index(get_request)
        self.assertEqual(response.status_code, 200)