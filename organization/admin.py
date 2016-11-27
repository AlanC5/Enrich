'''
Admin app privillages to allow for the adding of organizations
'''
from django.contrib import admin
from organization.models import Organization

admin.site.register(Organization)
