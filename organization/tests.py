"""Tests the organization app"""
from django.test import TestCase, Client
from .models import Organization
from .views import organization_page, submit_form

# Create your tests here.

class OrganizationTestCase(TestCase):
    """Organization Test Case"""
    def setUp(self):
        """Sets up test db"""
        self.c = Client()
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

    def test_entering_the_db(self):
        """Tests if I entered into the database"""
        entry = Organization.objects.get(organization_id=1)

        self.assertTrue(entry.name == "a")

    def test_removing_from_db(self):
        """Tests if I can add and remove to/from db"""

        Organization.objects.create(name="b",
                                    category="a",
                                    description="blah",
                                    free=False,
                                    tuition=1000,
                                    rating=2,
                                    address="123 Elm St",
                                    contact_number="1111",
                                    website="www.enrich.edu",
                                    imageURL="a")

        entry = Organization.objects.get(organization_id=2)
        self.assertTrue(entry)

        entry.delete()
        entry = Organization.objects.all()
        self.assertTrue(len(entry) == 1)

    def test_organization_page(self):
        response = self.c.get("/a")
        self.assertTrue(response.status_code, 200)
    def test_submit_form(self):
        response = self.c.get("/submit_form")
        self.assertTrue(response.status_code, 302)


