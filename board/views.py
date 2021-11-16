from django.shortcuts import render
from .models import BoardList
from django.views import View
from django.views import generic
# Create your views here.

def board_list(request):
    template_name = 'bbs_list.html'
    board_list = BoardList.objects.all()
    return render(request, template_name, {"board_list" : board_list})

print("a")