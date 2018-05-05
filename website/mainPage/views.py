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
    '''
    The index is basically the main page of our website. It creates a dictionary of events and then sorts all events by date. It sends all the events 
    to be viewed in a schedule-type view.
    '''
    event_dict = defaultdict(list)
    events = Event.objects.all()

    # dictionary key = dates, values = list of events
    for ev in sorted(events,key = lambda x: x.date_time):
        event_dict[str(ev.date_time.strftime("%A"))+ 
        ', ' + str(ev.date_time.strftime("%B")) + 
        ' '+str(ev.date_time.day) +', '+ str(ev.date_time.year)].append([ev,len(ev.atendees.all())])#len just for testing for number of attendees
    month_template = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    
    insert_dict = {'ev_dict': dict(event_dict),'months': month_template}
    insert_dict.update(get_calendar_variables())
    return render(request,'mainPage/index.html',insert_dict)
    

def calendarPage(request):
    '''
    This calendar page is the base calendar page. Redirecting to this page will bring you to the calendar view with default view month and will show you
    the current month. It works by taking in events that only take place in the current month, the amount of days in the month, and which day the month starts on
    and then sends those events to calendarPage.html to create the calendar view.
    '''

    today_date = datetime.datetime.today()
    cal_var = get_calendar_variables(c_month = today_date.month, c_year = today_date.year) #retrieves all the variables for the current calendar month/year

    data = {'n_view': 'month', 'n_year': today_date.year, 'n_month': today_date.month, 'n_day': today_date.day} #makes a dictionary of the current day's month/day/year, needed to view the next month/week/year
    events = Event.objects.filter(date_time__month = cal_var["cur_month"])

    insert_dict = {'events': sorted(events,key = lambda x: x.date_time)} #creates a dictionary with the events in the current month

    insert_dict.update(cal_var) #adds the calendar variables into the dictionary that will passed onto html
    insert_dict.update(data) #adds needed data into the dictionary that will passed onto html


    return render(request,'mainPage/calendarPage.html',insert_dict) #creates the calendar view using the insert dict

def cal(request, view, year, month, day):
    '''
    The cal view is used for displaying views on the calendar using specific dates in the past or in the future.
    It works by taking in the desired view type, the year, the month, and the day, and then does the same thing calendarPage does except
    it uses the variables for the desired month/year/week instead of the the current date's variables.
    '''
    if view == 'month':
        cal_var = get_calendar_variables(c_month = int(month), c_year = int(year)) #creates a cal_var using the desired month/year

        events = Event.objects.filter(date_time__month = cal_var["cur_month"])
        insert_dict = {'events': sorted(events,key = lambda x: x.date_time)}
        insert_dict.update(cal_var)
        data = {'n_view': view, 'n_year': year, 'n_month': month, 'n_day': day}
        insert_dict.update(data)
    
    return render(request,'mainPage/calendarPage.html', insert_dict)

def nextView(request, view, year, month, day):
    '''
    The nextView function is used to increment views. It takes in the parameters view, year, month, and day and will increment the days/month/year depending on 
    the desired view.
    '''
    if view == 'month':
        if month == 12: #makes sure that if the month is December, it will increment the year by 1 and set the month to January
            month = 1
            year += 1
        else:
            month += 1
        day = 1 #sets the day to 1 just to be sure that the date is a valid day

    return HttpResponseRedirect('/' + str(view) + '/' + str(year) + '-' + str(month) + '-' + str(day) + '/') #month/2018-06-12 -> month/2018/07/01

def prevView(request,view, year, month, day):
    '''
    The prevView function is used to decrement views. It takes in the parameters view, year, month, and day and will decrement the days/month/year depending on
    the desired view
    '''
    if view =='month':  #makes sure that if the month is January, it will decrement the year by 1 and set the month to December  
        if month == 1:
            month = 12
            year -= 1
        else:
            month -= 1
        day = 1 #makes sure that the day is a vali date

    return HttpResponseRedirect('/' + str(view) + '/' + str(year) + '-' + str(month) + '-' + str(day) + '/') #month/2018-06-12 -> month/2018-05-01

def resetToCurrent(request):
    '''
    This function redirects to the calendarpage to reset the date to view the current month/week/year
    '''
    return HttpResponseRedirect('/calendarpage')