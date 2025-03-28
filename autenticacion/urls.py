from django.urls import path
from .views import registro, inicio_sesion, cerrar_sesion

urlpatterns = [
    path('register/', registro, name='register'),
    path('login/', inicio_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]
