from django.db import models


class Personaje(models.Model):
    ROL_CHOICES = [
        ('cantante', 'Cantante'),
        ('guitarrista', 'Guitarrista'),
        ('baterista', 'Baterista'),
        ('espectaculo', 'Espectáculo'),
        ('animatronic', 'Animatrónico'),
        ('seguridad', 'Seguridad'),
        ('antagonista', 'Antagonista'),
        ('ayudante', 'Ayudante'),
        ('otro', 'Otro'),
    ]

    nombre_personaje = models.CharField(max_length=150, verbose_name='Nombre del personaje')
    descripcion = models.TextField(verbose_name='Descripción')
    imagen = models.ImageField(
        upload_to='personajes/',
        null=True,
        blank=True,
        verbose_name='Imagen'
    )
    juego_donde_sale = models.CharField(max_length=200, verbose_name='Juego donde sale')
    rol = models.CharField(
        max_length=50,
        choices=ROL_CHOICES,
        default='animatronic',
        verbose_name='Rol'
    )
    variantes = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='variante_de',
        verbose_name='Variantes'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Personaje'
        verbose_name_plural = 'Personajes'
        ordering = ['nombre_personaje']

    def __str__(self):
        return self.nombre_personaje
