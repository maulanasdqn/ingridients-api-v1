from django.urls import path
from . import views

urlpatterns = [
    path('', views.Ingridients, name="Ingridients")        
]


