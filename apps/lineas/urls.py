from django.urls import path
from apps.lineas.controllers import LineaListController, LineaDetailController

urlpatterns = [
    path('lineas/', LineaListController.as_view(), name='lineas-list'),
    path('lineas/<int:pk>/', LineaDetailController.as_view(), name='lineas-detail'),
]