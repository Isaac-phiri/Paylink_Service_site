from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    
]
