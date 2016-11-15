from __future__ import unicode_literals
from django.db import models

class Organization(models.Model):
    organization_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    free = models.BooleanField()
    tuition = models.TextField()
    rating = models.DecimalField(max_digits = 2, decimal_places = 1)
    category = models.TextField()
    address = models.TextField()
