"""Login tests"""

from django.test import TestCase
from django.test import Client

class LoginTestCase(TestCase):
    """Login tests"""
    def setUp(self):
        self.c = Client()

    def test_login_page_exists(self):
        """Makes sure the login page index returns a 200 OK"""
        response = self.c.get("/login/")
        self.assertEqual(response.status_code, 200)
    def test_logout_Page_exists(self):
        """Tests logout page"""
        response = self.c.get("/login/logout_user")
        self.assertEqual(response.status_code, 301)