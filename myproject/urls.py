from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.clientes.urls')),
    path('api/', include('apps.lineas.urls')),
]
