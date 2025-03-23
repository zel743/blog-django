from django.urls import path
from .views import registro, inicio_sesion, cerrar_sesion

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', inicio_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]
