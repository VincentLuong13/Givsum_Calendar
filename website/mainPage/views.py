from django.shortcuts import render
from .models import Organization, Event

def index(request):
    events = Event.objects.all()
    return render(request,'mainPage/index.html',{'events': sorted(events,key = lambda x: x.name)})
