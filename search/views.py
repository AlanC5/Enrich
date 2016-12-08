"""Rendering the appropriate views"""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q
from organization.models import Organization
from user.models import EnrichUser
from .forms import SearchForm, FilterSearchForm

def index(request):
    """Search Form and Get Response"""
    form = SearchForm()
    filterform = FilterSearchForm()
    #user = request.user
    return render(request, 'search/search.html', {'form' : form, 'filterForm' : filterform})

def search_result(request):
    """Display search results"""
    # Check if POST request
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # get the categoryChoices the user selected
            categoryChoices = form.cleaned_data.get('category')
            priceChoice = form.cleaned_data.get('price')
            #process data and render search results
            query = form.cleaned_data['search_term']
            # Create complex query with Q objects from category choices that the user selected
            # Utilize complex lookups with Q objects
            # https://docs.djangoproject.com/en/dev/topics/db/queries/#complex-lookups-with-q-objects
            if len(categoryChoices) > 0:
                categorySelected = '('
                for choice in categoryChoices:
                    categorySelected += ' Q(category=' + "\'" + choice + "\'" + ') |'
                categorySelected = categorySelected[:-1]
                categorySelected += ')'
                if len(priceChoice) != 0: #Check if program if free
                    results = Organization.objects.filter(Q(description__contains=query, free=False) & eval(categorySelected))
                else:
                    results = Organization.objects.filter(Q(description__contains=query) & eval(categorySelected))
            else:
                if len(priceChoice) != 0: #Check if program if free
                    results = Organization.objects.filter(description__contains=query, free=False)
                else:
                    results = Organization.objects.filter(description__contains=query)

            # starRange and negativeStarRange to render stars
            for result in results:
                rating = result.rating
                result.starRange = range(int(rating))
                result.negativeStarRange = range(5 - int(rating))
            return render(request, 'search/search_results.html', {'search_term': query, 'results':results})
        else:
            results = Organization.objects.all()
            for each in results:
                rating = each.rating
                each.starRange = range(int(rating))
                each.negativeStarRange = range(5 - int(rating))
            return render(request, 'search/search_results.html', {'search_term': ' ', 'results':results})
    else:
        return HttpResponseRedirect('/search/')
