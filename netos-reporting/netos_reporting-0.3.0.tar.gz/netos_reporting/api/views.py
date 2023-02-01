import logging
from . import serializers
from .. import filtersets, models
from netbox.api.viewsets import NetBoxModelViewSet
from django.conf import settings
from django.db.models import F, Q, Case, When, FloatField
from django.db.models.functions import JSONObject
from django.db.models import BooleanField, ExpressionWrapper, Q
from dcim.models.devices import Device, InventoryItem, Module
from django.db import DatabaseError, transaction
from netbox.api.viewsets import NetBoxModelViewSet
from rest_framework import status
from rest_framework.response import Response

config = settings.PLUGINS_CONFIG["netos_reporting"]


class NetosSoftwareReportViewSet(NetBoxModelViewSet):
    detected_name = config["software_fields"]["detected_software"]
    current_name = config["software_fields"]["current_software"]
    std_name = config["software_fields"]["standard_software"]

    queryset = models.NetosSoftwareReport.objects.all()

    serializer_class = serializers.NetosSoftwareReportSerializer
    filterset_class = filtersets.NetosSoftwareReportFilterSet

    def get_queryset(self):
        detected_name = config["software_fields"]["detected_software"]
        current_name = config["software_fields"]["current_software"]
        std_name = config["software_fields"]["standard_software"]

        return models.NetosSoftwareReport.objects.annotate(
            compliance=Case(
                When(
                    Q(**{f'custom_field_data__{current_name}': None}),
                    then=None
                ),
                default=ExpressionWrapper(
                    Q(custom_field_data__contains=JSONObject(**{current_name: F(f'custom_field_data__{detected_name}')})) |
                    Q(custom_field_data__contains=JSONObject(
                        **{current_name: F(f'custom_field_data__{std_name}')})),
                    output_field=BooleanField()))
        )

##
# Report
##


class NetosEoLReportDeviceViewSet(NetBoxModelViewSet):
    queryset = models.NetosEoLReportDevice.objects.all()
    serializer_class = serializers.NetosEoLReportDeviceSerializer


class NetosEoLReportModuleViewSet(NetBoxModelViewSet):
    queryset = models.NetosEoLReportModule.objects.all()
    serializer_class = serializers.NetosEoLReportModuleSerializer


class NetosEoLReportInventoryViewSet(NetBoxModelViewSet):
    queryset = models.NetosEoLReportInventory.objects.all()
    serializer_class = serializers.NetosEoLReportInventorySerializer


##
# Summary
##


class NetosSummaryDeviceViewSet(NetBoxModelViewSet):
    def paginate_queryset(self, queryset):
        return None
    queryset = models.NetosEoLReportDevice.objects.all()
    serializer_class = serializers.NetosSummaryDeviceSerializer


class NetosSummaryModuleViewSet(NetBoxModelViewSet):
    def paginate_queryset(self, queryset):
        return None

    queryset = models.NetosEoLReportModule.objects.all()
    serializer_class = serializers.NetosSummaryModuleSerializer


class NetosSummaryInventoryViewSet(NetBoxModelViewSet):
    def paginate_queryset(self, queryset):
        return None
    queryset = models.NetosEoLReportInventory.objects.all()
    serializer_class = serializers.NetosSummaryInventorySerializer


class NetosReportCollectViewSet(NetBoxModelViewSet):
    """
    Collect hardware report and save it
    """

    queryset = models.NetosEoLReportDevice.objects.all()
    serializer_class = serializers.NetosEoLReportDeviceSerializer

    def create(self, request, *args, **kwargs):
        hardwares = models.NetosHardware.objects.all()
        logger = logging.getLogger(__name__)
        try:
            with transaction.atomic():
                for hardware in hardwares:
                    # Find devices with the device_type
                    devices = Device.objects.filter(
                        device_type=hardware.device_type).all()
                    modules = Module.objects.filter(
                        device__device_type=hardware.device_type).all()
                    inventories = InventoryItem.objects.filter(
                        device__device_type=hardware.device_type).all()

                    for device in devices:
                        models.NetosEoLReportDevice.objects.create(
                            device=device,
                            eol_anncouncement=hardware.eol_anncouncement,
                            eol_maintanance=hardware.eol_maintanance,
                            eol_vulnerability=hardware.eol_vulnerability,
                            eol_support=hardware.eol_support,
                        )

                    for module in modules:
                        models.NetosEoLReportModule.objects.create(
                            device=module,
                            eol_anncouncement=hardware.eol_anncouncement,
                            eol_maintanance=hardware.eol_maintanance,
                            eol_vulnerability=hardware.eol_vulnerability,
                            eol_support=hardware.eol_support,
                        )
                    for inventory in inventories:
                        models.NetosEoLReportInventory.objects.create(
                            device=inventory,
                            eol_anncouncement=hardware.eol_anncouncement,
                            eol_maintanance=hardware.eol_maintanance,
                            eol_vulnerability=hardware.eol_vulnerability,
                            eol_support=hardware.eol_support,
                        )

            return Response({"detial": "New reports generated"}, status=status.HTTP_201_CREATED)
        except DatabaseError as ex:
            logger.error(f"Failed to collect report\n{ex}")
            return Response({"detial": "Failed to collect report. See logs for more information"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        return Response({"detial": "Method not allowed for report collection"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response({"detial": "Method not allowed for report collection"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response({"detial": "Method not allowed for report collection"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response({"detial": "Method not allowed for report collection"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def list(self, request, *args, **kwargs):
        return Response({"detial": "Method not allowed for report collection"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
