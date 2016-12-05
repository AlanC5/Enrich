'''
Rendering the appropriate views
'''
from django.shortcuts import render
from django.http import HttpResponseRedirect

from organization.models import Organization
from user.models import EnrichUser
from .forms import SearchForm, FilterSearchForm

def index(request):
    '''
    Search Form and Get Responses
    '''
    form = SearchForm()
    filterform = FilterSearchForm()
    user = request.user
    print(user)
    return render(request, 'search/search.html', {'form' : form, 'filterForm' : filterform})
    #if not request.user.is_authenticated():
    #    return render(request, 'search/search.html', {'form' : form, 'filterForm' : filterform})
    #else:
    #    print("user is logged in")
    #    user = EnrichUser.objects.filter(user=request.user)
    #    return render(request, 'search/search.html', {'form' : form, 'filterForm' : filterform})

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
            # starRange and negativeStarRange to render stars
            for result in results:
                rating = result.rating
                result.starRange = range(int(rating))
                result.negativeStarRange = range(5 - int(rating))

            return render(request, 'search/search_results.html', {'search_term': query, 'results':results})
    # else render the form
    else:
        return HttpResponseRedirect('/search/')
