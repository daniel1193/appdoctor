from django.urls import path
from .views import home, asignar, mimedico, admin

urlpatterns = [
    path('', home, name="home"),
    path('asignar',asignar, name="asignar"),
    path('mimedico', mimedico, name="mimedico"),
    path('admin',admin,name="admin"),
]