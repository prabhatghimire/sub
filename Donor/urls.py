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

from Donor.models import Bloodbank, Event
from django.urls import path

from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('', views.home, name='home'), #for home page url
    path('graphql/', jwt_cookie(GraphQLView.as_view(graphiql=True))),
    path('bloodbank/', ListView.as_view(queryset=Bloodbank.objects.all().order_by("id")[:25], template_name='donner/banklist.html'),name='bloodbank',),  #to dispaly bloodbank url
    path('news&events/', ListView.as_view(queryset=Event.objects.all().order_by("-id")[:25], template_name='donner/News & Events.html'),name='event'),    #get news and event form database and dispaly it
    path('news&events/<int:pk>', views.newsView, name='event'),
    path('feedback/', views.feedback, name='feedback'), #feedback form url
    path('about/', views.about, name='about'),  #about url
    path('contact/', views.contact, name='contact'),    #contact us url
]
