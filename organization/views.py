"""Organization views"""

from django.shortcuts import render
from django.http import HttpResponse
import googlemaps
from Enrich.models import Reviews
from .models import Organization


GMAPS = googlemaps.Client(key='AIzaSyDaRcVBVfVT8bTlZ5DUCir9qlT_EVYyWIM')

def index(request):
    """Organization index"""
    organizations = Organization.objects.all()
    return render(request, 'organization/home.html', {'organizations': organizations})

def organization_page(request, name):
    """Page for an organization"""

    organization = Organization.objects.filter(name=name)
    address = organization[0].address

    geocode_result = GMAPS.geocode(address)
    latlong = (geocode_result[0].get('geometry')).get('location')
    print(latlong)

    lat = latlong['lat']
    lon = latlong['lng']
    return render(request, 'organization/organization.html',
                  {'organization': organization[0], 'latitude': lat, 'longitude': lon})

def submit_form(request):
    user_id = request.POST["user_id"]
    organization_id = request.POST["organization_id"]
    rating = request.POST["rating"]
    review_text = request.POST["review_text"]

    Reviews.objects.create(review_text = review_text,
                            rating=rating,
                            date=datetime.now(),
                            user_id=User.objects.get(pk=user_id),
                            organization_id=Organization.objects.get(pk=organization_id))

    return redirect('organization/' + str(organization_id))

