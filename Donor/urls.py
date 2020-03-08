"""Dharko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views
from django.views.generic import ListView

from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),  # for home page url
    # to dispaly bloodbank url
    path('bloodbank/', views.bloodbank, name='bloodbank',),
    # get news and event form database and dispaly it
    path('news&events/', views.news, name='event'),
    path('news&events/<int:pk>', views.newsView, name='event'),
    path('feedback/', views.feedback, name='feedback'),  # feedback form url
    path('about/', views.about, name='about'),  # about url
    path('contact/', views.contact, name='contact'),  # contact us url
]
