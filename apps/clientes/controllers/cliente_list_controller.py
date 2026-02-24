from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from apps.clientes.repositories import ClienteRepository
from apps.clientes.use_cases import (
    CreateClienteUseCase, CreateClienteInput,
    ListClientesUseCase, ListClientesInput,
)


class ClienteListController(APIView):
    def get(self, request: Request) -> Response:
        identificacion = request.query_params.get('identificacion')
        razon_social = request.query_params.get('razon_social')

        use_case = ListClientesUseCase(repository=ClienteRepository())
        result = use_case.execute(
            ListClientesInput(
                identificacion=identificacion,
                razon_social=razon_social,
            )
        )

        data = [
            {
                'id': r.id,
                'identificacion': r.identificacion,
                'razon_social': r.razon_social,
                'email': r.email,
                'celular': r.celular,
            }
            for r in result
        ]
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        data = request.data

        required_fields = ['identificacion', 'razon_social']
        missing = [f for f in required_fields if f not in data]
        if missing:
            return Response(
                {'error': f"Parametros requeridos: {', '.join(missing)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            use_case = CreateClienteUseCase(repository=ClienteRepository())
            result = use_case.execute(
                CreateClienteInput(
                    identificacion=data['identificacion'],
                    razon_social=data['razon_social'],
                    email=data.get('email'),
                    celular=data.get('celular'),
                )
            )
        except (ValueError, TypeError) as exc:
            return Response({'error': str(exc)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response(
            {
                'id': result.id,
                'identificacion': result.identificacion,
                'razon_social': result.razon_social,
                'email': result.email,
                'celular': result.celular,
            },
            status=status.HTTP_201_CREATED,
        )