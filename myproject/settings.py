from decouple import config
from celery.schedules import crontab

SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-me')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'rest_framework',
    'apps.clientes',
    'apps.lineas',
    "apps.cobranza",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='mydb'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default='postgres'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}
CELERY_BROKER_URL = config('CELERY_BROKER_URL', default='redis://localhost:6379/0'),

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_BACKEND = config('CELERY_BROKER_URL', default='redis://localhost:6379/0'),

CELERY_TIMEZONE = "UTC"

CELERY_BEAT_SCHEDULE = {
    "cobranza-cada-5-minutos": {
        "task": "apps.cobranza.tasks.procesar_cobranza",
        "schedule": crontab(minute="*/5"),
    }
}
