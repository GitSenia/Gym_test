from django.shortcuts import render
from .models import Equipment,Services


def main(request):
    return render(request,'main/main.html')

def equipment(request):

    context = Equipment.objects.all()
    return render(request,'main/equipment.html',context={'machines':context})

def equipment_detail(request,m_id):
    context = Equipment.objects.get(id=m_id)
    return render(request,'main/equipment_id.html',context={'machine':context})

def servis(request):
    context = Services.objects.all()
    return render(request,'main/servicees.html',context={'services':context})
