from django.urls import path
from .views import home, asignar, mimedico, formula

urlpatterns = [
    path('', home, name="home"),
    path('asignar',asignar, name="asignar"),
    path('mimedico', mimedico, name="mimedico"),
    path('formula',formula, name="formula"),
]