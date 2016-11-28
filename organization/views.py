from django.shortcuts import render
from django.http import HttpResponse
from models import Organization

def index(request):
    organizations = Organization.objects.all()
    return render(request, 'organization/home.html', {'organizations': organizations})

def organization_page(request, o_name):
    organization = Organization.objects.filter(name=o_name)
    return render(request, 'organization/', {'organization': organization})
