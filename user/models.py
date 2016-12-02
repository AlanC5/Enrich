"""user models"""

from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(null=False, max_length = 100)
    password = models.CharField(null=False, max_length = 30)
    name = models.CharField(null=False, max_length = 100)
    school_name = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.user_id) + ', ' + self.email + ', ' + self.name + ', ' + self.school_name
