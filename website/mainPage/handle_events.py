from .models import Organization, Event,eventRepeat,Atendee
from datetime import timedelta,datetime
import calendar

def createRepeatEvents(parent):
    if (str(parent.repeat) ==  'None'):
        event = eventRepeat(event = parent,date_time = parent.date_time,end_date = parent.date_time,name = parent.name)
        event.save()
    else:
        for dt in create_specific_day_events(parent):
            print(str(parent.repeat))
            start = dt
            end = parent.end_date
            change = timedelta(days = 0)
            if (str(parent.repeat) ==  'monthly'):
                while (start<=end):
                    next_date  =  start.replace(month = start.month+1)
                    num_days = len(range(calendar.monthrange(next_date.year,next_date.month)[1]))
                    change = timedelta(days = num_days)
                    duration = parent.end_time - parent.date_time
                    event = eventRepeat(event = parent,date_time = start,end_time = start+duration,name=parent.name)
                    event.save()
                    start = start+change 
            else:
                
                if (str(parent.repeat) ==  'daily'):
                    change = timedelta(days = 1)
                elif (str(parent.repeat) ==  'weekly'):
                    change = timedelta(weeks = 1)
                elif (str(parent.repeat) ==  'yearly'):
                    change = timedelta(days = 365)
                while (start<=end):
                    duration = parent.end_time - parent.date_time
                    event = eventRepeat(event = parent,date_time = start,end_time = start+duration,name=parent.name)
                    event.save()
                    start = start+change 
                

def create_specific_day_events(parent):
    days = parent.day_repeat
    events_datetimes = []
    conversion_dict = {'Sunday': 1,'Monday': 2,'Tuesday': 3,'Wednesday': 4,'Thursday': 5,'Friday': 6,'Saturday': 7}
    parent_day = conversion_dict[parent.date_time.strftime("%A")]
    for day in days:
        if day != 'None':
            diff = int(parent_day) - int(day)
            if diff>0:
                alter = timedelta(days= (7-int(diff)))
            elif (diff <0):
                alter = timedelta(days = (-diff))
                
            elif diff == 0:
                alter = timedelta(day = 0)

            dy = parent.date_time + alter
            events_datetimes.append(dy)
    if len(events_datetimes) == 0:
        events_datetimes.append(parent.date_time)
    return events_datetimes


def edit_repeat_event(parent,time,edit,attr,change):

    if edit == 'this':
        events = parent.child.all().filter(date_time = time)
    elif edit == 'all':
        events = parent.child.all()
    elif edit == 'this_continue':
        events = [event for event in parent.child.all() if event.date_time>= time]

    for event in events:
        setattr(event,attr,change)






            
    
        
        
        




