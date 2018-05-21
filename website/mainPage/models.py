from django.db import models
import time,datetime
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length = 100)
    members = models.IntegerField(default = 0)
    website = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length = 250)
    date_time = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    day_name = models.IntegerField(default = datetime.datetime.now().weekday())
    duration =models.IntegerField(default=0)
    event_description = models.CharField(default = '' ,max_length = 750)
    address = models.CharField(default = '' ,max_length = 750)
    picture_url = models.CharField(default = '' ,max_length = 3000)
    event_url = models.CharField(default = '' ,max_length = 3000)
    on_going = models.BooleanField(default = False)


    def __str__(self):
        return self.name


class Atendee(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    bio =  models.CharField(default = '' ,max_length = 3000)
    events = models.ManyToManyField(Event,related_name='atendees')
    friends = models.ManyToManyField('self',related_name='friends')

