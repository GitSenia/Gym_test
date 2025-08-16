from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'gymHome/index.html')

def about(request):
    return render(request,'gymHome/abaut.html')

def service(request):
    return render(request,'gymHome/service.html')

def trainers(request):
    return render(request,'gymHome/trainers.html')

def equipment(request):
    return render(request,'gymHome/equipment.html')