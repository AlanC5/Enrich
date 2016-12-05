"""Enrich tests"""
from django.test import TestCase
from .models import Organization
from .models import Reviews

class EnrichTestCase(TestCase):
    """Login tests"""
    def setUp(self):
        organizations = Organization.objects
        reviews = Reviews.objects

    def test_organization_model(self):
        """Makes sure the login page index returns a 200 OK"""

        get_request = self.reqs.get("/login/")
        response = index(get_request)
        self.assertEqual(response.status_code, 200)

    def test_review_model(self):
        self.assertTrue(False)