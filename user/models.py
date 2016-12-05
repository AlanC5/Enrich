"""user models"""

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class EnrichUser(models.Model):
    user = models.OneToOneField(User, primary_key = True, related_name='enrichuser', default=1)
    school_name = models.CharField(max_length = 100, null=True)

    def __str__(self):
        return self.user.username

def create_enrich_user(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        enrich_user = EnrichUser(user=user)
        enrich_user.save()
post_save.connect(create_enrich_user, sender=User)


#def create_enrich_user(request):
#        obj = EnrichUser(user_id=request.user)
#        obj.save()
#        return True
