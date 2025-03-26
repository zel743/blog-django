from django.urls import path
from blog import views
from .views import linux_posts
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path('windows/', views.windows, name='windows'),  # Página de Windows
    # path('linux/', views.linux, name='linux'),   Página de Linux
    path('macos/', views.macos, name='macos'),  # Página de MacOS
    path('linux/', views.linux_posts, name='linux'),  # Muestra posts
    path('posting/', views.create_post, name='create_post'),  # Crear posts
    
    ]