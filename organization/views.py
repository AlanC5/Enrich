from django.shortcuts import render
from django.http import HttpResponse
from models import Organization
import googlemaps


gmaps = googlemaps.Client(key='AIzaSyDaRcVBVfVT8bTlZ5DUCir9qlT_EVYyWIM')

def index(request):
    organizations = Organization.objects.all()
    return render(request, 'organization/home.html', {'organizations': organizations})

def organization_page(request, name):
    organization = Organization.objects.filter(name = name)
    address = organization[0].address

    geocode_result = gmaps.geocode(address)
    latlong= geocode_result[0].itervalues().next()['location']

    print latlong
    lat = latlong['lat']
    lon = latlong['lng']
    return render(request, 'organization/organization.html', {'organization': organization[0], 'latitude': lat, 'longitude': lon})
