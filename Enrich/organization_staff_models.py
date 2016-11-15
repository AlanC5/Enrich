from __future__ import unicode_literals
from django.db import models

class Organization_Staff(models.Model):
    organization_staff_id = models.IntegerField(primary_key = True)
    email = models.CharField()
    password = models.CharField()
    name = models.CharField()
    title = models.CharField()
    organization_id = models.IntegerField() #Make foreign key later
