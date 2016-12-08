"""Tests the organization app"""
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from Enrich.models import Reviews
from .models import Organization
from .views import organization_page, submit_form, index

# Create your tests here.

class OrganizationTestCase(TestCase):
    """Organization Test Case"""
    def setUp(self):
        """Sets up test db"""
        self.c = Client()
        self.rf = RequestFactory()
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

        self.org1 = Organization.objects.create(organization_id=2,
                                                name="ace",
                                                description="after school",
                                                free=False,
                                                tuition=1000,
                                                rating=2,
                                                category="a",
                                                address="55 main street",
                                                contact_number="1111",
                                                website="www.ace.edu",
                                                imageURL="a")

    def test_attributes_of_organization_model(self):
        self.assertEquals(self.org1.organization_id, 2)
        self.assertEquals(self.org1.name, "ace")
        self.assertEquals(self.org1.description, "after school")
        self.assertEquals(self.org1.free, False)
        self.assertEquals(self.org1.tuition, 1000)
        self.assertEquals(self.org1.rating, 2)
        self.assertEquals(self.org1.category, "a")
        self.assertEquals(self.org1.address, "55 main street")
        self.assertEquals(self.org1.contact_number, "1111")
        self.assertEquals(self.org1.website, "www.ace.edu")
        self.assertEquals(self.org1.imageURL, "a")

    def test_entering_the_db(self):
        """Tests if I entered into the database"""
        entry = Organization.objects.get(organization_id=1)

        self.assertTrue(entry.name == "a")
        self.assertEqual(str(entry), "1, a, blah, False, 1000, 2.0, a, 123 Elm St")

    def test_removing_from_db(self):
        """Tests if I can add and remove to/from db"""

        Organization.objects.create(organization_id="10",
                                    name="b",
                                    category="a",
                                    description="blah",
                                    free=False,
                                    tuition=1000,
                                    rating=2,
                                    address="123 Elm St",
                                    contact_number="1111",
                                    website="www.enrich.edu",
                                    imageURL="a")

        entry = Organization.objects.get(organization_id=10)
        self.assertTrue(entry)
        self.assertEqual(entry.get_absolute_url(), "/organization/b/")
        entry.delete()
        entry = Organization.objects.all()
        self.assertEqual(len(entry), 2)
    def test_index(self):
        """tests the index"""
        req = self.rf.get("/")
        res = index(req)
        self.assertTrue(res.status_code, 200)
    def test_organization_page(self):
        """Tests the organization page"""
        response = self.c.get("/a /")
        self.assertTrue(response.status_code, 200)

    def test_submit_form(self):
        """Tests the submit form"""
        response = self.c.get("/submit_form")
        self.assertTrue(response.status_code, 302)

    def test_organization_page_functions(self):
        """Tests the organization page"""
        req = self.rf.get("/organization/a")
        name = "a"
        response = organization_page(req, name)
        self.assertEqual(response.status_code, 200)

        #looking for some known features of our org pages
        self.assertTrue("blah" in str(response.content))
        self.assertTrue("Reviews" in str(response.content))
    def test_absolute_url(self):
        """Verifies that the absolute URL function works"""
        self.assertEqual("/organization/%s/" % self.org1.name, self.org1.get_absolute_url())

    def test_a_submission(self):
        """Submits a review"""
        #first, create a user
        User.objects.create_user(
            username="test",
            first_name="Testy",
            last_name="McTestface",
            email="test@test.test",
            password="test")
        self.assertTrue(User.objects.all().exists())

        testy = User.objects.get(username="test")
        self.assertEqual(testy.username, "test")
        self.assertEqual(testy.pk, 1)
        self.c.post("/login/login_user/", {"username": "test", "password": "test"})
        response = self.c.post("/organization/submit_form/", {'organization_id': 1, "rating": 5,\
                                "review_text": 5})
        self.assertTrue(response.status_code, 302)
        reviewList = Reviews.objects.all()
        self.assertTrue(reviewList.exists())
        req = self.rf.get("/organization/a/")
        response = organization_page(req, "a")

    def test_submit_redirect(self):
        response = self.c.post("/organization/submit_form", {'organization_id': 1, "rating": 5,\
                                "review_text": 5}, follow=True)

        m = list(response.context['messages'])

        self.assertEqual(len(m), 1)
