from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.


def home(request):
    return redirect('register/')


def register(request):
    return render(request,'authentication_app/register.html')


def login(request):
    return render(request,'authentication_app/login.html')

