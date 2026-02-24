from celery import shared_task
from django.utils import timezone
from django.db import transaction
from django.db.models import Sum, Q

from apps.lineas.models import LineaServicio
from apps.cobranza.models import CollectionsRequestLog, Rubro



@shared_task
def procesar_cobranza():
    now = timezone.now()

    # Solo líneas activas (soft delete)
    lineas = (
        LineaServicio.objects
        .filter(is_active=True)
        .exclude(estado_linea__in=["CANCELADO", "NO_INSTALADO"])
        .select_related("cliente")
    )

    for linea in lineas:

        log = CollectionsRequestLog.objects.create(
            linea_servicio=linea,
            started_at=now,
            status="SUCCESS",
            unpaid_count=0,
            action_taken="NONE"
        )

        try:
            with transaction.atomic():

                # rubros vencidos y no pagados
                rubros_vencidos = (
                    Rubro.objects.filter(
                        linea_servicio=linea,
                        estado_rubro="NO_PAGADO",
                        fecha_vencimiento__lt=now
                    )
                )

                unpaid_count = rubros_vencidos.count()

                total_vencido = rubros_vencidos.aggregate(
                    total=Sum("valor_total")
                )["total"] or 0

                # actualizar saldo solo si cambió (idempotencia)
                if linea.saldo_vencido != total_vencido:
                    linea.saldo_vencido = total_vencido

                action = "NONE"

                # regla de suspensión
                if unpaid_count > 0 and linea.estado_linea != "SUSPENDIDO":
                    linea.estado_linea = "SUSPENDIDO"
                    action = "SUSPEND"

                # regla de reactivación
                elif unpaid_count == 0 and linea.estado_linea == "SUSPENDIDO":
                    linea.estado_linea = "ACTIVO"
                    action = "UNSUSPEND"

                linea.save(update_fields=["saldo_vencido", "estado_linea"])

                log.unpaid_count = unpaid_count
                log.action_taken = action
                log.finished_at = timezone.now()
                log.save()

        except Exception as e:
            log.status = "FAILED"
            log.error_message = str(e)
            log.finished_at = timezone.now()
            log.save()