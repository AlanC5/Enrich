"""user views"""


from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):#request):
    """User index"""
    all_users = User.objects.all()
    html = ''
    for user in all_users:
        url = '/user/' + str(user.id) + '/'
        html += '<a href="' + url + '"> ' + user.username + '</a><br>'
    return HttpResponse(html)

def hey():#request):
    """Test code returning Hey"""
    return HttpResponse("<h2>heyyyy</h2>")

def getUser(request):
    """Gets all users"""
    return render(request, 'user/theUsers.html', {'users': ['greg', 'bob']})
