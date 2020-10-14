from django.urls import path
from .views import home, asignar

urlpatterns = [
    path('', home, name="home"),
    path('asignar',asignar, name="asignar")
]