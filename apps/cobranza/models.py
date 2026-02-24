
from django.db import models

from apps.lineas.models import LineaServicio


class CollectionsRequestLog(models.Model):

    class Status(models.TextChoices):
        SUCCESS = "SUCCESS", "Success"
        FAILED = "FAILED", "Failed"

    class ActionTaken(models.TextChoices):
        NONE = "NONE", "None"
        SUSPEND = "SUSPEND", "Suspend"
        UNSUSPEND = "UNSUSPEND", "Unsuspend"

    linea_servicio = models.ForeignKey(
        LineaServicio,
        on_delete=models.PROTECT,
        related_name="collection_logs"
    )

    started_at = models.DateTimeField()
    finished_at = models.DateTimeField(null=True, blank=True)

    status = models.CharField(
        max_length=10,
        choices=Status.choices
    )

    unpaid_count = models.PositiveSmallIntegerField()

    action_taken = models.CharField(
        max_length=20,
        choices=ActionTaken.choices,
        null=True,
        blank=True
    )

    error_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Log línea {self.linea_servicio_id} - {self.status}"
    
class Rubro(models.Model):

    class EstadoRubro(models.TextChoices):
        NO_PAGADO = "NO_PAGADO", "No pagado"
        PAGADO = "PAGADO", "Pagado"
        VENCIDO = "VENCIDO", "Vencido"
        ANULADO = "ANULADO", "Anulado"

    linea_servicio = models.ForeignKey(
        LineaServicio,
        on_delete=models.PROTECT,
        related_name="rubros"
    )

    valor_total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estado_rubro = models.CharField(
        max_length=20,
        choices=EstadoRubro.choices,
        default=EstadoRubro.NO_PAGADO
    )

    fecha_emision = models.DateTimeField()
    fecha_vencimiento = models.DateTimeField()
    fecha_pago = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Rubro {self.id} - Línea {self.linea_servicio_id}"