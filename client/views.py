from rest_framework import viewsets,filters
from client.models import Client
from .serializers import ClientSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ClientViewSet(viewsets.ModelViewSet):
    """Exibindo lista de clientes"""

    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','email','cpf']
    filterset_fields = ['ativo']



