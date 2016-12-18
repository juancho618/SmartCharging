from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required           #This is need to validate that the user is log to create a new register
from django.views.generic import (DeleteView, ListView, CreateView,
                                  DetailView, UpdateView)
from django.core.urlresolvers import reverse_lazy


from . import models
from . import forms


from .models import ChargingSpot
from .forms import PlugTypeCreate, AppointmentCreate, RateSation
# Create your views here.

def chargingSpotList(request):
    chargingSpots = ChargingSpot.objects.all()
    return render(request, 'ChargingAppointment/chargingSpot/list.html', {'chargingSpots': chargingSpots})

#@login_required
def createChargingSpot(request):
    form = forms.ChargingStationCreate()
    if request.method == 'POST':
        print(request.POST.get('latitude'))
        form = forms.ChargingStationCreate(request.POST)
        if form.is_valid():
            chargingStation = form.save(commit=False)
            chargingStation.latitude = request.POST.get('latitude')
            chargingStation.longitude = request.POST.get('longitude')
            chargingStation.country = request.POST.get('country')
            chargingStation.city = request.POST.get('city')
            chargingStation.area = request.POST.get('area')
            chargingStation.neighborhood  = request.POST.get('neighborhood')
            chargingStation.save()
            #return HttpResponseRedirect(chargingStation.get_absolute_url())
    return render(request, 'ChargingAppointment/chargingSpot/create.html', {'form': form})

class ChargingStationDetail(LoginRequiredMixin, DetailView, CreateView ):
    form_class = RateSation
    model = models.ChargingSpot
    template_name = "ChargingAppointment/chargingSpot/details.html"


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.chargingStation = models.ChargingSpot.objects.get(pk=1)
        return super(ChargingStationDetail, self).form_valid(form)




#@login_required
def createPlugType(request):
    form = forms.PlugTypeCreate()
    if request.method == 'POST':
        form = forms.PlugTypeCreate(request.POST)
        if form.is_valid():
            plugType = form.save()
            print(plugType)
            #return HttpResponseRedirect()
    return render(request, 'ChargingAppointment/plugType/create.html', {'form': form})



#------------------------PlugType Controllers------------------------

#------------Details-------------------
class PlugTypeDetailView(LoginRequiredMixin, DetailView):
    model = models.PlugType
    template_name = "ChargingAppointment/plugType/details.html"


#------------Create-------------------
class PlugTypeCreateView(LoginRequiredMixin,CreateView):
    form_class = PlugTypeCreate
    template_name = "ChargingAppointment/plugType/create.html"
    model = models.PlugType

#------------Edit (Update)-------------------
class PlugTypeUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PlugTypeCreate
    template_name = "ChargingAppointment/plugType/create.html"
    model = models.PlugType

#------------List-------------------
class PlugTypeListView(LoginRequiredMixin,CreateView, ListView ):
    context_object_name = 'plugtype'
    model = models.PlugType
    form_class = PlugTypeCreate
    template_name = "ChargingAppointment/plugType/list.html"



#------------Delete-------------------
class PlugTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = models.PlugType
    template_name = "ChargingAppointment/plugType/delete.html"
    success_url = reverse_lazy("listPlugType")


#-----------Appointment----------------------------

#-----create-------------------------

class CreateAppointmentView(LoginRequiredMixin, CreateView):
    form_class = AppointmentCreate
    template_name = "ChargingAppointment/appointment/create.html"
    model = models.Appointment

    def form_valid(self, form):
        form.instance.userReservation = self.request.user
        return super(CreateAppointmentView, self).form_valid(form)

    #def get_context_data(self, **kwargs):
     #   context = super(CreateAppointmentView, self).get_context_data(**kwargs)
      #  user = self.request.user
       # print(user)
        #return context

    #def get_initial(self):
     #  return {'userReservation': self.request.user}

    #def get_queryset(self):
     #   return models.Appointment.objects.filter(userReservation  = self.request.user.pk)