from django.urls import path
from AnatoApp import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),

]