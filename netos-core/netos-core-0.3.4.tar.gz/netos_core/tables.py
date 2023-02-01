import django_tables2 as tables
from django_tables2.utils import Accessor
from netbox.tables import NetBoxTable

from . import models

REPORT_FIELDS = (
    'airflow',
    'cluster',
    'created',
    'device_role',
    'device_type',
    'device',
    'eol_anncouncement_days',
    'eol_anncouncement',
    'eol_maintanance_days',
    'eol_maintanance',
    'eol_support_days',
    'eol_support',
    'eol_vulnerability_days',
    'eol_vulnerability',
    'face',
    'location',
    'pk',
    'position',
    'primary_ip4',
    'primary_ip6',
    'rack',
    'region',
    'site_group',
    'site',
    'tenant',
    'vc_position',
    'vc_priority',
    'virtual_chassis',
)

REPORT_DEFAULT_COLS = (
    'device',
    'created',
    'eol_anncouncement_days',
    'eol_maintanance_days',
    'eol_support_days',
    'eol_vulnerability_days',
    'site',
)


class DaysLeftColumn(tables.TemplateColumn):
    """
    Display days left with threshold colors
    """
    template_code = """{% load eol_helpers %}{% if record.pk %}{% eol_threshold value %}{% endif %}"""

    def __init__(self, *args, **kwargs):
        super().__init__(template_code=self.template_code, *args, **kwargs)

    def value(self, value):
        return f'{value}%'


##
# Hardware
##

class NetosHardwareTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    device_type = tables.Column(
        accessor=Accessor('device_type'),
        linkify=True
    )

    replacement_model = tables.Column(
        accessor=Accessor('replacement_model'),
        linkify=True
    )

    eol_maintanance_days = DaysLeftColumn(
        orderable=False
    )

    eol_anncouncement_days = DaysLeftColumn(
        orderable=False
    )

    eol_vulnerability_days = DaysLeftColumn(
        orderable=False
    )

    eol_support_days = DaysLeftColumn(
        orderable=False
    )

    class Meta(NetBoxTable.Meta):
        model = models.NetosHardware
        fields = (
            'name',
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

        default_columns = (
            'name',
            'device_type',
            'eol_anncouncement',
            'eol_maintanance_days',
            'eol_maintanance',
            'pk',
            'product_data_sheet',
        )


##
# Software
##
class NetosSoftwareDeviceTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    device_type = tables.Column(
        accessor=Accessor('device_type'),
        linkify=True
    )

    replacement_model = tables.Column(
        accessor=Accessor('replacement_model'),
        linkify=True
    )

    manufacturer = tables.Column(
        accessor=Accessor('manufacturer'),
        linkify=True
    )

    eol_maintanance_days = DaysLeftColumn(
        orderable=False
    )

    eol_anncouncement_days = DaysLeftColumn(
        orderable=False
    )

    eol_vulnerability_days = DaysLeftColumn(
        orderable=False
    )

    eol_support_days = DaysLeftColumn(
        orderable=False
    )

    class Meta(NetBoxTable.Meta):
        model = models.NetosSoftware
        fields = (
            'name',
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
            'standard_version',
            'version',

        )
        default_columns = (
            'name',
            'device_type',
            'eol_anncouncement',
            'eol_maintanance_days',
            'eol_maintanance',
            'pk',
            'product_data_sheet',
        )


##
# Report
##
class NetosEoLReportBaseTable(NetBoxTable):
    eol_anncouncement_days = DaysLeftColumn(
        orderable=False
    )

    eol_maintanance_days = DaysLeftColumn(
        orderable=False
    )

    eol_maintanance_days = DaysLeftColumn(
        orderable=False
    )

    eol_vulnerability_days = DaysLeftColumn(
        orderable=False
    )

    eol_support_days = DaysLeftColumn(
        orderable=False
    )


class NetosEoLReportTable(NetosEoLReportBaseTable):
    device = tables.Column(
        accessor=Accessor('device'),
        linkify=True
    )

    site = tables.Column(
        accessor=Accessor('device__site'),
        linkify=True
    )
    tenant = tables.Column(
        accessor=Accessor('device__tenant'),
    )
    device_role = tables.Column(
        accessor=Accessor('device__device_role'),
        linkify=True
    )
    device_type = tables.Column(
        accessor=Accessor('device__device_type'),
        linkify=True
    )
    region = tables.Column(
        accessor=Accessor('device__site__region'),
        linkify=True
    )
    site_group = tables.Column(
        accessor=Accessor('device__site__site_group'),
    )
    location = tables.Column(
        accessor=Accessor('device__location'),
        linkify=True
    )
    rack = tables.Column(
        accessor=Accessor('device__rack'),
        linkify=True
    )
    position = tables.Column(
        accessor=Accessor('device.position'),
    )
    face = tables.Column(
        accessor=Accessor('device.face'),
    )
    airflow = tables.Column(
        accessor=Accessor('device.airflow'),
    )
    primary_ip4 = tables.Column(
        accessor=Accessor('device__primary_ip4'),
    )
    primary_ip6 = tables.Column(
        accessor=Accessor('device__primary_ip6'),
    )
    cluster = tables.Column(
        accessor=Accessor('device__cluster'),
        linkify=True

    )
    virtual_chassis = tables.Column(
        accessor=Accessor('device__virtual_chassis'),
        linkify=True
    )
    vc_position = tables.Column(
        accessor=Accessor('device.vc_position'),
    )
    vc_priority = tables.Column(
        accessor=Accessor('device.vc_priority'),
    )

    class Meta(NetBoxTable.Meta):
        model = models.NetosEoLReportDevice
        fields = REPORT_FIELDS
        default_columns = REPORT_DEFAULT_COLS
        order_by = ('device', '-created')


class NetosEoLReportModuleTable(NetosEoLReportBaseTable):
    module = tables.Column(
        accessor=Accessor('device'),
        linkify=True,
        verbose_name='Module'
    )

    module_type = tables.Column(
        accessor=Accessor('device__module_type'),
        linkify=True,
    )
    device = tables.Column(
        accessor=Accessor('device__device'),
        linkify=True
    )

    module_bay = tables.Column(
        accessor=Accessor('device__module_bay'),
        linkify=True
    )
    serial = tables.Column(
        accessor=Accessor('device.serial'),
    )
    asset_tag = tables.Column(
        accessor=Accessor('device.asset_tag'),
    )

    class Meta(NetBoxTable.Meta):
        model = models.NetosEoLReportModule
        fields = (
            'module',
            'created',
            'module_type',
            'device',
            'module_bay',
            'serial',
            'asset_tag',
            'eol_anncouncement_days',
            'eol_anncouncement',
            'eol_maintanance_days',
            'eol_maintanance',
            'eol_support_days',
            'eol_support',
            'eol_vulnerability_days',
            'eol_vulnerability',
        )
        default_columns = (
            'module',
            'created',
            'module_type',
            'device',
            'eol_anncouncement_days',
            'eol_maintanance_days',
            'eol_support_days',
            'eol_vulnerability_days',
        )

        order_by = ('module', '-created')


class NetosEoLReportInventoryTable(NetosEoLReportBaseTable):
    inventory_item = tables.Column(
        accessor=Accessor('device'),
        linkify=True,
        verbose_name='Inventory Item'
    )
    device = tables.Column(
        accessor=Accessor('device__device'),
        linkify=True
    )

    component = tables.Column(
        accessor=Accessor('device__component'),
        linkify=True
    )

    role = tables.Column(
        accessor=Accessor('device__role'),
        linkify=True
    )
    manufacturer = tables.Column(
        accessor=Accessor('device__manufacturer'),
        linkify=True
    )
    part_id = tables.Column(
        accessor=Accessor('device.part_id'),
    )
    asset_tag = tables.Column(
        accessor=Accessor('device.asset_tag'),
    )
    discovered = tables.Column(
        accessor=Accessor('device.discovered')
    )

    class Meta(NetBoxTable.Meta):
        model = models.NetosEoLReportInventory
        fields = (
            'inventory_item',
            'created',
            'device',
            'component',
            'role',
            'manufacturer',
            'part_id',
            'asset_tag',
            'discovered',
            'eol_anncouncement_days',
            'eol_anncouncement',
            'eol_maintanance_days',
            'eol_maintanance',
            'eol_support_days',
            'eol_support',
            'eol_vulnerability_days',
            'eol_vulnerability',
        )
        default_columns = (
            'inventory_item',
            'created',
            'component',
            'eol_anncouncement_days',
            'eol_maintanance_days',
            'eol_support_days',
            'eol_vulnerability_days',
        )
        order_by = ('inventory_item', '-created')
