from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'organization/home.html')

def organization_page(request, o_name):
    organization = Organization.objects.filter(name=o_name)
    return render(request, 'organization/', {'organization': organization})
