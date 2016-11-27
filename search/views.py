'''
Rendering the appropriate views
'''
from django.shortcuts import render

from organization.models import Organization
from .forms import SearchForm

def index(request):
    '''
    Search Form and Get Responses
    '''
    # if post request then process it
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            # process data and render search results
            query = form.cleaned_data['search_term']
            results = Organization.objects.filter(name__contains=query)
            print results

            return render(request, 'search/search_results.html')
            # redirect to search results
            # return HttpResponseRedirect('/search/search_result/')
    # else render the form
    else:
        form = SearchForm()

    return render(request, 'search/search.html', {'form' : form})
