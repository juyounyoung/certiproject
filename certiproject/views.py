from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def login(request):
    return render(request,'./login.html')

def bbs_list(request):
    return render(request,'./bbs_list.html')

def bbs_register(request):
    return render(request,'./bbs_register.html')

def signin(request):
    # return render(request, '/bbs_list.html')
    if request.method =='POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            return render(request, './bbs_list.html')

        else:
            return HttpResponse('Login failed. Try again.')
    else:
        form = LoginForm()
        return render(request, './login.html')
