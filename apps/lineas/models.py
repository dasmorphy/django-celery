from django.db import models
from django.core.exceptions import ValidationError
from apps.clientes.models import Cliente


class AuditDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        db_table = 'lineas'


class LineaServicio(AuditDateModel):

    class EstadoLinea(models.TextChoices):
        NO_INSTALADO = "NO_INSTALADO", "No instalado"
        ACTIVO = "ACTIVO", "Activo"
        SUSPENDIDO = "SUSPENDIDO", "Suspendido"
        CANCELADO = "CANCELADO", "Cancelado"

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="lineas"
    )

    linea_numero = models.PositiveSmallIntegerField()
    estado_linea = models.CharField(
        max_length=20,
        choices=EstadoLinea.choices
    )

    fecha_instalacion = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Línea {self.linea_numero} - {self.cliente.razon_social}"