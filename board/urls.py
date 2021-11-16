from django.urls import path,include
from . import views

urlpatterns =[
    #path('list/',views.board_list),
    path('',views.board_list),
]