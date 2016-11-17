from django.test import TestCase
from django.test.client import RequestFactory
from .views import *
# Create your tests here.

class LoginTestCase(TestCase):
    def setUp(self):
        self.rf = RequestFactory()

    def test_login_page_exists(self):
        """Makes sure the login page index returns a 200 OK"""

        get_request = self.rf.get("/login/")
        response = index(get_request)
        self.assertEqual(response.status_code, 200)


