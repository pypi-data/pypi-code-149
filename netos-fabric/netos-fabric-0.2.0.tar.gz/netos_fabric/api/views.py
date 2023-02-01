from .. import models
from .serializers import NetworkFabricSerializer
from netbox.api.viewsets import NetBoxModelViewSet


class NetworkFabricSViewSet(NetBoxModelViewSet):
    queryset = models.NetworkFabric.objects.all()
    serializer_class = NetworkFabricSerializer
