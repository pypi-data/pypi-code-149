from dcim.filtersets import DeviceFilterSet
import django_filters
from dcim.choices import DeviceStatusChoices
from dcim.models.devices import Device, DeviceRole, DeviceType, Manufacturer, Platform, VirtualChassis, ModuleType
from dcim.models.racks import Rack
from dcim.models.sites import Location, Region, Site, SiteGroup
from dcim.models.device_components import ModuleBay
from dcim.models.device_components import InventoryItem, InventoryItemRole
from netbox.filtersets import NetBoxModelFilterSet
from utilities.filters import ContentTypeFilter, MultiValueNumberFilter
from utilities.filters import MultiValueCharFilter, MultiValueMACAddressFilter, TreeNodeMultipleChoiceFilter
from virtualization.models import Cluster
from django.db.models import Q
from . import models


class NetosSoftwareReportFilterSet(DeviceFilterSet):
    compliance = django_filters.BooleanFilter(
        label='Serial number match',
    )

    class Meta:
        model = models.NetosSoftwareReport
        fields = ['id', 'name', 'asset_tag', 'face',
                  'position', 'airflow', 'vc_position', 'vc_priority']

##
# Report
##


class NetosEoLReportDeviceFilterSet(NetBoxModelFilterSet):
    manufacturer_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__device_type__manufacturer',
        queryset=Manufacturer.objects.all(),
        label='Manufacturer (ID)',
    )
    manufacturer = django_filters.ModelMultipleChoiceFilter(
        field_name='device__device_type__manufacturer__slug',
        queryset=Manufacturer.objects.all(),
        to_field_name='slug',
        label='Manufacturer (slug)',
    )
    device_type_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__device_type',
        queryset=DeviceType.objects.all(),
        label='Device type (ID)',
    )
    role_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__device_role_id',
        queryset=DeviceRole.objects.all(),
        label='Role (ID)',
    )
    role = django_filters.ModelMultipleChoiceFilter(
        field_name='device__device_role__slug',
        queryset=DeviceRole.objects.all(),
        to_field_name='slug',
        label='Role (slug)',
    )
    parent_device_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__parent_bay__device',
        queryset=Device.objects.all(),
        label='Parent Device (ID)',
    )
    platform_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__platform_id',
        queryset=Platform.objects.all(),
        label='Platform (ID)',
    )
    platform = django_filters.ModelMultipleChoiceFilter(
        field_name='device__platform__slug',
        queryset=Platform.objects.all(),
        to_field_name='slug',
        label='Platform (slug)',
    )
    region_id = TreeNodeMultipleChoiceFilter(
        queryset=Region.objects.all(),
        field_name='device__site__region',
        lookup_expr='in',
        label='Region (ID)',
    )
    region = TreeNodeMultipleChoiceFilter(
        queryset=Region.objects.all(),
        field_name='device__site__region',
        lookup_expr='in',
        to_field_name='slug',
        label='Region (slug)',
    )
    site_group_id = TreeNodeMultipleChoiceFilter(
        queryset=SiteGroup.objects.all(),
        field_name='device__site__group',
        lookup_expr='in',
        label='Site group (ID)',
    )
    site_group = TreeNodeMultipleChoiceFilter(
        queryset=SiteGroup.objects.all(),
        field_name='device__site__group',
        lookup_expr='in',
        to_field_name='slug',
        label='Site group (slug)',
    )
    site_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__site_id',
        queryset=Site.objects.all(),
        label='Site (ID)',
    )
    site = django_filters.ModelMultipleChoiceFilter(
        field_name='device__site__slug',
        queryset=Site.objects.all(),
        to_field_name='slug',
        label='Site name (slug)',
    )
    location_id = TreeNodeMultipleChoiceFilter(
        queryset=Location.objects.all(),
        field_name='device__location',
        lookup_expr='in',
        label='Location (ID)',
    )
    rack_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__rack',
        queryset=Rack.objects.all(),
        label='Rack (ID)',
    )
    cluster_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__cluster_id',
        queryset=Cluster.objects.all(),
        label='VM cluster (ID)',
    )
    model = django_filters.ModelMultipleChoiceFilter(
        field_name='device__device_type__slug',
        queryset=DeviceType.objects.all(),
        to_field_name='slug',
        label='Device model (slug)',
    )
    status = django_filters.MultipleChoiceFilter(
        field_name='device__status',
        choices=DeviceStatusChoices,
        null_value=None
    )
    is_full_depth = django_filters.BooleanFilter(
        field_name='device__device_type__is_full_depth',
        label='Is full depth',
    )
    mac_address = MultiValueMACAddressFilter(
        field_name='device__interfaces__mac_address',
        label='MAC address',
    )
    serial = MultiValueCharFilter(
        field_name='device__serial',
        lookup_expr='iexact'
    )
    has_primary_ip = django_filters.BooleanFilter(
        method='_has_primary_ip',
        label='Has a primary IP',
    )
    virtual_chassis_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__virtual_chassis',
        queryset=VirtualChassis.objects.all(),
        label='Virtual chassis (ID)',
    )
    virtual_chassis_member = django_filters.BooleanFilter(
        method='_virtual_chassis_member',
        label='Is a virtual chassis member'
    )
    console_ports = django_filters.BooleanFilter(
        method='_console_ports',
        label='Has console ports',
    )
    console_server_ports = django_filters.BooleanFilter(
        method='_console_server_ports',
        label='Has console server ports',
    )
    power_ports = django_filters.BooleanFilter(
        method='_power_ports',
        label='Has power ports',
    )
    power_outlets = django_filters.BooleanFilter(
        method='_power_outlets',
        label='Has power outlets',
    )
    interfaces = django_filters.BooleanFilter(
        method='_interfaces',
        label='Has interfaces',
    )
    pass_through_ports = django_filters.BooleanFilter(
        method='_pass_through_ports',
        label='Has pass-through ports',
    )
    module_bays = django_filters.BooleanFilter(
        method='_module_bays',
        label='Has module bays',
    )
    device_bays = django_filters.BooleanFilter(
        method='_device_bays',
        label='Has device bays',
    )

    position = django_filters.NumberFilter(
        field_name="device__position"
    )

    vc_position = django_filters.NumberFilter(
        field_name="device__vc_position"
    )

    vc_priority = django_filters.NumberFilter(
        field_name="device__vc_priority"
    )

    class Meta:
        model = models.NetosEoLReportDevice
        fields = ['id', 'position', 'vc_position', 'vc_priority']

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(serial__icontains=value.strip()) |
            Q(inventoryitems__serial__icontains=value.strip()) |
            Q(asset_tag__icontains=value.strip()) |
            Q(comments__icontains=value)
        ).distinct()

    def _has_primary_ip(self, queryset, name, value):
        params = Q(device__primary_ip4__isnull=False) | Q(
            device__primary_ip6__isnull=False)
        if value:
            return queryset.filter(params)
        return queryset.exclude(params)

    def _virtual_chassis_member(self, queryset, name, value):
        return queryset.exclude(device__virtual_chassis__isnull=value)

    def _console_ports(self, queryset, name, value):
        return queryset.exclude(device__consoleports__isnull=value)

    def _console_server_ports(self, queryset, name, value):
        return queryset.exclude(device__consoleserverports__isnull=value)

    def _power_ports(self, queryset, name, value):
        return queryset.exclude(device__powerports__isnull=value)

    def _power_outlets(self, queryset, name, value):
        return queryset.exclude(device__poweroutlets__isnull=value)

    def _interfaces(self, queryset, name, value):
        return queryset.exclude(device__interfaces__isnull=value)

    def _pass_through_ports(self, queryset, name, value):
        return queryset.exclude(
            device__frontports__isnull=value,
            device__rearports__isnull=value
        )

    def _module_bays(self, queryset, name, value):
        return queryset.exclude(device__modulebays__isnull=value)

    def _device_bays(self, queryset, name, value):
        return queryset.exclude(device__devicebays__isnull=value)


