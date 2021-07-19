from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
   path('', views.index, name='home'),
   path('', views.about, name='about'),
   path('', views.contact, name='contact'),

   
]