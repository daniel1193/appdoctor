from django.db import models

# Create your models here.

class Medico(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField()
    especialidad=models.CharField(max_length=45)

class HistoriaPaciente(models.Model):
    cedula=models.IntegerField(max_length=None)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=50)
    telefono=models.IntegerField(max_length=None)
    correo=models.EmailField()
    patologia=models.CharField(max_length=50)
    remisiones = models.CharField(max_length=80)

class FormulasPacientes(models.Model):
    cedula = models.IntegerField(max_length = None)
    fecha = models.DateField()
    medicamento = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=30)
    dosis = models.CharField(max_length=30)


class MedicosDisponibles(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField()
    especialidad=models.CharField(max_length=45)
    telefono = models.CharField(max_length = 15)