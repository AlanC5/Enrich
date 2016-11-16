from __future__ import unicode_literals
from django.db import models

class Reviews(models.Model):
    review_id = models.IntegerField(primary_key = True)
    review_text = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField()
    user_id = models.IntegerField()         #Make foreign key later
    organization_id = models.IntegerField() #Make foreign key later
