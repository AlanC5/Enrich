'''
Tests for Search functionality
'''
from django.test import TestCase, Client
from django.test.client import RequestFactory
from organization.models import Organization

from .views import index, search_result
# Create your tests here.

class SearchTestCase(TestCase):
    """A Search functionality test class"""
    def setUp(self):
        self.c = Client()
        self.rf = RequestFactory()
        Organization.objects.create(organization_id=1,
                                    name="b",
                                    category="STEM",
                                    description="d",
                                    free=False,
                                    tuition=6000,
                                    rating=5,
                                    address="124 Elm Ave",
                                    contact_number="555-555-5555",
                                    website="www.enrich.com",
                                    imageURL="IMAGE HERE")

        Organization.objects.create(organization_id=2,
                                    name="Test",
                                    category="Art/Humanities",
                                    description="d",
                                    free=True,
                                    tuition=0,
                                    rating=5,
                                    address="124 Elm Ave",
                                    contact_number="555-555-5555",
                                    website="www.enrich.com",
                                    imageURL="IMAGE HERE")

    def test_search_page_exists(self):
        """Makes sure the search page index returns a 200 OK"""

        #get_request = self.rf.get("/search/")
        response = self.c.get("/search/")
        self.assertEqual(response.status_code, 200)


    def test_search_results_page_exists(self):
        """Makes sure the search results page redirects to search when not given a request"""

        get_request = self.rf.get("/search/search_result/")
        response = search_result(get_request)
        self.assertEqual(response.status_code, 302)

    def test_results_page_exists(self):
        """Tests that a results page exists when given a post request"""

        post_request = self.rf.post("/search/search_result/", {"search_term": "a"})
        response = search_result(post_request)

        self.assertEqual(response.status_code, 200)

    def test_filter_arguments(self):
        """Tests that our filtering functions work"""
        response = self.c.post("/search/search_result/", {"search_term": "d", "category": "STEM"})
        self.assertTrue("<li>" in str(response.content))
        self.assertEqual(response.status_code, 200)
        response = self.c.post("/search/search_result/", {"search_term": "d", "category":"STEM", "price": "TUITION"})
        self.assertTrue("<li>" in str(response.content))
        self.assertEqual(response.status_code, 200)
        response = self.c.post("/search/search_result/", {"search_term": " ", "category": "STEM", "price": "TUITION"})
        self.assertTrue("<li>" in str(response.content))
        self.assertEqual(response.status_code, 200)

    def test_results_page_works(self):
        """Tests that a results page works for a given input"""

        post_request = self.rf.post("/search/search_result/", {"search_term": "a"})
        response = search_result(post_request)

        post_request = self.rf.post("/search/search_result/", {"search_term": ""})
        response = search_result(post_request)


        #We're looking for the right list element.
        #Our format is <li>
        self.assertTrue("<li>" in str(response.content))
