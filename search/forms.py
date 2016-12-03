'''
Search form input
'''
from django import forms

class SearchForm(forms.Form):
    '''
    Defining the input fields for Search Navbar
    Defined Here, but not templated for HTML and Stlying Reasons
    '''
    search_term = forms.CharField(label="", max_length=100)


class FilterSearchForm(forms.Form):
    '''
    Defining the input fields for Filter Search
    Defined Here, but not templated for HTML and Stlying Reasons
    '''
    CATEGORYCHOICES = [
        ('STEM', 'STEM'),
        ('Arts/Humanities', 'Arts/Humanities'),
        ('Academic Prep', 'Academic Prep'),
        ('Sports', 'Sports')]
    PRICECHOICES = [
        ('TUITION', 'TUITION')]

    search_term = forms.CharField(label="", max_length=100)
    category = forms.MultipleChoiceField(choices=CATEGORYCHOICES, widget=forms.CheckboxSelectMultiple())
    price = forms.ChoiceField(choices=PRICECHOICES, widget=forms.RadioSelect())
