from django import forms
from . import  models



class ChargingStationCreate(forms.ModelForm):
    class Meta:
        model = models.ChargingSpot
        fields = [
            'name',
            'plugType'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'plugType': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': "Charging station name"
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

'''class ChargingStation(forms.Form):
    name = forms.CharField()'''
