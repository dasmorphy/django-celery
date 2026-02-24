from dataclasses import dataclass
from apps.lineas.repositories import LineaRepository


@dataclass
class CreateLineaInput:
    cliente_id: int
    linea_numero: int
    estado_linea: str
    fecha_instalacion: str = None


@dataclass
class CreateLineaOutput:
    id: int
    cliente_id: int
    linea_numero: int
    estado_linea: str
    fecha_instalacion: str


class CreateLineaUseCase:
    def __init__(self, repository: LineaRepository):
        self.repository = repository

    def execute(self, data: CreateLineaInput) -> CreateLineaOutput:
        if not data.cliente_id:
            raise ValueError("Cliente ID es requerido.")
        if data.linea_numero <= 0:
            raise ValueError("Línea número debe ser positivo.")

        linea = self.repository.create(
            cliente_id=data.cliente_id,
            linea_numero=data.linea_numero,
            estado_linea=data.estado_linea,
            fecha_instalacion=data.fecha_instalacion,
        )

        return CreateLineaOutput(
            id=linea.pk,
            cliente_id=linea.cliente_id,
            linea_numero=linea.linea_numero,
            estado_linea=linea.estado_linea,
            fecha_instalacion=str(linea.fecha_instalacion) if linea.fecha_instalacion else None,
        )