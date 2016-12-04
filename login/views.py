from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from user.models import User
#from django.http import HttpResponse

# Create your views here.
def index(request):
    """Main login page"""
    return render(request, "login/loginpage.html")

class RegistrationFormView(View):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)

            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user.set_password(password)
            User.objects.create(user)


            #user_id=User.objects.get(pk=user_id),
