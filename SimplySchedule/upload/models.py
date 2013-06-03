# Create your models here.
from django.db import models

class Attendee(models.Model):
    name = models.CharField()
    prefs = models.CharField()
    sessions = models.ManyToManyField(Workshop)

    def __unicode__(self):
        return self.name

class Workshop(models.Model):
    name = models.CharField(max_length=120)
    sessions = models.ManyToManyField(Session)

    def __unicode__(self):
        return self.name

