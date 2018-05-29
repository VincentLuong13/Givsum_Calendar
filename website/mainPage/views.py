from django.shortcuts import render, redirect, get_object_or_404
from .models import Organization, Event,Atendee,eventRepeat
from django.contrib.auth.models import User
import datetime
import calendar
from collections import defaultdict
from .handle_calendar import get_calendar_variables,handle_year_info
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from .handle_events import createRepeatEvents,create_specific_day_events


    
global cal_month
global cal_year
cal_year = datetime.datetime.today().year
cal_month  = datetime.datetime.today().month


def schedulepage(request, filter = "all"):
    event_dict = defaultdict(list)
    if filter == 'all':
        events = Event.objects.all()
    elif filter == 'myevents':
        try:
            events = request.user.profile.events.all()
        except:
            events = []
    elif filter =='ongoing':
        events = Event.objects.all().exclude(repeat='None')
    elif filter == 'friends':
        events = Event.objects.none()
        try:
            friends = request.user.profile.friends.all()
            for friend in friends:
                events = events|friend.events.all()
            events = events.distinct()
                    
        except:
            events = []

    return scheduletemplate(request,events,event_dict)


    return scheduletemplate(request,events,event_dict)
def scheduletemplate(request,events,event_dict):
    user = request.user.profile
    # dictionary key = dates, values = list of events
    for ev in sorted(events,key = lambda x: x.date_time):
        event_dict[str(ev.date_time.strftime("%A"))+ 
        ', ' + str(ev.date_time.strftime("%B")) + 
        ' '+str(ev.date_time.day) +', '+ str(ev.date_time.year)].append([ev,len(ev.atendees.all()),ev.atendees.all(),(user in ev.atendees.all())])#len just for testing for number of attendees
    month_template = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    
    insert_dict = {'ev_dict': dict(event_dict),'months': month_template}
    insert_dict.update(get_calendar_variables())
    return render(request,'mainPage/index.html',insert_dict)

def calendarPage(request, filter = 'all'):
    '''
    This calendar page is the base calendar page. Redirecting to this page will bring you to the calendar view with default view month and will show you
    the current month. It works by taking in events that only take place in the current month, the amount of days in the month, and which day the month starts on
    and then sends those events to calendarPage.html to create the calendar view.
    '''
    # event_dict = defaultdict(list)
    if filter == 'all':
        events = Event.objects.all()
    elif filter == 'myevents':
        try:
            events = request.user.profile.events.all()
        except:
            events = []
    elif filter == 'ongoing':
        events = eventRepeat.objects.all()
    elif filter == 'friends':
        events = Event.objects.none()
        try:
            friends = request.user.profile.friends.all()
            for friend in friends:
                events = events|friend.events.all()
            events = events.distinct()
                    
        except:
            events = []

    today_date = datetime.datetime.today()
    cal_var = get_calendar_variables(c_month = today_date.month, c_year = today_date.year) #retrieves all the variables for the current calendar month/year

    data = {'n_view': 'month', 'n_year': today_date.year, 'n_month': today_date.month, 'n_day': today_date.day,'n_filter':filter} #makes a dictionary of the current day's month/day/year, needed to view the next month/week/year
    events = events.filter(date_time__month = cal_var["cur_month"])

    insert_dict = {'events': sorted(events,key = lambda x: x.date_time)} #creates a dictionary with the events in the current month

    insert_dict.update(cal_var) #adds the calendar variables into the dictionary that will passed onto html
    insert_dict.update(data) #adds needed data into the dictionary that will passed onto html


    return render(request,'mainPage/calendarPage.html',insert_dict) #creates the calendar view using the insert dict

def cal(request, view, year, month, day,filter ='all'):
    '''
    The cal view is used for displaying views on the calendar using specific dates in the past or in the future.
    It works by taking in the desired view type, the year, the month, and the day, and then does the same thing calendarPage does except
    it uses the variables for the desired month/year/week instead of the the current date's variables.
    '''
    if filter == 'all':
        events = Event.objects.all()
    elif filter == 'myevents':
        try:
            events = request.user.profile.events.all()
        except:
            events = []
    elif filter == 'ongoing':
        events = eventRepeat.objects.all()

    elif filter == 'friends':
        events = Event.objects.none()
        try:
            friends = request.user.profile.friends.all()
            for friend in friends:
                events = events|friend.events.all()
            events = events.distinct()
                    
        except:
            events = []
    if view == 'month':

        cal_var = get_calendar_variables(c_month = int(month), c_year = int(year)) #creates a cal_var using the desired month/year

        events = events.filter(date_time__month = cal_var["cur_month"])
        insert_dict = {'events': sorted(events,key = lambda x: x.date_time)}
        insert_dict.update(cal_var)
        data = {'n_view': view, 'n_year': year, 'n_month': month, 'n_day': day,'n_filter':filter}
        insert_dict.update(data)
    return render(request,'mainPage/calendarPage.html', insert_dict)

