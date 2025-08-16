from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/about', views.about, name='about'),
    path('/service', views.service, name='service'),
    path('/trainers', views.trainers, name='trainers'),
    path('/equipment', views.equipment, name='equipment'),

]