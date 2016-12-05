'''
Admin app privillages to allow for the adding of users
'''
from django.contrib import admin
from user import models

admin.site.register(models.EnrichUser)
