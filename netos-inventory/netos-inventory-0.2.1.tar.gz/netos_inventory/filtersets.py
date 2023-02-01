import django_filters
from dcim.filtersets import DeviceFilterSet, ModuleFilterSet, InventoryItemFilterSet
from dcim.models.sites import Site, Region
from netbox.filtersets import NetBoxModelFilterSet
from . import models


class ReconDeviceFilterSet(DeviceFilterSet):
    serial_match = django_filters.BooleanFilter(
        label='Serial number match',
    )
    device_type_match = django_filters.BooleanFilter(
        label='Device type match',
    )
    netos_software_kickstart_version_match = django_filters.BooleanFilter(
        label='Software kickstart version match',
    )
    netos_software_version_match = django_filters.BooleanFilter(
        label='Software version match',
    )
    netos_hostname_match = django_filters.BooleanFilter(
        label='Hostname match',
    )
    model = models.ReconDevice

class ReconModuleFilterSet(ModuleFilterSet):
    site_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Site.objects.all(),
        field_name='device__site',
        label='Site (ID)',
    )

    region_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Region.objects.all(),
        field_name='device__site__region',
        label='Region (ID)',
    )

    serial_match = django_filters.BooleanFilter(
        label='Serial number match',
    )

    model = models.ReconModule

class ReconInventoryItemFilterSet(InventoryItemFilterSet):
    serial_match = django_filters.BooleanFilter(
        label='Serial number match',
    )

    model = models.ReconInventoryItem

###
# Hardware Last Detected
##
class DeviceDetectedFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.DeviceDetected
        fields = ('id', )
    
class InterfaceDetectedFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.InterfaceDetected
        fields = ('id', )
    
class ModuleDetectedFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.ModuleDetected
        fields = ('id', )
    
class CableDetectedFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.CableDetected
        fields = ('id', )

###
# Logical Last Detected
###

class VRFDetectedFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.VRFDetected
        fields = ('id', )

class VLANDetectedFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.VLANDetected
        fields = ('id', )

class FHRPGroupDetectedFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.FHRPGroupDetected
        fields = ('id', )

class ASNDetectedFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.ASNDetected
        fields = ('id', )

class IPAddressDetectedFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.IPAddressDetected
        fields = ('id', )


class PrefixDetectedFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.PrefixDetected
        fields = ('id', )

class WirelessLANDetectedFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.WirelessLANDetected
        fields = ('id', )

##
# LAN Reprot
##
class LANConsolidationReportFilterSet(DeviceFilterSet):
    utilization = django_filters.NumberFilter(field_name='utilization', lookup_expr='lte')

    class Meta:
        model = models.LANConsolidationReport
        fields = ['id', 'name', 'asset_tag', 'face', 'position', 'airflow', 'vc_position', 'vc_priority']

