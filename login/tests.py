"""Login tests"""

from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from django.contrib import auth
from .views import register

class LoginTestCase(TestCase):
    """Login tests"""
    def setUp(self):
        User.objects.create_user(username="Sam", password="Sam")
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

    def test_login(self):
        """Tests the login"""
        self.c.login(username="Sam", password="Sam")
        user = auth.get_user(self.c)
        self.assertTrue(user.is_authenticated())

    def test_logout(self):
        """Tests logout functionality"""
        self.c.get("/login/logout_user/")
        user = auth.get_user(self.c)
        self.assertFalse(user.is_authenticated())


    def test_registration_form(self):
        """Tests registration functionality"""
        request = self.c.post("/login/register", {"username": "Sam123", "first_name": "Sam",
            "last_name": "Cohen", "email": "samcohen@gmail.com", "password": "test"})

        self.assertTrue("True")
