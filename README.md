# 🎃 Five Nights at Freddy's API

API REST desarrollada con **Django + Django REST Framework** para la gestión de personajes de Five Nights at Freddy's.

---

##  Instalación

```bash
# 1. Clonar el proyecto y entrar al directorio
cd fnaf_backend

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py migrate

# 5. (Opcional) Poblar con datos de ejemplo
python seed_data.py

# 6. Iniciar servidor
python manage.py runserver
```

La API queda disponible en: `http://localhost:8000/api/`

---

## Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/personajes/` | Listar personajes (paginado) |
| POST | `/api/personajes/` | Crear personaje |
| GET | `/api/personajes/{id}/` | Detalle de personaje |
| PUT | `/api/personajes/{id}/` | Actualizar personaje completo |
| PATCH | `/api/personajes/{id}/` | Actualizar personaje parcial |
| DELETE | `/api/personajes/{id}/` | Eliminar personaje |
| POST | `/api/personajes/{id}/imagen/` | Subir/reemplazar imagen |
| DELETE | `/api/personajes/{id}/imagen/` | Eliminar imagen |

---

## Filtros disponibles

```
GET /api/personajes/?nombre_personaje=freddy
GET /api/personajes/?juego_donde_sale=fnaf 2
GET /api/personajes/?rol=cantante
```

### Roles válidos
`cantante` | `guitarrista` | `baterista` | `espectaculo` | `animatronic` | `seguridad` | `antagonista` | `ayudante` | `otro`

---

## Ordenamiento

```
GET /api/personajes/?ordering=nombre_personaje       # A → Z
GET /api/personajes/?ordering=-nombre_personaje      # Z → A
GET /api/personajes/?ordering=juego_donde_sale
GET /api/personajes/?ordering=-juego_donde_sale
```

---

##  Paginación

```
GET /api/personajes/                    # Página 1, 3 resultados (defecto)
GET /api/personajes/?page=2             # Página 2
GET /api/personajes/?page_size=10       # 10 resultados por página
GET /api/personajes/?page=2&page_size=5 # Página 2, 5 resultados
```

### Respuesta paginada
```json
{
  "pagination": {
    "count": 15,
    "total_pages": 5,
    "current_page": 1,
    "page_size": 3,
    "next": "http://localhost:8000/api/personajes/?page=2",
    "previous": null
  },
  "results": [...]
}
```

---

## Gestión de imágenes

```bash
# Subir imagen (multipart/form-data)
curl -X POST http://localhost:8000/api/personajes/1/imagen/ \
     -F "imagen=@freddy.png"

# Eliminar imagen
curl -X DELETE http://localhost:8000/api/personajes/1/imagen/
```

---

## Estructura del proyecto

```
fnaf_backend/
├── requirements.txt
├── seed_data.py
├── manage.py
├── README.md
├── media/                      ← imágenes subidas
│   └── personajes/
├── fnaf_backend/
│   ├── settings.py
│   └── urls.py
└── api/
    ├── models.py               ← Modelo Personaje
    ├── serializers.py          ← Serializers (completo y de imagen)
    ├── views.py                ← ViewSet con acciones extra
    ├── filters.py              ← Filtros: nombre, juego, rol
    ├── pagination.py           ← Paginación personalizada
    ├── urls.py                 ← Router DRF
    └── admin.py                ← Panel admin
```

---

##  Ejemplo: Crear personaje con variantes

```bash
curl -X POST http://localhost:8000/api/personajes/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre_personaje": "Shadow Freddy",
    "descripcion": "Versión sombría misteriosa de Freddy.",
    "juego_donde_sale": "Five Nights at Freddys 2",
    "rol": "antagonista",
    "variantes": [1, 6, 7]
  }'
```
