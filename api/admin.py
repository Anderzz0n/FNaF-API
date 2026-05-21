from django.contrib import admin
from .models import Personaje


@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_personaje', 'rol', 'juego_donde_sale', 'created_at']
    list_filter = ['rol', 'juego_donde_sale']
    search_fields = ['nombre_personaje', 'descripcion']
    filter_horizontal = ['variantes']
    readonly_fields = ['created_at', 'updated_at']
