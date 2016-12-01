"""Views for the login"""

from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    """Main login page"""
    return render(request, "login/loginpage.html")
