from django.db import models
import time

class Organization(models.Model):
    name = models.CharField(max_length = 100)
    members = models.IntegerField(default = 0)
    website = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length = 250)
    time = models.CharField(max_length = 250)
    date = models.CharField(max_length = 250)
    event_description = models.CharField(default = '' ,max_length = 750)
    address = models.CharField(default = '' ,max_length = 750)
    picture_url = models.CharField(default = '' ,max_length = 1000)

    def __str__(self):
        return self.name
