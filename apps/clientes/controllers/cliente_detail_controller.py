from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from apps.clientes.repositories import ClienteRepository
from apps.clientes.use_cases import (
    GetClienteUseCase, GetClienteInput,
    UpdateClienteUseCase, UpdateClienteInput,
    DeleteClienteUseCase, DeleteClienteInput,
)


class ClienteDetailController(APIView):
    def get(self, request: Request, pk: int) -> Response:
        use_case = GetClienteUseCase(repository=ClienteRepository())
        result = use_case.execute(GetClienteInput(id=pk))

        if not result:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            {
                'id': result.id,
                'identificacion': result.identificacion,
                'razon_social': result.razon_social,
                'email': result.email,
                'celular': result.celular,
            },
            status=status.HTTP_200_OK,
        )

    def patch(self, request: Request, pk: int) -> Response:
        data = request.data

        try:
            use_case = UpdateClienteUseCase(repository=ClienteRepository())
            result = use_case.execute(
                UpdateClienteInput(
                    id=pk,
                    identificacion=data.get('identificacion'),
                    razon_social=data.get('razon_social'),
                    email=data.get('email'),
                    celular=data.get('celular'),
                )
            )
        except (ValueError, TypeError) as exc:
            return Response({'error': str(exc)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if not result:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            {
                'id': result.id,
                'identificacion': result.identificacion,
                'razon_social': result.razon_social,
                'email': result.email,
                'celular': result.celular,
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request: Request, pk: int) -> Response:
        use_case = DeleteClienteUseCase(repository=ClienteRepository())
        success = use_case.execute(DeleteClienteInput(id=pk))

        if not success:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)