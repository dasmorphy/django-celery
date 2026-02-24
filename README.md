# Django + DRF — Products API

## Stack
- Python 3.11+
- Django 5
- Django REST Framework
- PostgreSQL (via psycopg2)
- python-decouple (env vars)

## Arquitectura

```
apps/products/
├── controllers/       ← Recibe la request HTTP (equivale al Controller)
├── use_cases/         ← Lógica de negocio pura
├── repositories/      ← Acceso a base de datos
├── models.py          ← Modelos ORM de Django
└── urls.py            ← Ruteo
```

## Endpoint

| Método | URL             | Descripción          |
|--------|-----------------|----------------------|
| POST   | /api/products/  | Crea un producto     |

### Request body
```json
{
  "name": "Laptop",
  "price": 999.99,
  "stock": 10
}
```

### Response 201
```json
{
  "id": 1,
  "name": "Laptop",
  "price": 999.99,
  "stock": 10
}
```

## Setup

```bash
# 1. Clonar / descomprimir el proyecto
cd django_project

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales de Postgres

# 5. Crear la base de datos en Postgres
# CREATE DATABASE mydb;

# 6. Aplicar migraciones
python manage.py migrate

# 7. Correr el servidor
python manage.py runserver
```

## Notas sobre decisiones tomadas

- **"Controller" en Django**: Django no usa el patrón MVC clásico — su capa de presentación se llama *View*. Aquí se respetó el nombre `ProductController` extendiéndolo de `APIView` para mantener la intención arquitectónica sin romper la integración con DRF.
- **Serializers de DRF**: En un proyecto más grande lo correcto sería usar `serializers.Serializer` para validar el payload. Aquí se omitieron para mantener la separación de capas clara y que la validación sencilla viva en el use case. Si lo necesitás te lo agrego.
- **Inyección de dependencias**: El use case recibe el repository por constructor, lo que permite mockearlo fácilmente en tests sin frameworks externos.
