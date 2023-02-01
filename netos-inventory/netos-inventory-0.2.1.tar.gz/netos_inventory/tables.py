import django_tables2 as tables
from ipam.tables.vlans import VLANTable
from ipam.tables.vrfs import VRFTable
from ipam.tables.fhrp import FHRPGroupTable
from ipam.tables.ip import ASNTable, IPAddressTable, PrefixTable
from dcim.tables.devices import InterfaceTable
from dcim.tables.cables import CableTable
from dcim.tables.modules import ModuleTable
from dcim.tables.devices import InventoryItemTable
from dcim.tables.template_code import DEVICE_LINK

from netbox.tables import NetBoxTable, columns
from wireless.tables.wirelesslan import WirelessLANTable
from . import models
from dcim.tables.devices import DeviceTable
from django.conf import settings

config = settings.PLUGINS_CONFIG["netos_inventory"]

CUSTOM_FIELDS = ("cf_Netos_Last_Polled", "cf_polled_status")


class MatchColumn(tables.TemplateColumn):
    """
    Render a colored column. Column is colored red when columns match is false, else is green
    """
    template_code = """
  {% load helpers %}
  {% if value is True %}
    <span class="badge" style="color: {{ 'green'|fgcolor }}; background-color: green">
      Yes
    </span>
  {% elif value is False %}
    <span class="badge" style="color: {{ 'red'|fgcolor }}; background-color: red">
      No
    </span>
  {% else %}
    <span class="badge" style="color: {{ 'grey'|fgcolor }}; background-color: grey">
      Unknown
    </span>
  {% endif %}
"""

    def __init__(self, *args, **kwargs):
        super().__init__(template_code=self.template_code, *args, **kwargs)

    def value(self, value):
        return str(value)


class LanUtilizationColumn(tables.TemplateColumn):
    """
    Display a colored utilization bar graph.
    Use red when utilization is below level given in config ('min_lan_switch_utilization')
    """
    template_code = """
    {% load recon_buttons %}
    {% lan_utilization_graph value danger_threshold=min_lan_switch_utilization %}
    """

    def __init__(self, *args, **kwargs):
        min_utilization = config["min_lan_switch_utilization"]
        extra_context = {
            "min_lan_switch_utilization": min_utilization
        }
        super().__init__(template_code=self.template_code,
                         extra_context=extra_context, *args, **kwargs)

    def value(self, value):
        return f'{value}%'


class ReconDeviceTable(DeviceTable):

    device_type_match = MatchColumn()
    serial_match = MatchColumn()
    netos_software_kickstart_version_match = MatchColumn()
    netos_software_version_match = MatchColumn()
    netos_hostname_match = MatchColumn()

    def __init__(self, *args, extra_columns=None, **kwargs):
        super().__init__(*args, extra_columns=extra_columns, **kwargs)

    class Meta(NetBoxTable.Meta):
        detected_fields = tuple(
            map(lambda x: f"cf_{x}", config["device_recon_fields"].values()))
        custom_fields = tuple(
            map(lambda x: f"cf_{x}", [k for k in config["device_recon_fields"].keys() if "Netos" in k])
        )
        model = models.ReconDevice

        default_columns = ('pk', 'name', 'status', 'device_type', 'serial',
                           'serial_match', 'device_type_match', 'netos_software_kickstart_version_match', 'netos_software_version_match', 'netos_hostname_match') + custom_fields + detected_fields
        fields = (
            'pk', 'id', 'name', 'status', 'tenant', 'tenant_group', 'device_role', 'manufacturer', 'device_type',
            'platform', 'serial', 'asset_tag', 'region', 'site_group', 'site', 'location', 'rack', 'position', 'face',
            'airflow', 'primary_ip', 'primary_ip4', 'primary_ip6', 'cluster', 'virtual_chassis', 'vc_position',
            'vc_priority', 'comments', 'contacts', 'tags', 'created', 'last_updated',
            'serial_match', 'device_type_match', 'netos_software_kickstart_version_match', 'netos_software_version_match', 'netos_hostname_match'
        )  + custom_fields + detected_fields


class ReconModuleTable(ModuleTable):
    serial_match = MatchColumn()

    class Meta(NetBoxTable.Meta):
        model = models.ReconModule
        detected_fields = tuple(
            map(lambda x: f"cf_{x}", config["module_recon_fields"].values()))
        custom_fields = tuple(
            map(lambda x: f"cf_{x}", [k for k in config["module_recon_fields"].keys() if "Netos" in k])
        )

        fields = (
            'pk', 'id', 'device', 'module_bay', 'manufacturer', 'module_type', 'serial', 'asset_tag', 'comments',
            'tags', 'serial_match'
        ) + custom_fields + detected_fields
        default_columns = (
            'pk', 'id', 'device', 'module_bay', 'manufacturer', 'module_type', 'serial', 'asset_tag', 'serial_match'
        ) + custom_fields + detected_fields


