from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonajeViewSet

router = DefaultRouter()
router.register(r'personajes', PersonajeViewSet, basename='personaje')

urlpatterns = [
    path('', include(router.urls)),
]
