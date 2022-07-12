from math import remainder
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import RequestContext

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request, username=username, password=password)

        if User is not None:
         login(request, User)
         return redirect('dashboard')
        #else:
        # messages.warning(request, 'invalid username or password, please try again')
         #redirect('login')

    
    else:
        return render(request, 'authenticate/login.html', {})