class ReconInventoryItemTable(InventoryItemTable):
    serial_match = MatchColumn()

    class Meta(NetBoxTable.Meta):
        model = models.ReconInventoryItem
        detected_fields = tuple(
            map(lambda x: f"cf_{x}", config["inventory_recon_fields"].values()))
        custom_fields = tuple(
            map(lambda x: f"cf_{x}", [k for k in config["inventory_recon_fields"].keys() if "Netos" in k])
        )

        fields = (
            'pk', 'id', 'name', 'device', 'component', 'label', 'role', 'manufacturer', 'part_id', 'serial',
            'asset_tag', 'description', 'discovered', 'tags', 'created', 'last_updated', 'serial_match'
        ) + custom_fields + detected_fields

        default_columns = (
            'pk', 'name', 'device', 'label', 'role', 'manufacturer', 'part_id', 'serial', 'asset_tag', 'serial_match'
        ) + custom_fields + detected_fields


# Logical Last Detected


class VRFDetectedTable(VRFTable):
    actions = {}

    class Meta(VRFTable.Meta):
        model = models.VRFDetected
        fields = ('pk', 'id', 'name', 'tenant', 'tenant_group',
                  'description', 'tags', 'created', 'last_updated',) + CUSTOM_FIELDS
        default_columns = ('pk', 'name', 'rd', 'tenant',
                           'description',) + CUSTOM_FIELDS


class VLANDetectedTable(VLANTable):
    actions = {}

    class Meta(VLANTable.Meta):
        model = models.VLANDetected
        fields = (
            'pk', 'id', 'vid', 'name', 'site', 'group', 'prefixes', 'tenant', 'tenant_group', 'status', 'role',
            'description', 'tags', 'l2vpn', 'created', 'last_updated',) + CUSTOM_FIELDS
        default_columns = ('pk', 'vid', 'name', 'site', 'group', 'prefixes',
                           'tenant', 'status', 'role', 'description', ) + CUSTOM_FIELDS


class FHRPGroupDetectedTable(FHRPGroupTable):
    actions = {}

    class Meta(FHRPGroupTable.Meta):
        model = models.FHRPGroupDetected
        fields = (
            'pk', 'group_id', 'protocol', 'auth_type', 'auth_key', 'description', 'ip_addresses', 'member_count',
            'tags', 'created', 'last_updated') + CUSTOM_FIELDS
        default_columns = ('pk', 'group_id', 'protocol', 'auth_type',
                           'description', 'ip_addresses', 'member_count',) + CUSTOM_FIELDS


class ASNDetectedTable(ASNTable):
    #actions = {}

    class Meta(ASNTable.Meta):
        model = models.ASNDetected
        fields = (
            'pk', 'asn', 'asn_asdot', 'rir', 'site_count', 'provider_count', 'tenant', 'tenant_group', 'description', 'sites', 'tags',
            'created', 'last_updated', 'actions') + CUSTOM_FIELDS
        default_columns = ('pk', 'asn', 'rir', 'site_count', 'provider_count',
                           'sites', 'description', 'tenant') + CUSTOM_FIELDS


class IPAddressDetectedTable(IPAddressTable):
    actions = {}

    class Meta(IPAddressTable.Meta):
        model = models.IPAddressDetected
        fields = (
            'pk', 'id', 'address', 'vrf', 'status', 'role', 'tenant', 'tenant_group', 'nat_inside', 'nat_outside', 'assigned', 'dns_name', 'description',
            'tags', 'created', 'last_updated',
        ) + CUSTOM_FIELDS
        default_columns = (
            'pk', 'address', 'vrf', 'status', 'role', 'tenant', 'assigned', 'dns_name', 'description',
        ) + CUSTOM_FIELDS


class PrefixDetectedTable(PrefixTable):
    actions = {}

    class Meta(PrefixTable.Meta):
        model = models.PrefixDetected
        fields = (
            'pk', 'id', 'prefix', 'prefix_flat', 'status', 'children', 'vrf', 'utilization', 'tenant', 'tenant_group', 'site',
            'vlan_group', 'vlan', 'role', 'is_pool', 'mark_utilized', 'description', 'tags', 'created', 'last_updated',
        ) + CUSTOM_FIELDS
        default_columns = (
            'pk', 'prefix', 'status', 'children', 'vrf', 'utilization', 'tenant', 'site', 'vlan', 'role', 'description',
        ) + CUSTOM_FIELDS


