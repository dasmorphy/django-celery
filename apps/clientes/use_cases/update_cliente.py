from dataclasses import dataclass
from apps.clientes.repositories import ClienteRepository


@dataclass
class UpdateClienteInput:
    id: int
    identificacion: str = None
    razon_social: str = None
    email: str = None
    celular: str = None


@dataclass
class UpdateClienteOutput:
    id: int
    identificacion: str
    razon_social: str
    email: str
    celular: str


class UpdateClienteUseCase:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    def execute(self, data: UpdateClienteInput) -> UpdateClienteOutput | None:
        cliente = self.repository.get_by_id(data.id)
        if not cliente:
            return None

        update_data = {}
        if data.identificacion is not None:
            update_data['identificacion'] = data.identificacion
        if data.razon_social is not None:
            update_data['razon_social'] = data.razon_social
        if data.email is not None:
            update_data['email'] = data.email
        if data.celular is not None:
            update_data['celular'] = data.celular

        cliente = self.repository.update(cliente, **update_data)

        return UpdateClienteOutput(
            id=cliente.pk,
            identificacion=cliente.identificacion,
            razon_social=cliente.razon_social,
            email=cliente.email,
            celular=cliente.celular,
        )