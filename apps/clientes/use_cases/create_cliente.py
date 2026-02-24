from dataclasses import dataclass
from apps.clientes.repositories import ClienteRepository


@dataclass
class CreateClienteInput:
    identificacion: str
    razon_social: str
    email: str = None
    celular: str = None


@dataclass
class CreateClienteOutput:
    id: int
    identificacion: str
    razon_social: str
    email: str
    celular: str


class CreateClienteUseCase:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    def execute(self, data: CreateClienteInput) -> CreateClienteOutput:
        if not data.identificacion:
            raise ValueError("Identificación es requerido.")
        if not data.razon_social:
            raise ValueError("Razón social es requerido.")

        cliente = self.repository.create(
            identificacion=data.identificacion,
            razon_social=data.razon_social,
            email=data.email,
            celular=data.celular,
        )

        return CreateClienteOutput(
            id=cliente.pk,
            identificacion=cliente.identificacion,
            razon_social=cliente.razon_social,
            email=cliente.email,
            celular=cliente.celular,
        )