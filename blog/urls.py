from django.urls import path

from .. import views

urlpatterns = [
    path("index", views.index, name="index"),
    path('windows/', views.windows, name='windows'),  # Página de Windows
    path('linux/', views.linux, name='linux'),  # Página de Linux
    path('macos/', views.macos, name='macos'),  # Página de MacOS
]