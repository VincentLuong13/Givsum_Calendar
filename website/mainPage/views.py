from django.shortcuts import render
from .models import Organization, Event
import datetime
import calendar
from collections import defaultdict
from .handle_calendar import get_calendar_variables
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect

    
global cal_month
global cal_year
cal_year = datetime.datetime.today().year
cal_month  = datetime.datetime.today().month
def index(request):
    event_dict = defaultdict(list)
    events = Event.objects.all()

    # dictionary key = dates, values = list of events
    for ev in sorted(events,key = lambda x: x.date_time):
        event_dict[str(ev.date_time.strftime("%A"))+ ', ' + str(ev.date_time.strftime("%B")) + ' '+str(ev.date_time.day) +', '+ str(ev.date_time.year)].append(ev)
    month_template = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    
    insert_dict = {'ev_dict': dict(event_dict),'months': month_template}
    insert_dict.update(get_calendar_variables())
    return render(request,'mainPage/index.html',insert_dict)
    

def calendarPage(request):
    global cal_month

    cal_var = get_calendar_variables(c_month = cal_month, c_year = cal_year)

    
    events = Event.objects.filter(date_time__month = cal_var["cur_month"])
    insert_dict = {'events': sorted(events,key = lambda x: x.date_time)}
    insert_dict.update(cal_var)
    return render(request,'mainPage/calendarPage.html',insert_dict)

def nextMonth(request):
    global cal_month
    global cal_year

    if cal_month == 12:
        cal_month = 1
        cal_year += 1
    else:
        cal_month += 1

    return HttpResponseRedirect('/calendarpage')

def prevMonth(request):
    global cal_month
    global cal_year
    if cal_month == 1:
        cal_month = 12
        cal_year -= 1
    else:
        cal_month -= 1

    return HttpResponseRedirect('/calendarpage')

def resetToCurrent(request):
    global cal_month
    global cal_year
    cal_year = datetime.datetime.today().year
    cal_month  = datetime.datetime.today().month
    return HttpResponseRedirect('/calendarpage')