from django.contrib import admin
from .models import Event,Organization,Atendee,eventRepeat

# Register your models here.
admin.site.register(Event)
admin.site.register(Organization)
admin.site.register(Atendee)
admin.site.register(eventRepeat)