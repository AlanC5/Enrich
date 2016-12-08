"""user tests"""

from django.test import TestCase, Client
from .models import EnrichUser

class UserTestCase(TestCase):
   """User Test Case"""
    def setUp(self):
        """Sets up test db"""
        self.c = Client()
        User.objects.create(user="name")

#         self.user1 = Organization.objects.create(user="tony")
#
#     def test_attributes_of_user_model(self):
#         self.assertEquals(self.user1.user, "tony")