class WirelessLANDetectedTable(WirelessLANTable):
    actions = {}

    class Meta(WirelessLANTable.Meta):
        model = models.WirelessLANDetected
        fields = (
            'pk', 'ssid', 'group', 'tenant', 'tenant_group', 'description', 'vlan', 'interface_count', 'auth_type',
            'auth_cipher', 'auth_psk', 'tags', 'created', 'last_updated',
        ) + CUSTOM_FIELDS
        default_columns = ('pk', 'ssid', 'group', 'description',
                           'vlan', 'auth_type', 'interface_count',) + CUSTOM_FIELDS

##
# Hardware Last Detected
##


class DeviceDetectedTable(DeviceTable):

    actions = {}

    class Meta(DeviceTable.Meta):
        model = models.DeviceDetected
        fields = (
            'pk', 'id', 'name', 'status', 'tenant', 'tenant_group', 'device_role', 'manufacturer', 'device_type',
            'platform', 'serial', 'asset_tag', 'region', 'site_group', 'site', 'location', 'rack', 'position', 'face',
            'airflow', 'primary_ip', 'primary_ip4', 'primary_ip6', 'cluster', 'virtual_chassis', 'vc_position',
            'vc_priority', 'comments', 'contacts', 'tags', 'created', 'last_updated',
        ) + CUSTOM_FIELDS
        default_columns = (
            'pk', 'name', 'status', 'tenant', 'site', 'location', 'rack', 'device_role', 'manufacturer', 'device_type',
            'primary_ip',
        ) + CUSTOM_FIELDS


class InterfaceDetectedTable(InterfaceTable):
    actions = {}

    class Meta(InterfaceTable.Meta):
        model = models.InterfaceDetected
        fields = (
            'pk', 'id', 'name', 'device', 'module_bay', 'module', 'label', 'enabled', 'type', 'mgmt_only', 'mtu',
            'speed', 'duplex', 'mode', 'mac_address', 'wwn', 'poe_mode', 'poe_type', 'rf_role', 'rf_channel',
            'rf_channel_frequency', 'rf_channel_width', 'tx_power', 'description', 'mark_connected', 'cable',
            'cable_color', 'wireless_link', 'wireless_lans', 'link_peer', 'connection', 'tags', 'vrf', 'l2vpn',
            'ip_addresses', 'fhrp_groups', 'untagged_vlan', 'tagged_vlans', 'created', 'last_updated',
        ) + CUSTOM_FIELDS
        default_columns = ('pk', 'name', 'device', 'label',
                           'enabled', 'type', 'description',) + CUSTOM_FIELDS


class ModuleDetectedTable(ModuleTable):
    actions = {}

    class Meta(ModuleTable.Meta):
        model = models.ModuleDetected
        fields = (
            'pk', 'id', 'device', 'module_bay', 'manufacturer', 'module_type', 'serial', 'asset_tag', 'comments',
            'tags',
        ) + CUSTOM_FIELDS
        default_columns = (
            'pk', 'id', 'device', 'module_bay', 'manufacturer', 'module_type', 'serial', 'asset_tag',
        ) + CUSTOM_FIELDS


class CableDetectedTable(CableTable):
    actions = {}

    class Meta(CableTable.Meta):
        model = models.CableDetected
        fields = (
            'pk', 'id', 'label', 'a_terminations', 'b_terminations', 'device_a', 'device_b', 'rack_a', 'rack_b',
            'location_a', 'location_b', 'site_a', 'site_b', 'status', 'type', 'tenant', 'tenant_group', 'color',
            'length', 'tags', 'created', 'last_updated',
        ) + CUSTOM_FIELDS
        default_columns = (
            'pk', 'id', 'label', 'a_terminations', 'b_terminations', 'status', 'type',
        ) + CUSTOM_FIELDS

# Report


class LANConsolidationReportTable(DeviceTable):
    actions = {}

    utilization = LanUtilizationColumn(
        verbose_name='Percentage Port Utilization',
    )

    class Meta(NetBoxTable.Meta):
        model = models.LANConsolidationReport

        fields = (
            'pk', 'id', 'name', 'status', 'tenant', 'tenant_group', 'device_role', 'manufacturer', 'device_type',
            'platform', 'serial', 'asset_tag', 'region', 'site_group', 'site', 'location', 'rack', 'position', 'face',
            'airflow', 'primary_ip', 'primary_ip4', 'primary_ip6', 'cluster', 'virtual_chassis', 'vc_position',
            'vc_priority', 'comments', 'contacts', 'tags', 'created', 'last_updated', 'interface_up', 'interface_down', 'utilization'
        )
        default_columns = (
            'pk', 'name', 'status', 'tenant', 'site', 'location', 'rack', 'device_role', 'manufacturer', 'device_type',
            'primary_ip', 'interface_up', 'interface_down', 'utilization'
        )
