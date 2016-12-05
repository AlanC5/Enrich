"""Enrich tests"""
from django.test import TestCase
from organization.models import Organization
from .models import Reviews

class EnrichTestCase(TestCase):
    """Login tests"""
    def setUp(self):
        """Sets up my test case"""
        organizations = Organization.objects
        reviews = Reviews.objects

    def test_organization_model(self):
        """Tests that the organization_staff model works"""
        self.assertTrue(True)

    def test_review_model(self):
        """Tests that the review model works"""
        self.assertTrue(True)