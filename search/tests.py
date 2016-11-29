'''
Tests for Search functionality
'''
from django.test import TestCase
from django.test.client import RequestFactory
from .views import *
# Create your tests here.

class SearchTestCase(TestCase):
    def setUp(self):
        self.rf = RequestFactory()

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

    def test_results_page_works(self):
        """Tests that a results page exists when given a post request"""

        post_request = self.rf.post("/search/search_result/", {"search_term": "a"})
        response = search_result(post_request)

        self.assertEqual(response.status_code, 200)
