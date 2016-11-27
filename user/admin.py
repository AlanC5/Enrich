'''
Admin app privillages to allow for the adding of users
'''
from django.contrib import admin
from user.models import User

admin.site.register(User)
