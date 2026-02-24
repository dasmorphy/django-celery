from apps.clientes.models import Cliente


class ClienteRepository:
    def get_all(self, identificacion=None, razon_social=None) -> list[Cliente]:
        queryset = Cliente.objects.filter(is_active=True)
        if identificacion:
            queryset = queryset.filter(identificacion__icontains=identificacion)
        if razon_social:
            queryset = queryset.filter(razon_social__icontains=razon_social)
        return list(queryset)

    def get_by_id(self, cliente_id: int) -> Cliente | None:
        return Cliente.objects.filter(pk=cliente_id, is_active=True).first()

    def create(self, identificacion: str, razon_social: str, email: str = None, celular: str = None) -> Cliente:
        return Cliente.objects.create(
            identificacion=identificacion,
            razon_social=razon_social,
            email=email,
            celular=celular,
        )

    def update(self, cliente: Cliente, **kwargs) -> Cliente:
        for key, value in kwargs.items():
            if hasattr(cliente, key):
                setattr(cliente, key, value)
        cliente.save()
        return cliente

    def delete(self, cliente: Cliente) -> None:
        cliente.is_active = False
        cliente.save()