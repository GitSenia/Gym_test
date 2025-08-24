from django.shortcuts import render
from .models import Services
# Create your views here.
def servis(request):
    context = Services.objects.all()
    return render(request, 'services/services.html' , context={'services':context})