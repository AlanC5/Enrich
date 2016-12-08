"""Login forms"""
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(forms.ModelForm):
    """Registration form"""

    class Meta:
        """Meta data about form"""
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password']
