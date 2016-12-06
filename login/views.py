from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import View
from user.models import EnrichUser
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from .forms import RegistrationForm

# Create your views here.

def logout_user(request):
    logout(request)
    return render(request, 'search/search.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                curr_user = EnrichUser.objects.filter(user=request.user)
                return render(request, 'search/search.html')
        else:
            return render(request, 'login/login_register.html', {'error_message': 'Invalid login'})
    return render(request, 'login/login_register.html')


def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        if user is not None:
            login(request, user)
            return render(request, 'search/search.html')
        return render(request, 'search/search.html')
    context = {
        "form": form,
    }
    return render(request, 'login/login_register.html', context)
