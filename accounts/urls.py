"""UserDetails URL Configuration

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

from accounts.views import UserRegister, ProfileUpdate, UserList

# Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3NzM1MTU2LCJpYXQiOjE2MzY0MzkxNTYsImp0aSI6ImZlY2MzNTI5N2Q0NzQ4NGJhNDQ5Y2U4NDM1NThhZGFmIiwidXNlcl9pZCI6N30.hFElt0PB-p1INfMBnellP-ZTMEYSB8KtihUBTVeo-Zc

urlpatterns = [
    path('register', UserRegister.as_view(),name='register'),
    path('profile-update', ProfileUpdate.as_view(), name='profile-update'),
    path('user-list', UserList.as_view(), name='user-list'),

]
