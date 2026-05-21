import django_filters
from .models import Personaje


class PersonajeFilter(django_filters.FilterSet):
    # Filtro exacto e insensible a mayúsculas por nombre
    nombre_personaje = django_filters.CharFilter(
        field_name='nombre_personaje',
        lookup_expr='icontains',
        label='Nombre del personaje (contiene)'
    )
    # Filtro exacto por juego
    juego_donde_sale = django_filters.CharFilter(
        field_name='juego_donde_sale',
        lookup_expr='icontains',
        label='Juego donde sale (contiene)'
    )
    # Filtro exacto por rol (usa los choices definidos)
    rol = django_filters.ChoiceFilter(
        choices=Personaje.ROL_CHOICES,
        label='Rol'
    )

    class Meta:
        model = Personaje
        fields = ['nombre_personaje', 'juego_donde_sale', 'rol']
