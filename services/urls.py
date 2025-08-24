from django.urls import path
from . import views

urlpatterns = [

    path('servis', views.servis, name='servis'),

]