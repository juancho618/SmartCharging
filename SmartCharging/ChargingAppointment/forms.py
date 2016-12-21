from django import forms
from . import  models



class ChargingStationCreate(forms.ModelForm):
    class Meta:
        model = models.ChargingSpot
        fields = [
            'name',
            'plugType',
            'description'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'plugType': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': "Charging station name",
            'Plug Type': "Plug Type"
        }

class PlugTypeCreate(forms.ModelForm):
    class Meta:
        model = models.PlugType
        fields = [
            'name'
        ]
        labels = {
            'name': "Plug type name"
        }

class AppointmentCreate(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = [
            'chargingStation',
            'reservationDate',
        ]
        widgets = {
            'reservationDate': forms.TextInput(attrs={'class': 'flatpickr'}),
        }
        labels = {
            'chargingStation': "Charging station",
        }

class AppointmentCalendar(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields=[
            'chargingStation'
        ]

class RateSation(forms.ModelForm):
    class Meta:
        model = models.ChargingStationRate
        fields = [
            'rate',
        ]
        widgets = {
            'rate': forms.NumberInput(attrs={'class': 'hidden'}),
        }
        labels = {
            'rate' : ""
        }

'''class ChargingStation(forms.Form):
    name = forms.CharField()'''
