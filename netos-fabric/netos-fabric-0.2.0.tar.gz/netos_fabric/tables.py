from netbox.tables import NetBoxTable
from . import models
import django_tables2 as tables


class NetworkFabricTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = models.NetworkFabric
        fields = (
            'name',
            'slug',
            'ip_address',
            'mac_address',
            'ieee_mac_vendor_prefix',
            'ieee_mac_vendor',
            'device',
            'interface',
            'vlan',
            'prefix',
            'site',
            'region',
            'dns_record',
            'whois',
            'whois_link',
            'last_detected'
        )
        default_columns = (
            'name',
            'slug',
            'vlan',
            'prefix',
            'site',
            'region',
            'dns_record',
            'whois',
            'whois_link',
            'last_detected'
        )
