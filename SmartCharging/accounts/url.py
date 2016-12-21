from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r"login/$", views.LoginView.as_view(), name="login"),
    url(r"logout/$", views.LogoutView.as_view(), name="logout"),
    url(r"signup/$", views.SingUp.as_view(), name="signup"),
    url(r'^profile/(?P<pk>\d+)/$', views.Profile.as_view(), name='profile'),

]