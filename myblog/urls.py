"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from blog import views
from django.conf import settings
from django.conf.urls.static import static


# by default the URLs add / at the beginning
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('windows/', views.windows_posts, name='windows'),
    path('linux/', views.linux_posts, name='linux'),
    path('macos/', views.macos_posts, name='macos'),
    path('', include('autenticacion.urls')),
    path('posting/', views.create_post, name='create_post'),
    path('', include('blog.urls')),
    
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Para servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)