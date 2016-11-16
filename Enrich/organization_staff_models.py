from __future__ import unicode_literals
from django.db import models

class Organization_Staff(models.Model):
    organization_staff_id = models.IntegerField(primary_key = True)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 30)
    name = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    organization_id = models.IntegerField() #Make foreign key later
