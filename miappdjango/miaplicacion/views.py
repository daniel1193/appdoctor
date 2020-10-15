from django.shortcuts import render
from miaplicacion.models import Medico

# Create your views here.
def home(request):
    return render(request,'miaplicacion/home.html')

def asignar(request):
    return render(request,'miaplicacion/asigmedicos.html')

def mimedico(request):
    medicos = Medico.objects.filter()
    return render(request, 'miaplicacion/mimedico.html', {"medicos": medicos})

def admin(request):
    return render(request, admin.site.urls)
