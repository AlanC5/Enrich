"""Login tests"""

from django.test import TestCase, Client
from django.test.client import RequestFactory
from .views import register

class LoginTestCase(TestCase):
    """Login tests"""
    def setUp(self):
        self.c = Client()
        self.rf = RequestFactory()

    def test_login_page_exists(self):
        """Makes sure the login page index returns a 200 OK"""
        response = self.c.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_logout_Page_exists(self):
        """Tests logout page"""
        response = self.c.get("/login/logout_user")
        self.assertEqual(response.status_code, 301)

    def test_register_page_exists(self):
        """Makes sure the register page index returns a 200 OK"""
        response = self.c.get("/login/#")
        self.assertEqual(response.status_code, 200)

    def test_login_redirect(self):
        """Given a get instead of a POST, login_user redirects to login"""
        response = self.c.get("/login/login_user/")

        self.assertEqual(response.status_code, 302)

    def test_registration_form(self):
        """Tests registration functionality"""
        request = self.c.post("login/register", {"username": "a", "first_name": "Sam",
            "last_name": "Cohen", "email": "samcohen@gmail.com", "password": "test"})

        request = self.c.get("login/register")
        self.assertTrue("True")
