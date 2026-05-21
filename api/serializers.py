from rest_framework import serializers
from .models import Personaje


class PersonajeSimpleSerializer(serializers.ModelSerializer):
    """Serializer simplificado para mostrar variantes sin recursión infinita."""
    class Meta:
        model = Personaje
        fields = ['id', 'nombre_personaje', 'rol', 'juego_donde_sale', 'imagen']


class PersonajeSerializer(serializers.ModelSerializer):
    variantes_detalle = PersonajeSimpleSerializer(
        source='variantes',
        many=True,
        read_only=True
    )
    variantes = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Personaje.objects.all(),
        required=False
    )
    imagen_url = serializers.SerializerMethodField()
    rol_display = serializers.CharField(source='get_rol_display', read_only=True)

    class Meta:
        model = Personaje
        fields = [
            'id',
            'nombre_personaje',
            'descripcion',
            'imagen',
            'imagen_url',
            'juego_donde_sale',
            'rol',
            'rol_display',
            'variantes',
            'variantes_detalle',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_imagen_url(self, obj):
        request = self.context.get('request')
        if obj.imagen and request:
            return request.build_absolute_uri(obj.imagen.url)
        return None


class PersonajeImagenSerializer(serializers.ModelSerializer):
    """Serializer exclusivo para subir/actualizar la imagen del personaje."""
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = Personaje
        fields = ['id', 'nombre_personaje', 'imagen', 'imagen_url']
        read_only_fields = ['id', 'nombre_personaje']

    def get_imagen_url(self, obj):
        request = self.context.get('request')
        if obj.imagen and request:
            return request.build_absolute_uri(obj.imagen.url)
        return None
