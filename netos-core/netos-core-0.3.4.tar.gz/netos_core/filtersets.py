import django_filters
from netbox.filtersets import NetBoxModelFilterSet

from . import models

##
# Hardware
##


class NetosHardwareFilterSet(NetBoxModelFilterSet):
    device_type_id = django_filters.NumberFilter(
        field_name='device_type_id')

    class Meta:
        model = models.NetosHardware
        fields = (
            'device_type',
            'device_type_id',
            'eol_anncouncement',
            'eol_maintanance',
            'eol_support',
            'eol_vulnerability',
            'manufacturer',
            'product_data_sheet',
            'replacement_model',
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            name__icontains=value
        )


##
# Software
##

class NetosSoftwareFilterSet(NetBoxModelFilterSet):
    device_type_id = django_filters.NumberFilter(
        field_name='device_type_id')

    class Meta:
        model = models.NetosHardware
        fields = (
            'device_type',
            'device_type_id',
            'eol_anncouncement',
            'eol_maintanance',
            'eol_support',
            'eol_vulnerability',
            'manufacturer',
            'product_data_sheet',
            'replacement_model',
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            name__icontains=value
        )
##
# Report
##


class NetosEoLReportDeviceFilterSet(NetBoxModelFilterSet):
    site_id = django_filters.NumberFilter(field_name='device__site_id')
    device_type_id = django_filters.NumberFilter(
        field_name='device__device_type_id')
    device_role_id = django_filters.NumberFilter(
        field_name='device__device_role_id')
    region_id = django_filters.NumberFilter(
        field_name='device__site__region__id')
    manufacturer_id = django_filters.NumberFilter(
        field_name='device__device_type__manufacturer_id')
    device_model = django_filters.CharFilter(
        field_name='device__device_type__model')

    class Meta:
        model = models.NetosEoLReportDevice
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
            device__name__icontains=value
        )


class NetosEoLReportModuleFilterSet(NetBoxModelFilterSet):
    site_id = django_filters.NumberFilter(field_name='device__device__site_id')
    device_type_id = django_filters.NumberFilter(
        field_name='device__device__device_type_id')
    device_role_id = django_filters.NumberFilter(
        field_name='device__device__device_role_id')
    region_id = django_filters.NumberFilter(
        field_name='device__device__site__region__id')
    manufacturer_id = django_filters.NumberFilter(
        field_name='device__device__device_type__manufacturer_id')
    device_model = django_filters.CharFilter(
        field_name='device__device__device_type__model')

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
    site_id = django_filters.NumberFilter(field_name='device__device__site_id')
    device_type_id = django_filters.NumberFilter(
        field_name='device__device__device_type_id')
    device_role_id = django_filters.NumberFilter(
        field_name='device__device__device_role_id')
    region_id = django_filters.NumberFilter(
        field_name='device__device__site__region__id')
    manufacturer_id = django_filters.NumberFilter(
        field_name='device__device__device_type__manufacturer_id')
    device_model = django_filters.CharFilter(
        field_name='device__device__device_type__model')

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
