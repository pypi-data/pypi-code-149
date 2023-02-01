from dcim.api.nested_serializers import (NestedDeviceSerializer,
                                         NestedDeviceTypeSerializer,
                                         NestedInventoryItemSerializer,
                                         NestedManufacturerSerializer,
                                         NestedModuleSerializer)
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

from .. import models

HARDWARE_FIELDS = (
    'name',
    'slug',
    'device_type',
    'eol_anncouncement_days',
    'eol_anncouncement',
    'eol_maintanance_days',
    'eol_maintanance',
    'eol_support_days',
    'eol_support',
    'eol_vulnerability_days',
    'eol_vulnerability',
    'manufacturer',
    'product_data_sheet',
    'replacement_model',
)

REPORT_FIELDS = (
    'created',
    'device',
    'eol_anncouncement_days',
    'eol_anncouncement',
    'eol_maintanance_days',
    'eol_maintanance',
    'eol_support_days',
    'eol_support',
    'eol_vulnerability_days',
    'eol_vulnerability',
)

SUMMARY_FIELDS = (
    'created',
    'device_model_id',
    'device_model',
    'device_role_id',
    'device_role',
    'device_type_id',
    'device_type',
    'eol_anncouncement_days',
    'eol_anncouncement',
    'eol_maintanance_days',
    'eol_maintanance',
    'eol_support_days',
    'eol_support',
    'eol_vulnerability_days',
    'eol_vulnerability',
    'location_id',
    'location',
    'manufacturer_display',
    'manufacturer_id',
    'region_id',
    'region',
    'site_id',
    'site',
)

SOFTWARE_FIELDS = (
    'name',
    'slug',
    'device_type',
    'eol_anncouncement_days',
    'eol_anncouncement',
    'eol_maintanance_days',
    'eol_maintanance',
    'eol_support_days',
    'eol_support',
    'eol_vulnerability_days',
    'eol_vulnerability',
    'manufacturer',
    'product_data_sheet',
    'replacement_model',
    'version',
    'standard_version',
    'operating_system',
)
##
# Hardware
##


class NetosHardwareSerializer(NetBoxModelSerializer):
    device_type = NestedDeviceTypeSerializer()
    manufacturer = NestedManufacturerSerializer()

    class Meta:
        model = models.NetosHardware
        fields = HARDWARE_FIELDS


##
# Software
##


class NetosSoftwareSerializer(NetBoxModelSerializer):
    device_type = NestedDeviceTypeSerializer()
    manufacturer = NestedManufacturerSerializer()

    class Meta:

        model = models.NetosSoftware
        fields = SOFTWARE_FIELDS

##
# Report
##


class NetosEoLReportDeviceSerializer(NetBoxModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    device = NestedDeviceSerializer()

    class Meta:
        model = models.NetosEoLReportModule
        fields = REPORT_FIELDS


class NetosEoLReportModuleSerializer(NetBoxModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    device = NestedModuleSerializer()

    class Meta:
        model = models.NetosEoLReportDevice
        fields = REPORT_FIELDS


class NetosEoLReportInventorySerializer(NetBoxModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    device = NestedInventoryItemSerializer()

    class Meta:
        model = models.NetosEoLReportInventory
        fields = REPORT_FIELDS

##
# Summary
##


class NetosSummaryDeviceSerializer(NetBoxModelSerializer):
    class Meta:

        model = models.NetosEoLReportDevice
        fields = SUMMARY_FIELDS


class NetosSummaryModuleSerializer(NetBoxModelSerializer):

    class Meta:

        model = models.NetosEoLReportModule
        fields = SUMMARY_FIELDS


class NetosSummaryInventorySerializer(NetBoxModelSerializer):

    class Meta:

        model = models.NetosEoLReportInventory
        fields = SUMMARY_FIELDS
