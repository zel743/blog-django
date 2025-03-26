from django.urls import path
from blog import views
from .views import linux_posts
from .views import windows_posts
from .views import macos_posts
from .views import edit_post
from .views import delete_post
from .views import create_post

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path('windows/', views.windows_posts, name='windows'),  # Página de Windows
    # path('linux/', views.linux, name='linux'),   Página de Linux
    path('macos/', views.macos_posts, name='macos'),  # Página de MacOS
    path('linux/', views.linux_posts, name='linux'),  # Muestra posts
    path('posting/', views.create_post, name='create_post'),  # Crear posts
    path('post/<int:post_id>/edit/', edit_post, name='edit_post'), # edita los post
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'), # elimina los posts

        ]