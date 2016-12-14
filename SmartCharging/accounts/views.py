from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm         #Use authentication
from django.core.urlresolvers import reverse_lazy                #Redirect to the last url after login
from django.shortcuts import render
from django.views import generic            #Allow to use form view

class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("listPlugType")
    template_name = "accounts/login.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return  super().form_valid(form)