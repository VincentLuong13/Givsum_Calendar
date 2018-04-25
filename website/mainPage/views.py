from django.shortcuts import render
from .models import Organization, Event
import datetime
import calendar
from collections import defaultdict

def index(request):
    event_dict = defaultdict(list)
    events = Event.objects.all()
    # trying dictionary
    for ev in sorted(events,key = lambda x: x.date_time):
        event_dict[str(ev.date_time.strftime("%A")) + ' '+str(ev.date_time.day) +', '+ str(ev.date_time.year)].append(ev)
    month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    return render(request,'mainPage/index.html',{'ev_dict': dict(event_dict), "months": month})

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