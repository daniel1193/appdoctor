from django.shortcuts import render
from miaplicacion.models import Medico, MedicosDisponibles, FormulasPacientes

# Create your views here.
def home(request):
    return render(request,'miaplicacion/home.html')

def asignar(request):
    medicosdispo = MedicosDisponibles.objects.filter()
    return render(request,'miaplicacion/asigmedicos.html', {"medicosdispo":medicosdispo})

def mimedico(request):
    medicos = Medico.objects.filter()
    return render(request, 'miaplicacion/mimedico.html', {"medicos": medicos})

def formula(request):
    formulas = FormulasPacientes.objects.filter()
    return render(request, 'miaplicacion/miformula.html',{"formulas": formulas})