'''
Models for oganizations
'''

from __future__ import unicode_literals
from django.db import models

class Organization(models.Model):
    """Our organization model"""

    organization_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    free = models.BooleanField()
    tuition = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    category = models.TextField(null=False)
    address = models.TextField(null=True)
    contact_number = models.TextField(null=True)
    website = models.TextField(null=True)
    imageURL = models.TextField(null=True)


    def __str__(self):
        return str(self.organization_id) + ', ' + self.name + ', ' + self.description + ', ' +\
        str(self.free) + ', ' + self.tuition + ', ' + str(self.rating) + ', ' +\
        self.category + ', ' + self.address
