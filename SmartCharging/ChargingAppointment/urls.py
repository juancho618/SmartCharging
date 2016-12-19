from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns =[
    url(r'^$', views.chargingSpotList, name='chargingSpotsList'),
    url(r'^chargingSpot/create', views.createChargingSpot, name='createChargingStation'),
    url(r'^chargingSpot/(?P<pk>\d+)/$', views.ChargingStationDetail.as_view(), name='detailsChargingStation'),
    url(r'^plugType/create/$', views.PlugTypeCreateView.as_view(), name='createPlugType'),
    url(r'^plugType/(?P<pk>\d+)/$', views.PlugTypeDetailView.as_view(), name='detailPlugType'),
    url(r'^plugType/edit/(?P<pk>\d+)/$', views.PlugTypeUpdateView.as_view(), name='updatePlugType'),
    url(r'^plugType/$', views.PlugTypeListView.as_view(), name='listPlugType'),
    url(r'^plugType/delete/(?P<pk>\d+)/$', views.PlugTypeDeleteView.as_view(), name='deletePlugType'),
    url(r'^appointment/create/$', views.CreateAppointmentView.as_view(), name='createAppointment'),
    url(r'^appointment/calendar/(?P<pk>\d+)/$', views.AppointmentCalendar.as_view(), name='calendarAppointment'),

]