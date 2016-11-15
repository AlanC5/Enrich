from django.db import models

class User(models.Model):
    user_id = models.CharField(primary_key = True)
    email = models.CharField()
    password = models.CharField()
    name = models.CharField()
    schoolName = models.CharField()
