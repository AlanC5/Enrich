'''
Rendering the appropriate views
'''
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SearchForm

def index(request):
    '''
    Rendering index example
    '''
    return render(request, 'search/search_results.html')

def get_search(request):
    '''
    Search Form and Get Responses
    '''
    # if post request then process it
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            # process data
            # redirect to search results
            return HttpResponseRedirect('/search/')
    # else render the form
    else:
        form = SearchForm()

    return render(request, 'search/search.html', {'form' : form})
