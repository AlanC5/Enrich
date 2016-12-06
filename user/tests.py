"""user tests"""

from django.test import TestCase, Client
from .models import User

class UserTestCase(TestCase):
    """User Test Case"""
    def setUp(self):
        """Sets up test db"""
        self.c = Client()
        User.objects.create(user="name",
                            school_name="ps200")


        self.user1 = Organization.objects.create(user="tony",
                                                 school_name="ps100")

    def test_attributes_of_user_model(self):
        self.assertEquals(self.user1.user, "tony")
        self.assertEquals(self.user1.school_name, "ps100")
