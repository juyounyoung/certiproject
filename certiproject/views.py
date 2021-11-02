from django.shortcuts import render
from django.http import HttpResponse
def login(request):
    return render(request,'./login.html')

def bbs_list(request):
    return render(request,'./bbs_list.html')
