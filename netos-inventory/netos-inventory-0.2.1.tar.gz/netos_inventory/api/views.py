from netbox.api.viewsets import NetBoxModelViewSet
from .. import filtersets, models
from . import serializers


class ReconDeviceViewSet(NetBoxModelViewSet):
    queryset = models.ReconDevice.objects.all()
    serializer_class = serializers.ReconDeviceSerializer


class ReconModuleViewSet(NetBoxModelViewSet):
    queryset = models.ReconModule.objects.all()
    serializer_class = serializers.ReconModuleSerializer


class ReconInventoryItemViewSet(NetBoxModelViewSet):
    queryset = models.ReconInventoryItem.objects.all()
    serializer_class = serializers.ReconInventoryItemSerializer


class VRFDetectedViewSet(NetBoxModelViewSet):
    queryset = models.VRFDetected.objects.all()
    serializer_class = serializers.VRFDetectedSerializer
