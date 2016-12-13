from django import forms


class ChargingStation(forms.Form):
    name = forms.CharField()