def nextView(request, view, year, month, day,filter):
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
    
    if view == 'year':
        return HttpResponseRedirect('/calendarpage/year/' + str(year + 1) + '/filters='+str(filter) + '/')
    return HttpResponseRedirect('/' + str(view) + '/' + str(year) + '-' + str(month) + '-' + str(day) + '/filters=' +str(filter) + '/') #month/2018-06-12 -> month/2018/07/01

def prevView(request,view, year, month, day,filter):
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

    if view == 'year':
        return HttpResponseRedirect('/calendarpage/year/' + str(year - 1) + '/filters='+str(filter) + '/')
    
    return HttpResponseRedirect('/' + str(view) + '/' + str(year) + '-' + str(month) + '-' + str(day) + '/filters='+str(filter) + '/') #month/2018-06-12 -> month/2018-05-01

def resetToCurrent(request,view,filter):
    '''
    This function redirects to the calendarpage to reset the date to view the current month/week/year
    '''
    print(filter)
    if(view == 'month'):
        return HttpResponseRedirect('/calendarpage/filters=' + str(filter)+'/')
    elif(view == 'year'):
        return HttpResponseRedirect('/calendarpage/year/filters=' + str(filter)+'/')
    

def yearview(request, year = datetime.datetime.today().year,filter = 'all'):
    if filter == 'all':
        events = Event.objects.all()
    elif filter == 'myevents':
        try:
            events = request.user.profile.events.all()
        except:
            events = []
    elif filter == 'ongoing':
        events = eventRepeat.objects.all()

    elif filter == 'friends':
        events = Event.objects.none()
        try:
            friends = request.user.profile.friends.all()
            for friend in friends:
                events = events|friend.events.all()
            events = events.distinct()
                    
        except:
            events = []
    today_date = datetime.datetime.today()
    cal_var = get_calendar_variables(c_month = today_date.month, c_year = year) #retrieves all the variables for the current calendar month/year

    data = {'n_view': 'month', 'n_year': year, 'n_month': today_date.month, 'n_day': today_date.day,'n_filter':filter} #makes a dictionary of the current day's month/day/year, needed to view the next month/week/year
    events = events.filter(date_time__year = year)
    insert_dict = {'events': sorted(events,key = lambda x: x.date_time)} #creates a dictionary with the events in the current month
    insert_dict.update(cal_var) #adds the calendar variables into the dictionary that will passed onto html
    insert_dict.update(data) #adds needed data into the dictionary that will passed onto html
    insert_dict['year_info'] = handle_year_info(year)#gets information for year

    heat_map = {'#feb24c':lambda x: x==1,'#fd8d3c':lambda x: x==2,'#f03b20':lambda x: x==3,'#bd0026' : lambda x: x==5}

    month_counter=1
    for month in insert_dict['year_info'].keys():
        insert_dict['year_info'][month]['day_distribution'] = {}
        for day in (insert_dict['year_info'][month]['cur_num_days']):
            temp_events = events.filter(date_time__year = year).filter(date_time__month = month_counter).filter(date_time__day = day+1)
            insert_dict['year_info'][month]['day_distribution'][day+1] = [temp_events,len(temp_events),[color for color in heat_map.keys() if heat_map[color]((len(temp_events)))]]
            if (len(insert_dict['year_info'][month]['day_distribution'][day+1][2])>=1):
                insert_dict['year_info'][month]['day_distribution'][day+1][2]  = insert_dict['year_info'][month]['day_distribution'][day+1][2][0]
            
        month_counter+=1
            

    
    return render(request,'mainPage/yearCal.html',insert_dict)

def rsvp(request, event):

    user = Atendee.objects.get(user = request.user)

    try:
        select = user.events.get(id = event)
    except:
        select = None
    
    if select:
        user.events.remove(event)
    else:
        user.events.add(event)
    return HttpResponseRedirect('/schedulepage/')

def weekview(request,filter = 'all'):
    if filter == 'all':
        events = Event.objects.all()
    elif filter == 'myevents':
        try:
            events = request.user.profile.events.all()
        except:
            events = []

    elif filter == 'friends':
        events = Event.objects.none()
        try:
            friends = request.user.profile.friends.all()
            for friend in friends:
                events = events|friend.events.all()
            events = events.distinct()
                    
        except:
            events = []

    today_date = datetime.datetime.today()
    cal_var = get_calendar_variables(c_month = today_date.month, c_year = today_date.year) #retrieves all the variables for the current calendar month/year

    data = {'n_view': 'month', 'n_year': today_date.year, 'n_month': today_date.month, 'n_day': today_date.day,'n_filter':filter} #makes a dictionary of the current day's month/day/year, needed to view the next month/week/year
    events = events.filter(date_time__month = cal_var["cur_month"])

    insert_dict = {'events': sorted(events,key = lambda x: x.date_time)} #creates a dictionary with the events in the current month

    insert_dict.update(cal_var) #adds the calendar variables into the dictionary that will passed onto html
    insert_dict.update(data) #adds needed data into the dictionary that will passed onto html

    return render(request,'mainPage/weekPage.html',insert_dict)

def controlView(request):
    events = Event.objects.all().filter(repeat = 'weekly')
    for e in events:
        createRepeatEvents(e)
    #create_specific_day_events(test)
    return render(request,'mainPage/controlPanel.html')