from dataclasses import dataclass
from apps.lineas.repositories import LineaRepository


@dataclass
class GetLineaInput:
    id: int


@dataclass
class GetLineaOutput:
    id: int
    cliente_id: int
    cliente_razon_social: str
    linea_numero: int
    estado_linea: str
    fecha_instalacion: str


class GetLineaUseCase:
    def __init__(self, repository: LineaRepository):
        self.repository = repository

    def execute(self, data: GetLineaInput) -> GetLineaOutput | None:
        linea = self.repository.get_by_id(data.id)
        if not linea:
            return None
        return GetLineaOutput(
            id=linea.pk,
            cliente_id=linea.cliente_id,
            cliente_razon_social=linea.cliente.razon_social,
            linea_numero=linea.linea_numero,
            estado_linea=linea.estado_linea,
            fecha_instalacion=str(linea.fecha_instalacion) if linea.fecha_instalacion else None,
        )