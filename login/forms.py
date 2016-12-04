from user.models import User
from django import forms

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'name', 'school_name', 'password']
