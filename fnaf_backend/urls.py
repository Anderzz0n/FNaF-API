from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    """Punto de entrada principal de la API de Five Nights at Freddy's."""
    return Response({
        'mensaje': '🎃 Bienvenido a la API de Five Nights at Freddy\'s',
        'version': '1.0.0',
        'endpoints': {
            'personajes': reverse('personaje-list', request=request, format=format),
        },
        'documentacion': {
            'filtros_disponibles': ['nombre_personaje', 'juego_donde_sale', 'rol'],
            'ordenamiento_disponible': ['nombre_personaje', 'juego_donde_sale'],
            'busqueda_texto': '?search=<texto>',
            'paginacion': '?page=<n>&page_size=<n> (defecto: 3 por página)',
            'ejemplos': {
                'filtrar_por_rol': '?rol=cantante',
                'filtrar_por_juego': '?juego_donde_sale=fnaf 1',
                'ordenar_por_nombre': '?ordering=nombre_personaje',
                'ordenar_descendente': '?ordering=-juego_donde_sale',
                'pagina_personalizada': '?page=2&page_size=10',
            }
        }
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', api_root, name='api-root'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
