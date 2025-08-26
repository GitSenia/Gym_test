from django.shortcuts import render



def main(request):
    return render(request,'main/main.html')

def equipment(request):
    return render(request,'main/equipment.html')
