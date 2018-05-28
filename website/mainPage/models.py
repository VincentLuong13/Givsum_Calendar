from django.db import models
import time,datetime
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

REPEAT_CHOICES= [
    ('none', 'None'),
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('yearly','Yearly')
    ]
DAY_CHOICES = [
    ('None', 'None'),
    ('1','Sunday'),
    ('2','Monday'),
    ('3','Tuesday'),
    ('4','Wednesday'),
    ('5','Thursday'),
    ('6','Friday'),
    ('7','Saturday')
]

class Organization(models.Model):
    name = models.CharField(max_length = 100)
    members = models.IntegerField(default = 0)
    website = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length = 250)
    date_time = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    end_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    day_name = models.IntegerField(default = datetime.datetime.now().weekday())
    duration =models.IntegerField(default=0)
    event_description = models.CharField(default = '' ,max_length = 750)
    address = models.CharField(default = '' ,max_length = 750)
    picture_url = models.CharField(default = '' ,max_length = 3000)
    event_url = models.CharField(default = '' ,max_length = 3000)
    repeat = models.CharField(max_length = 128, choices = REPEAT_CHOICES, default='None')
    day_repeat = MultiSelectField(choices = DAY_CHOICES, default = 'None')
    


    def __str__(self):
        return self.name


class eventRepeat(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    end_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    

class Atendee(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    bio =  models.CharField(default = '' ,max_length = 3000)
    events = models.ManyToManyField(Event,related_name='atendees')
    friends = models.ManyToManyField('self',related_name='friends')

