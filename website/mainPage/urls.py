from django.contrib import admin
from django.urls import path
from . import views

app_name = "mainPage"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('calendarpage/',views.calendarPage , name = 'calendar'),
    path('calendarpage/nextMonth/', views.nextMonth, name = 'nextMonth'),
    path('calendarpage/prevMonth/', views.prevMonth, name = 'prevMonth'),
]
