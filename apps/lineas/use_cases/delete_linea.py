from dataclasses import dataclass
from apps.lineas.repositories import LineaRepository


@dataclass
class DeleteLineaInput:
    id: int


class DeleteLineaUseCase:
    def __init__(self, repository: LineaRepository):
        self.repository = repository

    def execute(self, data: DeleteLineaInput) -> bool:
        linea = self.repository.get_by_id(data.id)
        if not linea:
            return False
        self.repository.delete(linea)
        return True