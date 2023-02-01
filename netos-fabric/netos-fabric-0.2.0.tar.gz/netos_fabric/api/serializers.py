from netbox.api.serializers import NetBoxModelSerializer
from .. import models

class NetworkFabricSerializer(NetBoxModelSerializer):
    class Meta:
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
