"""Acceptance tests"""
from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from organization.models import Organization
from Enrich.models import Reviews


class AcceptanceTests(TestCase):
    """Our acceptance tests"""

    def setUp(self):
        """Set up class"""
        self.c = Client()
        User.objects.create_user(username="Sam", password="Sam")
        Organization.objects.create(organization_id=1,
                                    name="a",
                                    category="a",
                                    description="blah",
                                    free=False,
                                    tuition=1000,
                                    rating=2,
                                    address="123 Elm St",
                                    contact_number="1111",
                                    website="www.enrich.edu",
                                    imageURL="a")
    def tearDown(self):
        User.objects.all().delete()
        Organization.objects.all().delete()
        Reviews.objects.all().delete()

    def test_look_for_free_programs(self):
        """As a user, I want to be able to search programs by their price
        so that users who have money constraints can identify programs that they can afford."""

        #As a user
        self.c.login(username="Sam", password="Sam")
        user = auth.get_user(self.c)
        self.assertTrue(user.is_authenticated())

        #I want to be able to search
        response = self.c.get("/search/")
        self.assertEqual(response.status_code, 200)

        #by their price
        response = self.c.post("/search/search_result/", {"price": "TUITION"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue("<li>" in str(response.content))

    def test_write_reviews(self):
        """As a user, I want to be able to write reviews for the programs so that other users 
        can benefit from my information."""

        #As a user
        self.c.login(username="Sam", password="Sam")
        user = auth.get_user(self.c)
        self.assertTrue(user.is_authenticated())

        #I want to be able to write reviews
        ##Check that program exists
        response = self.c.get("/organization/a/")
        self.assertEqual(response.status_code, 200)

        #submit review
        self.c.post("/organization/submit_form/", {"organization_id": 1, 
                    "review_text": "Great program!",
                    "rating": 5})

        #prove review is there
        rev = Reviews.objects.filter(organization_id=1, rating=5)
        self.assertTrue(rev.exists())




