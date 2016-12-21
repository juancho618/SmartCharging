from django.shortcuts import render


def layout(request):
    return  render(request, 'layout.html')

def home(request):
    return  render(request, 'home.html')

