from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from apps.lineas.repositories import LineaRepository
from apps.lineas.use_cases import (
    GetLineaUseCase, GetLineaInput,
    UpdateLineaUseCase, UpdateLineaInput,
    DeleteLineaUseCase, DeleteLineaInput,
)


class LineaDetailController(APIView):
    def get(self, request: Request, pk: int) -> Response:
        use_case = GetLineaUseCase(repository=LineaRepository())
        result = use_case.execute(GetLineaInput(id=pk))

        if not result:
            return Response({'error': 'Linea no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            {
                'id': result.id,
                'cliente_id': result.cliente_id,
                'cliente_razon_social': result.cliente_razon_social,
                'linea_numero': result.linea_numero,
                'estado_linea': result.estado_linea,
                'fecha_instalacion': result.fecha_instalacion,
            },
            status=status.HTTP_200_OK,
        )

    def patch(self, request: Request, pk: int) -> Response:
        data = request.data

        try:
            use_case = UpdateLineaUseCase(repository=LineaRepository())
            result = use_case.execute(
                UpdateLineaInput(
                    id=pk,
                    cliente_id=int(data['cliente_id']) if 'cliente_id' in data else None,
                    linea_numero=int(data['linea_numero']) if 'linea_numero' in data else None,
                    estado_linea=data.get('estado_linea'),
                    fecha_instalacion=data.get('fecha_instalacion'),
                )
            )
        except (ValueError, TypeError) as exc:
            return Response({'error': str(exc)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if not result:
            return Response({'error': 'Linea no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            {
                'id': result.id,
                'cliente_id': result.cliente_id,
                'cliente_razon_social': result.cliente_razon_social,
                'linea_numero': result.linea_numero,
                'estado_linea': result.estado_linea,
                'fecha_instalacion': result.fecha_instalacion,
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request: Request, pk: int) -> Response:
        use_case = DeleteLineaUseCase(repository=LineaRepository())
        success = use_case.execute(DeleteLineaInput(id=pk))

        if not success:
            return Response({'error': 'Linea no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)