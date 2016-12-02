'''
Search form input
'''
from django import forms

class SearchForm(forms.Form):
    '''
    Defining the input fields
    '''
    search_term = forms.CharField(label="", max_length=100)
