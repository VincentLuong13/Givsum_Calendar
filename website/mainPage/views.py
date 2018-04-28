from django.shortcuts import render
from .models import Organization, Event
import datetime
import calendar
from collections import defaultdict

# def get_calendar_variables():
#     today_date = datetime.datetime.today()
#     first_day = {'Sunday': 1,'Monday': 2,'Tuesday': 3,'Wednesday': 4,'Thursday': 5,'Friday': 6,'Saturday': 7}[today_date.replace(day=1).strftime("%A")]
#     year = today_date.year
#     month = today_date.month
#     day = today_date.day

#     info_dict = {'cur_name_of_month' :calendar.month_name[month],
#     'cur_num_days': range(calendar.monthrange(year,month)[1]),
#     'cur_year':year,
#     'cur_month':month,
#     'cur_day' : day,
#     'cur_name_of_day' : datetime.datetime.now().strftime("%A"),
#     'first_day':range(first_day-1)}
    
#     return info_dict
    

def index(request):
    ##Test
    today_date = datetime.datetime.today()
    first_day = {'Sunday': 1,'Monday': 2,'Tuesday': 3,'Wednesday': 4,'Thursday': 5,'Friday': 6,'Saturday': 7}[today_date.replace(day=1).strftime("%A")]
    year = today_date.year
    month = today_date.month
    day = today_date.day

    event_dict = defaultdict(list)
    events = Event.objects.all()
    # dictionary key = dates, values = list of events
    for ev in sorted(events,key = lambda x: x.date_time):
        event_dict[str(ev.date_time.strftime("%A"))+ ', ' + str(ev.date_time.strftime("%B")) + ' '+str(ev.date_time.day) +', '+ str(ev.date_time.year)].append(ev)
    month_template = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    
    return render(request,'mainPage/index.html',
    {'ev_dict': dict(event_dict),
    'months': month_template,
    'cur_name_of_month' :calendar.month_name[month],
    'cur_num_days': range(calendar.monthrange(year,month)[1]),
    'cur_year':year,
    'cur_month':month,
    'cur_day' : day,
    'cur_name_of_day' : datetime.datetime.now().strftime("%A"),
    'first_day':range(first_day-1)})

def calendarPage(request):
    today_date = datetime.datetime.today()
    first_day = {'Sunday': 1,'Monday': 2,'Tuesday': 3,'Wednesday': 4,'Thursday': 5,'Friday': 6,'Saturday': 7}[today_date.replace(day=1).strftime("%A")]
    year = today_date.year
    month = today_date.month
    day = today_date.day
    events = Event.objects.all()
    return render(request,'mainPage/calendarPage.html',
    {'events': sorted(events,key = lambda x: x.name),
    'cur_name_of_month' :calendar.month_name[month],
    'cur_num_days': range(calendar.monthrange(year,month)[1]),
    'cur_year':year,
    'cur_month':month,
    'cur_day' : day,
    'cur_name_of_day' : datetime.datetime.now().strftime("%A"),
    'first_day':range(first_day-1)})