from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.contrib.auth.views import login

app_name = "mainPage"
urlpatterns = [
    path('schedulepage/', views.schedulepage, name = 'schedule'), #schedulepage/, the 'home page', view of the schedule
    #path('schedulepage/myevents', views.myEvents, name = 'myevents'), #schedulepage/myevents/, the 'home page', view of the schedule for my events only
    #path('schedulepage/friendevents', views.friendEvents, name = 'friendevents'), #schedulepage/friendevents/, the 'home page', view of the schedule for my events only
    path('calendarpage/',views.calendarPage , name = 'calendar'), #calendarpage/, the current month's view of the calendar page
    path('calendarpage/curDay/', views.resetToCurrent, name = 'currentTime'), #resets the day to today, then redirects to calendarpage/
    re_path(r'^(?P<view>month|week|year)\/(?P<year>[1-9]?[0-9]{3})-(?P<month>[0-1]?[0-9])-(?P<day>[0-3]?[0-9])\/filters\=(?P<filter>all|myevents|friends)\/$', views.cal, name = 'cal'), #month/2018-10-3, changes the current view using the desired view type, and the date. Uses calendarpage.html to create the calendar
    path('calendarpage/nextView/<str:view>/<int:year>/<int:month>/<int:day>/filters=<str:filter>/', views.nextView, name = "nextView"), #calendarpage/nextView/month/2018/10/3, uses the nextView function to increment the view type to display the next view, then redirects the link to show the updated view
    path('calendarpage/prevView/<str:view>/<int:year>/<int:month>/<int:day>/filters=<str:filter>/', views.prevView, name = "prevView"), #calendarpage/prevView/week/2018/10/3, uses thep prevView function to decrement the view type to display the next view, then redirects thel ink tos how the updated view 
    path('',login,{'template_name':'mainPage/login.html'}),
    path('calendarpage/year/', views.yearview, name = 'yearview3'),
    path('calendarpage/year/<int:year>/filters=<str:filter>/', views.yearview, name = 'yearview2'),
    path('calendarpage/year/filters=<str:filter>/', views.yearview, name = 'yearview1'),
    #re_path(r'^schedulepage\/filter=(?P<filter>all|myevents|friend)/$', views.schedulepage, name = "schedulepage"),
    path('schedulepage/filters=<str:filter>/', views.schedulepage, name = 'schedulepage'),
    path('calendarpage/filters=<str:filter>/',views.calendarPage , name = 'calendarpage'),

]
