from django.contrib import admin
from .models import  ChargingSpot, PlugType, Appointment

admin.site.register(ChargingSpot)
admin.site.register(PlugType)
admin.site.register(Appointment)
# Register your models here.
