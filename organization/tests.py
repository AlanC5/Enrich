from django.test import TestCase

from .models import Organization

# Create your tests here.

def OrganizationTestCase(TestCase):

    def setUp(self):
        self.rf = RequestFactory()
        Organization.objects.create( organization_id = 1,
            name = "a",
            category = "a",
            description = "blah",
            free = False,
            tuition = 1000,
            rating = 2,
            address = "123 Elm St",
            contact_number = "1111",
            website = "www.enrich.edu",
            imageURL = "a")

    def test_entering_the_db(self):

        entry = Organization.objects.get(organization_id = 1)

        self.assertTrue(entry.name == "a")

    def test_adding_and_removing_from_db(self):

        Organization.objects.create(
            name = "b",
            category = "a",
            description = "blah",
            free = False,
            tuition = 1000,
            rating = 2,
            address = "123 Elm St",
            contact_number = "1111",
            website = "www.enrich.edu",
            imageURL = "a")

        entry = Organization.objects.get(organization_id = 2)
        self.assertNotNull(entry)

        Organization.objects.remove(organization_id=2)
        entry = Organization.objects.get(organization_id=2)
        self.assertNull(entry)