class NetosEoLReportModuleFilterSet(NetBoxModelFilterSet):
    site_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__device__site_id',
        queryset=Site.objects.all(),
    )
    device_type_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__device__device_type_id',
        queryset=DeviceType.objects.all()
    )
    device_role_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__device__device_role_id',
        queryset=DeviceRole.objects.all()
    )
    region_id = django_filters.NumberFilter(
        field_name='device__device__site__region__id'
    )
    device_model = django_filters.CharFilter(
        field_name='device__device__device_type__model'
    )

    manufacturer_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__module_type__manufacturer',
        queryset=Manufacturer.objects.all(),
        label='Manufacturer (ID)',
    )
    manufacturer = django_filters.ModelMultipleChoiceFilter(
        field_name='device__module_type__manufacturer__slug',
        queryset=Manufacturer.objects.all(),
        to_field_name='slug',
        label='Manufacturer (slug)',
    )
    module_type_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__module_type',
        queryset=ModuleType.objects.all(),
        label='Module type (ID)',
    )
    module_type = django_filters.ModelMultipleChoiceFilter(
        field_name='device__module_type__model',
        queryset=ModuleType.objects.all(),
        to_field_name='model',
        label='Module type (model)',
    )
    module_bay_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device__module_bay',
        queryset=ModuleBay.objects.all(),
        to_field_name='id',
        label='Module Bay (ID)'
    )
    device_id = django_filters.ModelMultipleChoiceFilter(
        field_name="device__device_id",
        queryset=Device.objects.all(),
        label='Device (ID)',
    )
    serial = MultiValueCharFilter(
        field_name="device__serial",
        lookup_expr='iexact'
    )

    class Meta:
        model = models.NetosEoLReportModule
        fields = (
            'site_id',
            'device_type_id',
            'device_role_id',
            'region_id',
            'manufacturer_id',
            'device_model',
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            device__device__name__icontains=value
        )


