from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm         #User authentication by default from Django!
from django.core.urlresolvers import reverse_lazy                       #Redirect to the last url after login
from django.shortcuts import render
from django.views import generic            #Allow to use form view

from . import forms
from django.contrib.auth import get_user_model

class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('chargingSpotsList')
    template_name = "accounts/login.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return  super().form_valid(form)

class LogoutView(generic.RedirectView):
    url = reverse_lazy('chargingSpotsList')

    def get(self, request, *args, **kwargs):
        logout(request)
        return  super().get(request, *args, **kwargs)

class SingUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = "accounts/signup.html"

    def  form_valid(self, form):
        form.instance.display_name =  form.instance.username
        return super(SingUp, self).form_valid(form)

class Profile(generic.DetailView):
    model = get_user_model()
    template_name = "accounts/profile.html"