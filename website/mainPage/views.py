from django.shortcuts import render
from .models import Organization, Event
import datetime
import calendar
from collections import defaultdict
from .handle_calendar import get_calendar_variables
    

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
    cal_var = get_calendar_variables(c_month = 2)
    events = Event.objects.filter(date_time__month = cal_var["cur_month"])
    insert_dict = {'events': sorted(events,key = lambda x: x.date_time)}
    insert_dict.update(cal_var)
    return render(request,'mainPage/calendarPage.html',insert_dict)