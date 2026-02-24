from django.urls import path
from apps.clientes.controllers import ClienteListController, ClienteDetailController

urlpatterns = [
    path('clientes/', ClienteListController.as_view(), name='clientes-list'),
    path('clientes/<int:pk>/', ClienteDetailController.as_view(), name='clientes-detail'),
]