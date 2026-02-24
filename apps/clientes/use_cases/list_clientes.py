from dataclasses import dataclass
from typing import List
from apps.clientes.repositories import ClienteRepository
from apps.clientes.models import Cliente


@dataclass
class ListClientesInput:
    identificacion: str = None
    razon_social: str = None


@dataclass
class ClienteOutput:
    id: int
    identificacion: str
    razon_social: str
    email: str
    celular: str


class ListClientesUseCase:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    def execute(self, data: ListClientesInput) -> List[ClienteOutput]:
        clientes = self.repository.get_all(
            identificacion=data.identificacion,
            razon_social=data.razon_social,
        )
        return [
            ClienteOutput(
                id=c.pk,
                identificacion=c.identificacion,
                razon_social=c.razon_social,
                email=c.email,
                celular=c.celular,
            )
            for c in clientes
        ]