
from dcim.api.serializers import DeviceSerializer, InterfaceSerializer, ModuleSerializer, CableSerializer
from ipam.api.serializers import (VRFSerializer, ASNSerializer, VLANSerializer,
                                  FHRPGroupSerializer, IPAddressSerializer, PrefixSerializer)
from dcim.api.serializers import InventoryItemSerializer
from wireless.api.serializers import WirelessLANSerializer

from .. import models


class ReconDeviceSerializer(DeviceSerializer):

    class Meta:
        model = models.ReconDevice
        fields = [
            'id', 'url', 'display', 'name', 'device_type', 'device_role', 'tenant', 'platform', 'serial', 'asset_tag',
            'site', 'location', 'rack', 'position', 'face', 'parent_device', 'status', 'airflow', 'primary_ip',
            'primary_ip4', 'primary_ip6', 'cluster', 'virtual_chassis', 'vc_position', 'vc_priority', 'comments',
            'local_context_data', 'tags', 'custom_fields', 'created', 'last_updated',
        ]

class ReconModuleSerializer(ModuleSerializer):

    class Meta:
        model = models.ReconModule
        fields = [
            'id', 'url', 'display', 'device', 'module_bay', 'module_type', 'serial', 'asset_tag', 'comments', 'tags',
            'custom_fields', 'created', 'last_updated',
        ]

class ReconInventoryItemSerializer(InventoryItemSerializer):

    class Meta:
        model = models.ReconInventoryItem
        fields = [
            'id', 'url', 'display', 'device', 'parent', 'name', 'label', 'role', 'manufacturer', 'part_id', 'serial',
            'asset_tag', 'discovered', 'description', 'component_type', 'component_id', 'component', 'tags',
            'custom_fields', 'created', 'last_updated', '_depth',
        ]

##
# Hardware
##


class DeviceDetectedSerializer(DeviceSerializer):
    class Meta:
        model = models.DeviceDetected
        fields = ('id', 'url', 'display', 'name', 'device_type', 'device_role', 'tenant', 'platform', 'serial', 'asset_tag',
                  'site', 'location', 'rack', 'position', 'face', 'parent_device', 'status', 'airflow', 'primary_ip',
                  'primary_ip4', 'primary_ip6', 'cluster', 'virtual_chassis', 'vc_position', 'vc_priority', 'comments',
                  'local_context_data', 'tags', 'custom_fields', 'created', 'last_updated',)


class InterfaceDetectedSerializer(InterfaceSerializer):
    class Meta:
        model = models.InterfaceDetected
        fields = ('id', 'url', 'display', 'device', 'module', 'name', 'label', 'type', 'enabled', 'parent', 'bridge', 'lag',
                  'mtu', 'mac_address', 'speed', 'duplex', 'wwn', 'mgmt_only', 'description', 'mode', 'rf_role', 'rf_channel',
                  'poe_mode', 'poe_type', 'rf_channel_frequency', 'rf_channel_width', 'tx_power', 'untagged_vlan',
                              'tagged_vlans', 'mark_connected', 'cable', 'cable_end', 'wireless_link', 'link_peers', 'link_peers_type',
                              'wireless_lans', 'vrf', 'l2vpn_termination', 'connected_endpoints', 'connected_endpoints_type',
                              'connected_endpoints_reachable', 'tags', 'custom_fields', 'created', 'last_updated', 'count_ipaddresses',
                              'count_fhrp_groups', '_occupied',)


class ModuleDetectedSerializer(ModuleSerializer):
    class Meta:
        model = models.ModuleDetected
        fields = ('id', 'url', 'display', 'device', 'module_bay', 'module_type', 'serial', 'asset_tag', 'comments', 'tags',
                  'custom_fields', 'created', 'last_updated',)


class CableDetectedSerialzier(CableSerializer):
    class Meta:
        model = models.CableDetected
        fields = ('id', 'url', 'display', 'type', 'a_terminations', 'b_terminations', 'status', 'tenant', 'label', 'color',
                  'length', 'length_unit', 'tags', 'custom_fields', 'created', 'last_updated',)
##
# Logical
##


class VRFDetectedSerializer(VRFSerializer):
    class Meta:
        model = models.VRFDetected
        fields = [
            'id', 'url', 'display', 'name', 'rd', 'tenant', 'enforce_unique', 'description', 'import_targets',
            'export_targets', 'tags', 'custom_fields', 'created', 'last_updated', 'ipaddress_count', 'prefix_count',
        ]


class VLANDetectedSerializer(VLANSerializer):
    class Meta:
        model = models.VLANDetected
        fields = (
            'id', 'url', 'display', 'site', 'group', 'vid', 'name', 'tenant', 'status', 'role', 'description',
            'l2vpn_termination', 'tags', 'custom_fields', 'created', 'last_updated',
        )


class FHRPGroupDetectedSerializer(FHRPGroupSerializer):
    class Meta:
        model = models.FHRPGroupDetected
        fields = ('id', 'url', 'display', 'protocol', 'group_id', 'auth_type', 'auth_key', 'description', 'ip_addresses',
                  'tags', 'custom_fields', 'created', 'last_updated',)


class ASNDetectedSerializer(ASNSerializer):
    class Meta:
        model = models.ASNDetected
        fields = ('id', 'url', 'display', 'asn', 'rir', 'tenant', 'description', 'site_count', 'provider_count', 'tags',
                  'custom_fields', 'created', 'last_updated',)


class IPAddressDetectedSerializer(IPAddressSerializer):
    class Meta:
        model = models.IPAddressDetected
        fields = ('id', 'url', 'display', 'asn', 'rir', 'tenant', 'description', 'site_count', 'provider_count', 'tags',
                  'custom_fields', 'created', 'last_updated',)


class PrefixDetectedSerializer(PrefixSerializer):
    class Meta:
        model = models.PrefixDetected
        fields = ('id', 'url', 'display', 'family', 'prefix', 'site', 'vrf', 'tenant', 'vlan', 'status', 'role', 'is_pool',
                  'mark_utilized', 'description', 'tags', 'custom_fields', 'created', 'last_updated', 'children', '_depth',)


class WirelessLANDetectedSerializer(WirelessLANSerializer):
    class Meta:
        model = models.WirelessLANDetected
        fields = ('id', 'url', 'display', 'ssid', 'description', 'group', 'vlan', 'tenant', 'auth_type', 'auth_cipher',
                  'auth_psk', 'description', 'tags', 'custom_fields', 'created', 'last_updated',)
