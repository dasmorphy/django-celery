from apps.lineas.models import LineaServicio


class LineaRepository:
    def get_all(self, cliente_id=None, estado_linea=None) -> list[LineaServicio]:
        queryset = LineaServicio.objects.filter(is_active=True).select_related('cliente')
        if cliente_id:
            queryset = queryset.filter(cliente_id=cliente_id)
        if estado_linea:
            queryset = queryset.filter(estado_linea=estado_linea)
        return list(queryset)

    def get_by_id(self, linea_id: int) -> LineaServicio | None:
        return LineaServicio.objects.filter(pk=linea_id, is_active=True).select_related('cliente').first()

    def create(self, cliente_id: int, linea_numero: int, estado_linea: str, fecha_instalacion=None) -> LineaServicio:
        from apps.clientes.models import Cliente
        cliente = Cliente.objects.get(pk=cliente_id)
        return LineaServicio.objects.create(
            cliente=cliente,
            linea_numero=linea_numero,
            estado_linea=estado_linea,
            fecha_instalacion=fecha_instalacion,
        )

    def update(self, linea: LineaServicio, **kwargs) -> LineaServicio:
        for key, value in kwargs.items():
            if hasattr(linea, key):
                setattr(linea, key, value)
        linea.save()
        return linea

    def delete(self, linea: LineaServicio) -> None:
        linea.is_active = False
        linea.save()