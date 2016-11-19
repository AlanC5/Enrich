from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>HEY!</h2>")

def hey(request):
    return HttpResponse("<h2>heyyyy</h2>")

def getUser(request):
    return render(request, 'user/theUsers.html', {'users': ['greg', 'bob']})
