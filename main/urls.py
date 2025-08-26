
from django.urls import path
from . import views


urlpatterns = [

    path('', views.main, name='index'),

    path('equipment', views.equipment, name='machines'),

]