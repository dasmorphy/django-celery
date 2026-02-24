from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from apps.lineas.repositories import LineaRepository
from apps.lineas.use_cases import (
    CreateLineaUseCase, CreateLineaInput,
    ListLineasUseCase, ListLineasInput,
)


class LineaListController(APIView):
    def get(self, request: Request) -> Response:
        cliente_id = request.query_params.get('cliente_id')
        estado_linea = request.query_params.get('estado_linea')

        use_case = ListLineasUseCase(repository=LineaRepository())
        result = use_case.execute(
            ListLineasInput(
                cliente_id=int(cliente_id) if cliente_id else None,
                estado_linea=estado_linea,
            )
        )

        data = [
            {
                'id': r.id,
                'cliente_id': r.cliente_id,
                'cliente_razon_social': r.cliente_razon_social,
                'linea_numero': r.linea_numero,
                'estado_linea': r.estado_linea,
                'fecha_instalacion': r.fecha_instalacion,
                'saldo_vencido': r.saldo_vencido,
            }
            for r in result
        ]
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        data = request.data

        required_fields = ['cliente_id', 'linea_numero', 'estado_linea']
        missing = [f for f in required_fields if f not in data]
        if missing:
            return Response(
                {'error': f"Parametros requeridos: {', '.join(missing)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            use_case = CreateLineaUseCase(repository=LineaRepository())
            result = use_case.execute(
                CreateLineaInput(
                    cliente_id=int(data['cliente_id']),
                    linea_numero=int(data['linea_numero']),
                    estado_linea=data['estado_linea'],
                    fecha_instalacion=data.get('fecha_instalacion'),
                )
            )
        except (ValueError, TypeError) as exc:
            return Response({'error': str(exc)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response(
            {
                'id': result.id,
                'cliente_id': result.cliente_id,
                'linea_numero': result.linea_numero,
                'estado_linea': result.estado_linea,
                'fecha_instalacion': result.fecha_instalacion,
            },
            status=status.HTTP_201_CREATED,
        )