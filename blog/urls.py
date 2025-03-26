from django.urls import path,include
from blog import views
from .views import linux_posts
from .views import windows_posts
from .views import macos_posts
from .views import edit_post
from .views import delete_post
from .views import create_post
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path("index", views.index, name="index"),
    path('windows/', views.windows_posts, name='windows'),  # Página de Windows
    # path('linux/', views.linux, name='linux'),   Página de Linux
    path('macos/', views.macos_posts, name='macos'),  # Página de MacOS
    path('linux/', views.linux_posts, name='linux'),  # Muestra posts
    path('posting/', views.create_post, name='create_post'),  # Crear posts
    path('post/<int:post_id>/edit/', edit_post, name='edit_post'), # edita los post
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'), # elimina los posts
    path('api/', include(router.urls)),
    path('api/auth/login/', obtain_auth_token, name='api-login'),

        ]