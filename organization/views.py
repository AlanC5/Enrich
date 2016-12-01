"""Organization views"""

from django.shortcuts import render
from django.http import HttpResponse
import googlemaps
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
