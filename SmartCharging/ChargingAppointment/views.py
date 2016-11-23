from django.http import HttpResponse
from django.shortcuts import render

from .models import ChargingSpot
# Create your views here.

def chargingSpotList(request):
    chargingSpots = ChargingSpot.objects.all()
    return render(request, 'ChargingAppointment/chargingSpot/list.html', {'chargingSpots': chargingSpots})