"""user tests"""

from django.test import TestCase, Client
from .models import EnrichUser

class UserTestCase(TestCase):
    """User Test Case"""
    def setUp(self):
        """Sets up test db"""
        self.c = Client()


    def test_create_Enrich_user(self):
        EnrichUser.objects.create(user = "Test")