from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import UserListCreateView, UserDetailView
router = DefaultRouter()
router.register(r'users', UserViewSet)  # Crea las rutas CRUD automáticamente

urlpatterns = [
    path('api/', include(router.urls)),
]

