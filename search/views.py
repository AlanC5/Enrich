'''
Rendering the appropriate views
'''
from django.shortcuts import render
from django.http import HttpResponseRedirect

from organization.models import Organization
from .forms import SearchForm, FilterSearchForm
from django.db.models import Q


def index(request):
    '''
    Search Form and Get Responses
    '''
    form = SearchForm()
    filterform = FilterSearchForm()
    return render(request, 'search/search.html', {'form' : form, 'filterForm' : filterform})

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

            # get the categoryChoices the user selected
            categoryChoices = form.cleaned_data.get('category')

            # Create complex query with Q objects from category choices that the user selected
            # Utilize complex lookups with Q objects
            #https://docs.djangoproject.com/en/dev/topics/db/queries/#complex-lookups-with-q-objects
            categorySelected = '('
            for choice in categoryChoices:
                categorySelected += ' Q(category=' + "\'" + choice + "\'" + ') |'
            categorySelected = categorySelected[:-1]
            categorySelected += ')'

            results = Organization.objects.filter(Q(description__contains=query) & eval(categorySelected))

            # starRange and negativeStarRange to render stars
            for result in results:
                rating = result.rating
                result.starRange = range(int(rating))
                result.negativeStarRange = range(5 - int(rating))

            return render(request, 'search/search_results.html', {'search_term': query, 'results':results})
    # else render the form
    else:
        return HttpResponseRedirect('/search/')
