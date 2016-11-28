from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):
    all_users = User.objects.all()
    html = ''
    for user in all_users:
        url = '/user/' + str(user.user_id) + '/'
        html += '<a href="' + url + '"> ' + user.name + '</a><br>'
    return HttpResponse(html)

def hey(request):
    return HttpResponse("<h2>heyyyy</h2>")

def getUser(request):
    return render(request, 'user/theUsers.html', {'users': ['greg', 'bob']})
