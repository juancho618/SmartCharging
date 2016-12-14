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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': "Plug type name"
        }
'''class ChargingStation(forms.Form):
    name = forms.CharField()'''
