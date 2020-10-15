from django.contrib import admin
from miaplicacion.models import HistoriaPaciente, FormulasPacientes
# Register your models here.

class HistoriaPacienteAdmin(admin.ModelAdmin):
    list_display = ("cedula", "nombre","apellido","telefono", "correo", "patologia", "remisiones")
    search_fields = ("cedula",)
    list_filter = ("cedula",)

class FormulasPacientesAdmin(admin.ModelAdmin):
    list_display = ("cedula", "fecha", "medicamento","cantidad", "dosis")
    search_fields = ("cedula",)
    list_filter = ("cedula",)

admin.site.register(HistoriaPaciente, HistoriaPacienteAdmin)
admin.site.register(FormulasPacientes, FormulasPacientesAdmin)

#modificacion de titulos y subtitulos
admin.site.site_header = 'Administracion medica'
admin.site.index_title = 'Rol Medico'
admin.site.site_title = 'Datos rol medico'