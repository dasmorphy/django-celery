from django.db import models
from django.core.exceptions import ValidationError


class AuditDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        db_table = 'clientes'


class Cliente(AuditDateModel):
    identificacion = models.CharField(
        max_length=20,
        unique=True,
        db_index=True
    )
    razon_social = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    celular = models.CharField(max_length=30, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.razon_social} ({self.identificacion})"