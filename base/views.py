from django.shortcuts import render, redirect
#from django.contrib import messages
#from django.contrib.auth import authenticate, login, logout
from .models import data
from django.http import HttpResponse

# Create your views here.


def dashboard(request):
    return render(request, 'base/dashboard.html')



    