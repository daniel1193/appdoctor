from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'miaplicacion/home.html')

def asignar(request):
    return render(request,'miaplicacion/asigmedicos.html')

def mimedico(request):
    return rener(request, 'miaplicacion/mimedico.html')