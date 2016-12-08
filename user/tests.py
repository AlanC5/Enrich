"""user tests"""

from django.test import TestCase, Client
from .models import EnrichUser

class UserTestCase(TestCase):
    """User Test Case"""
    def setUp(self):
        """Sets up test db"""
        self.c = Client()
