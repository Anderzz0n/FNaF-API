"""
Script para poblar la base de datos con personajes de Five Nights at Freddy's.
Ejecutar con: python manage.py shell < seed_data.py
  o bien:     python seed_data.py  (desde la raíz del proyecto)
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fnaf_backend.settings')
django.setup()

from api.models import Personaje

Personaje.objects.all().delete()

personajes_data = [
    {
        'nombre_personaje': 'Freddy Fazbear',
        'descripcion': 'El animatrónico estrella de Freddy Fazbear\'s Pizza. Es un oso café con sombrero de copa y corbata que actúa como cantante principal de la banda.',
        'juego_donde_sale': 'Five Nights at Freddy\'s 1',
        'rol': 'cantante',
    },
    {
        'nombre_personaje': 'Bonnie the Bunny',
        'descripcion': 'Conejo animatrónico de color morado que toca la guitarra en la banda. Es uno de los animatrónicos más agresivos en la noche.',
        'juego_donde_sale': 'Five Nights at Freddy\'s 1',
        'rol': 'guitarrista',
    },
    {
        'nombre_personaje': 'Chica the Chicken',
        'descripcion': 'Pollo animatrónico amarillo que carga una pizza. Suele merodear la cocina y es la única animatrónica femenina original.',
        'juego_donde_sale': 'Five Nights at Freddy\'s 1',
        'rol': 'espectaculo',
    },
    {
        'nombre_personaje': 'Foxy the Pirate Fox',
        'descripcion': 'Zorro animatrónico con parche en el ojo y un gancho en lugar de mano. Se encuentra en Pirate Cove y ataca corriendo por el pasillo izquierdo.',
        'juego_donde_sale': 'Five Nights at Freddy\'s 1',
        'rol': 'espectaculo',
    },
    {
        'nombre_personaje': 'Golden Freddy',
        'descripcion': 'Versión dorada misteriosa de Freddy Fazbear. Aparece de forma aleatoria y su origen está lleno de misterio relacionado con los crímenes del local.',
        'juego_donde_sale': 'Five Nights at Freddy\'s 1',
        'rol': 'antagonista',
    },
    {
        'nombre_personaje': 'Withered Freddy',
        'descripcion': 'Versión deteriorada del Freddy original, almacenada en la trastienda de la segunda pizzería. Tiene el traje muy dañado y partes expuestas.',
        'juego_donde_sale': 'Five Nights at Freddy\'s 2',
        'rol': 'cantante',
    },
    {
        'nombre_personaje': 'Toy Freddy',
        'descripcion': 'Rediseño moderno y más colorido de Freddy para el nuevo local. Tiene mejillas rosadas y aspecto más amigable pero sigue siendo peligroso.',
        'juego_donde_sale': 'Five Nights at Freddy\'s 2',
        'rol': 'cantante',
    },
    {
        'nombre_personaje': 'Toy Bonnie',
        'descripcion': 'Versión renovada de Bonnie con aspecto brillante y moderno. A diferencia del original, tiene ojos azules y apariencia más plástica.',
        'juego_donde_sale': 'Five Nights at Freddy\'s 2',
        'rol': 'guitarrista',
    },
    {
        'nombre_personaje': 'The Puppet',
        'descripcion': 'La Marioneta es el animatrónico que habita en la caja de música. Es considerada la antagonista principal y está vinculada directamente con los asesinatos.',
        'juego_donde_sale': 'Five Nights at Freddy\'s 2',
        'rol': 'espectaculo',
    },
    {
        'nombre_personaje': 'Springtrap',
        'descripcion': 'El animatrónico más aterrador de la franquicia. Es el traje Spring Bonnie con los restos del asesino en serie William Afton atrapados en su interior.',
        'juego_donde_sale': 'Five Nights at Freddy\'s 3',
        'rol': 'antagonista',
    },
    {
        'nombre_personaje': 'Fredbear',
        'descripcion': 'El animatrónico original que precedió a Freddy Fazbear. Es de color dorado y usaba el mecanismo Spring Lock junto con Spring Bonnie.',
        'juego_donde_sale': 'Five Nights at Freddy\'s 4',
        'rol': 'cantante',
    },
    {
        'nombre_personaje': 'Circus Baby',
        'descripcion': 'Animatrónica femenina de aspecto circense creada por William Afton para su hija. Es la líder de los animatrónicos Sister Location y alberga el alma de Elizabeth Afton.',
        'juego_donde_sale': 'Five Nights at Freddy\'s: Sister Location',
        'rol': 'espectaculo',
    },
    {
        'nombre_personaje': 'Funtime Freddy',
        'descripcion': 'Versión de entretenimiento de Freddy diseñada para Sister Location. Lleva consigo a Bon-Bon, una marioneta de conejo en su mano derecha.',
        'juego_donde_sale': 'Five Nights at Freddy\'s: Sister Location',
        'rol': 'cantante',
    },
    {
        'nombre_personaje': 'Glamrock Freddy',
        'descripcion': 'La versión glam rock de Freddy de Mega Pizzaplex. A diferencia de otros animatrónicos, ayuda al protagonista Gregory y actúa como su aliado principal.',
        'juego_donde_sale': 'Five Nights at Freddy\'s: Security Breach',
        'rol': 'cantante',
    },
    {
        'nombre_personaje': 'Roxanne Wolf',
        'descripcion': 'Animatrónica lobo con aspecto punk y actitud arrogante. Canta y toca la guitarra en los shows del Mega Pizzaplex. Tiene miedo a perder su popularidad.',
        'juego_donde_sale': 'Five Nights at Freddy\'s: Security Breach',
        'rol': 'guitarrista',
    },
]

created = []
for data in personajes_data:
    p = Personaje.objects.create(**data)
    created.append(p)
    print(f"  ✓ Creado: {p.nombre_personaje}")

# Asignar variantes (personajes del mismo "linaje")
freddy = Personaje.objects.get(nombre_personaje='Freddy Fazbear')
withered_freddy = Personaje.objects.get(nombre_personaje='Withered Freddy')
toy_freddy = Personaje.objects.get(nombre_personaje='Toy Freddy')
glamrock_freddy = Personaje.objects.get(nombre_personaje='Glamrock Freddy')
golden_freddy = Personaje.objects.get(nombre_personaje='Golden Freddy')
fredbear = Personaje.objects.get(nombre_personaje='Fredbear')
funtime_freddy = Personaje.objects.get(nombre_personaje='Funtime Freddy')

freddy_variants = [withered_freddy, toy_freddy, glamrock_freddy, golden_freddy, fredbear, funtime_freddy]
for v in freddy_variants:
    freddy.variantes.add(v)

bonnie = Personaje.objects.get(nombre_personaje='Bonnie the Bunny')
toy_bonnie = Personaje.objects.get(nombre_personaje='Toy Bonnie')
bonnie.variantes.add(toy_bonnie)

print(f"\n✅ Seed completado: {len(created)} personajes creados")
print(f"   Variantes de Freddy: {freddy.variantes.count()}")
print(f"   Variantes de Bonnie: {bonnie.variantes.count()}")
