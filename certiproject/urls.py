"""certiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import include, path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.signin, name='login'),
    path('board/',include('board.urls')),
   # path('bbs_list', views.Board_list, name='bbs_list'),
    path('bbs_register', views.bbs_register, name='bbs_register'),
    path('admin/', admin.site.urls),
    # path('', templates.views.index,name='login'),
    path('auth/', include('users.urls')),
    path('preview', views.preview, name='preview'),
    path('register_ondirect', views.register_ondirect, name='register_ondirect'),
]