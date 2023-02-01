from netbox.filtersets import NetBoxModelFilterSet
from . import models

class NetworkFabricFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.NetworkFabric
        fields = (            
            'name',
            'slug',
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
