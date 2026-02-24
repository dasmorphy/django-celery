from dataclasses import dataclass
from apps.lineas.repositories import LineaRepository


@dataclass
class UpdateLineaInput:
    id: int
    cliente_id: int = None
    linea_numero: int = None
    estado_linea: str = None
    fecha_instalacion: str = None


@dataclass
class UpdateLineaOutput:
    id: int
    cliente_id: int
    cliente_razon_social: str
    linea_numero: int
    estado_linea: str
    fecha_instalacion: str


class UpdateLineaUseCase:
    def __init__(self, repository: LineaRepository):
        self.repository = repository

    def execute(self, data: UpdateLineaInput) -> UpdateLineaOutput | None:
        linea = self.repository.get_by_id(data.id)
        if not linea:
            return None

        update_data = {}
        if data.cliente_id is not None:
            update_data['cliente_id'] = data.cliente_id
        if data.linea_numero is not None:
            update_data['linea_numero'] = data.linea_numero
        if data.estado_linea is not None:
            update_data['estado_linea'] = data.estado_linea
        if data.fecha_instalacion is not None:
            update_data['fecha_instalacion'] = data.fecha_instalacion

        linea = self.repository.update(linea, **update_data)

        return UpdateLineaOutput(
            id=linea.pk,
            cliente_id=linea.cliente_id,
            cliente_razon_social=linea.cliente.razon_social,
            linea_numero=linea.linea_numero,
            estado_linea=linea.estado_linea,
            fecha_instalacion=str(linea.fecha_instalacion) if linea.fecha_instalacion else None,
        )