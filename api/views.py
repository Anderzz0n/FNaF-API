from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Personaje
from .serializers import PersonajeSerializer, PersonajeImagenSerializer
from .filters import PersonajeFilter
from .pagination import CustomPageNumberPagination


class PersonajeViewSet(viewsets.ModelViewSet):
    """
    ViewSet para la gestión completa de personajes de Five Nights at Freddy's.

    list:        GET  /api/personajes/
    create:      POST /api/personajes/
    retrieve:    GET  /api/personajes/{id}/
    update:      PUT  /api/personajes/{id}/
    partial:     PATCH /api/personajes/{id}/
    destroy:     DELETE /api/personajes/{id}/
    imagen:      POST/DELETE /api/personajes/{id}/imagen/
    """
    queryset = Personaje.objects.prefetch_related('variantes').all()
    serializer_class = PersonajeSerializer
    pagination_class = CustomPageNumberPagination
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    # Filtros
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = PersonajeFilter

    # Ordenamiento: permitido por nombre y juego
    ordering_fields = ['nombre_personaje', 'juego_donde_sale']
    ordering = ['nombre_personaje']   # orden por defecto

    # Búsqueda de texto libre
    search_fields = ['nombre_personaje', 'descripcion', 'juego_donde_sale']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(
        detail=True,
        methods=['post', 'delete'],
        url_path='imagen',
        parser_classes=[MultiPartParser, FormParser],
        serializer_class=PersonajeImagenSerializer,
    )
    def imagen(self, request, pk=None):
        """
        POST   /api/personajes/{id}/imagen/  → Sube o reemplaza la imagen
        DELETE /api/personajes/{id}/imagen/  → Elimina la imagen
        """
        personaje = self.get_object()

        if request.method == 'POST':
            if 'imagen' not in request.FILES:
                return Response(
                    {'error': 'No se proporcionó ninguna imagen. Usa el campo "imagen".'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            # Eliminar imagen anterior si existe
            if personaje.imagen:
                personaje.imagen.delete(save=False)

            serializer = PersonajeImagenSerializer(
                personaje,
                data=request.data,
                partial=True,
                context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            if not personaje.imagen:
                return Response(
                    {'error': 'Este personaje no tiene imagen registrada.'},
                    status=status.HTTP_404_NOT_FOUND
                )
            personaje.imagen.delete(save=True)
            return Response(
                {'mensaje': f'Imagen de "{personaje.nombre_personaje}" eliminada correctamente.'},
                status=status.HTTP_200_OK
            )
