from dataclasses import dataclass
from apps.clientes.repositories import ClienteRepository


@dataclass
class GetClienteInput:
    id: int


@dataclass
class GetClienteOutput:
    id: int
    identificacion: str
    razon_social: str
    email: str
    celular: str


class GetClienteUseCase:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    def execute(self, data: GetClienteInput) -> GetClienteOutput | None:
        cliente = self.repository.get_by_id(data.id)
        if not cliente:
            return None
        return GetClienteOutput(
            id=cliente.pk,
            identificacion=cliente.identificacion,
            razon_social=cliente.razon_social,
            email=cliente.email,
            celular=cliente.celular,
        )