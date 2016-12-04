from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.http import HttpResponse

# Create your views here.
def index(request):
    """Main login page"""
    return render(request, "login/loginpage.html")
