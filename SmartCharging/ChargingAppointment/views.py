from django.http import HttpResponse
from django.shortcuts import render
from . import forms

from .models import ChargingSpot
# Create your views here.

def chargingSpotList(request):
    chargingSpots = ChargingSpot.objects.all()
    return render(request, 'ChargingAppointment/chargingSpot/list.html', {'chargingSpots': chargingSpots})

def createChargingSpot(request):
    form = forms.ChargingStation()
    return render(request, 'ChargingAppointment/chargingSpot/create.html', {'form': form})