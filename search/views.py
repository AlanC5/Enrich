'''
Rendering the appropriate views
'''
from django.shortcuts import render
from django.http import HttpResponseRedirect

from organization.models import Organization
from .forms import SearchForm

def index(request):
    '''
    Search Form and Get Responses
    '''
    form = SearchForm()
    return render(request, 'search/search.html', {'form' : form})

def search_result(request):
    '''
    Display search results
    '''
    # Check if POST request
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            # process data and render search results
            query = form.cleaned_data['search_term']
            results = Organization.objects.filter(description__contains=query)
            print(results)
            return render(request, 'search/search_results.html', {'search_term': query, 'results':results})
    # else render the form
    else:
        return HttpResponseRedirect('/search/')
