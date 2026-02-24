from dataclasses import dataclass
from apps.clientes.repositories import ClienteRepository


@dataclass
class DeleteClienteInput:
    id: int


class DeleteClienteUseCase:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    def execute(self, data: DeleteClienteInput) -> bool:
        cliente = self.repository.get_by_id(data.id)
        if not cliente:
            return False
        self.repository.delete(cliente)
        return True