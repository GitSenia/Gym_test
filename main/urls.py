
from django.urls import path
from . import views


urlpatterns = [

    path('', views.main, name='index'),

    path('machines/<int:m_id>', views.equipment_detail, name='machin'),
    path('machines', views.equipment, name='machines'),

    path('services', views.servis, name='servis'),

]