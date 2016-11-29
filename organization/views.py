from django.shortcuts import render
from django.http import HttpResponse
from models import Organization
from geopy.geocoders import Nominatim

geolocator = Nominatim()

def index(request):
    organizations = Organization.objects.all()
    return render(request, 'organization/home.html', {'organizations': organizations})

def organization_page(request, name):
    organization = Organization.objects.filter(name = name)
    address = organization[0].address
    print address
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    print latitude, longitude
    return render(request, 'organization/organization.html', {'organization': organization[0], 'latitude': latitude, 'longitude': longitude})
