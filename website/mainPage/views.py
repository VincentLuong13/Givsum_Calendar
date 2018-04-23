from django.shortcuts import render
from .models import Organization, Event
import datetime
import calendar

def index(request):
    events = Event.objects.all()
    return render(request,'mainPage/index.html',{'events': sorted(events,key = lambda x: x.name)})

def calendarPage(request):
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    events = Event.objects.all()
    return render(request,'mainPage/calendarPage.html',
    {'events': sorted(events,key = lambda x: x.name),
    'name_of_month' :calendar.month_name[month],
    'num_days': range(calendar.monthrange(year,month)[1]),
    'year':year,
    'day' : day,
    'name_of_day' : datetime.datetime.now().strftime("%A")})