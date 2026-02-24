from dataclasses import dataclass
from typing import List
from apps.lineas.repositories import LineaRepository
from apps.lineas.models import LineaServicio


@dataclass
class ListLineasInput:
    cliente_id: int = None
    estado_linea: str = None


@dataclass
class LineaOutput:
    id: int
    cliente_id: int
    cliente_razon_social: str
    linea_numero: int
    estado_linea: str
    fecha_instalacion: str
    saldo_vencido: int


class ListLineasUseCase:
    def __init__(self, repository: LineaRepository):
        self.repository = repository

    def execute(self, data: ListLineasInput) -> List[LineaOutput]:
        lineas = self.repository.get_all(
            cliente_id=data.cliente_id,
            estado_linea=data.estado_linea,
        )
        return [
            LineaOutput(
                id=l.pk,
                cliente_id=l.cliente_id,
                cliente_razon_social=l.cliente.razon_social,
                linea_numero=l.linea_numero,
                estado_linea=l.estado_linea,
                saldo_vencido=l.saldo_vencido,
                fecha_instalacion=str(l.fecha_instalacion) if l.fecha_instalacion else None,
            )
            for l in lineas
        ]