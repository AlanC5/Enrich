"""Our Enrich app models"""

from __future__ import unicode_literals
from django.db import models

class Organization_Staff(models.Model):
    """Organization staff model"""

    organization_staff_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    organization_id = models.ForeignKey('Reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.organization_staff_id + ', ' + self.email + ', ' + self.name + ', ' + \
        self.title + ', ' + self.organization_id

class Reviews(models.Model):
    """Reviews Model"""
    review_id = models.IntegerField(primary_key=True)
    review_text = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField()
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    organization_id = models.ForeignKey('Organization', on_delete=models.CASCADE)

    def __str__(self):
        return self.review_id + ', ' + self.review_text + ', ' + self.rating + ', ' + self.date \
        + ', ' + self.user_id + self.organization_id
