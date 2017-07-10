from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=30)
    password = models.IntegerField()

    def __unicode__(self):
        return  self.name
