# Django + DRF — Products API

## Stack
- Python 3.11+
- Django 5
- Django REST Framework
- PostgreSQL (via psycopg2)
- python-decouple (env vars)
- python-decouple (env vars)
- Redis

## Estructura del proyecto

```
apps/products/
├── controllers/       ← Recibe la request HTTP
├── use_cases/         ← Lógica de negocio pura
├── repositories/      ← Acceso a base de datos
├── models.py          ← Modelos ORM de Django
└── urls.py            ← Ruteo
```

## Endpoint

| Método | URL             | Descripción          |
|--------|-----------------|----------------------|
| GET   | /api/clientes  | Listar todos los clientes    |
| POST   | /api/clientes/  | Crea un cliente     |
| GET   | /api/clientes/{id}/  | Busca cliente por id     |
| PATCH   | /api/clientes/{id}/  | Actualiza parcialmente un cliente     |
| DELETE   | /api/clientes/{id}/  | Eliminacion logica de un cliente     |
| GET   | /api/lineas/  | Lista las lineas del cliente     |
| POST   | /api/lineas/  | Crea una linea     |
| POST   | /api/lineas/{id}/  | Obtiene una linea por su id     |
| PATCH   | /api/lineas/{id}/  | Actualiza parcialmente una linea     |
| DELETE   | /api/lineas/{id}/  | Eliminación lógica de una linea     |
| POST   | /api/products/  | Crea un producto     |
| POST   | /api/products/  | Crea un producto     |
| POST   | /api/products/  | Crea un producto     |
| POST   | /api/products/  | Crea un producto     |
| POST   | /api/products/  | Crea un producto     |
| POST   | /api/products/  | Crea un producto     |
| POST   | /api/products/  | Crea un producto     |
| POST   | /api/products/  | Crea un producto     |

### Request body new line
```json
{
  "cliente_id": 2,
  "cliente_razon_social": "test",
  "linea_numero": "1",
  "estado_linea": "activo"
}
```

### Response 201
```json
{
  "id": 1,
  "cliente_id": 1,
  "cliente_razon_social": "test",
  "linea_numero": 1,
  "estado_linea": "activo",
  "fecha_instalacion": null,
  "saldo_vencido": 0.0
}
```

### Request body new client
```json
{
  "identificacion": "2",
  "razon_social": "test",
  "email": "test@hotmail.com",
  "celular": "0999222"
}
```

### Response 201
```json
{
  "id": 1,
  "identificacion": "1",
  "razon_social": "test",
  "email": "test@hotmail.com",
  "celular": "0999222"
}
```

## Despliegue local

```bash
# 1. Clonar / descomprimir el proyecto
cd django_celery

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

## Despliegue docker
```bash
# 1. Levantar contenedores
docker compose up --build
```


## Env de ejemplo
```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=1234
DB_HOST=localhost
DB_PORT=5432
CELERY_BROKER_URL=redis://redis:6379/0
```

