from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def school_list(request):
#        return HttpResponse("Hello, world. You're at the bbs index.")


def login(request):
        return render(request,'templates/login.html',)