class NetosEoLReportInventoryFilterSet(NetBoxModelFilterSet):
    site_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Site.objects.all(),
        field_name='device__device__site_id'
    )
    device_type_id = django_filters.ModelMultipleChoiceFilter(
        queryset=DeviceType.objects.all(),
        field_name='device__device__device_type_id'
    )
    device_role_id = django_filters.ModelMultipleChoiceFilter(
        queryset=DeviceRole.objects.all(),
        field_name='device__device__device_role_id'
    )
    region_id = django_filters.NumberFilter(
        field_name='device__device__site__region__id')
    # manufacturer_id = django_filters.NumberFilter(
    #     field_name='device__device__device_type__manufacturer_id')
    device_model = django_filters.CharFilter(
        field_name='device__device__device_type__model'
    )

    parent_id = django_filters.ModelMultipleChoiceFilter(
        field_name="device__parent_id",
        queryset=InventoryItem.objects.all(),
        label='Parent inventory item (ID)',
    )
    manufacturer_id = django_filters.ModelMultipleChoiceFilter(
        field_name="device__manufacturer",
        queryset=Manufacturer.objects.all(),
        label='Manufacturer (ID)',
    )
    manufacturer = django_filters.ModelMultipleChoiceFilter(
        field_name='device__manufacturer__slug',
        queryset=Manufacturer.objects.all(),
        to_field_name='slug',
        label='Manufacturer (slug)',
    )

    component_type = ContentTypeFilter(
        field_name="device__component_type"
    )
    component_id = MultiValueNumberFilter(
        field_name="device__component_id"
    )
    serial = MultiValueCharFilter(
        field_name="device__serial",
        lookup_expr='iexact'
    )

    class Meta:
        model = models.NetosEoLReportInventory
        fields = (
            'site_id',
            'device_type_id',
            'device_role_id',
            'region_id',
            'manufacturer_id',
            'device_model',
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            device__device__name__icontains=value
        )
