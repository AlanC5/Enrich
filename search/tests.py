'''
Tests for Search functionality
'''
from django.test import TestCase
from django.test.client import RequestFactory
from .views import *
from organization.models import Organization
# Create your tests here.

class SearchTestCase(TestCase):
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


    def test_search_page_exists(self):
        """Makes sure the search page index returns a 200 OK"""

        get_request = self.rf.get("/search/")
        response = index(get_request)
        self.assertEqual(response.status_code, 200)

    def test_search_page_title(self):
        """Tests that the search page has the correct title tag"""
        get_request = self.rf.get("/search/")
        response = index(get_request)
        self.assertTrue("<title>Search</title>" in str(response.content))


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


    def test_results_page_works(self):
        """Tests that a results page works for a given input"""

        post_request = self.rf.post("/search/search_result/", {"search_term": "a"})
        response = search_result(post_request)

        #We're looking for the right list element.
        #Our format is <li>
        self.assertTrue("<li id = \"organization_1\"" in str(response.content))