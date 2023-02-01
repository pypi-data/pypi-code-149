from netbox.forms.base import NetBoxModelForm
from netbox.forms.base import NetBoxModelFilterSetForm
from utilities.forms.widgets import DateTimePicker
from utilities.forms.fields.fields import SlugField
from . import models
from django import forms

class NetworkFabricEditForm(NetBoxModelForm):
    slug = SlugField()
    last_detected = forms.DateTimeField(
        required=True,
        widget=DateTimePicker()
    )

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

class NetworkFabricFilterForm(NetBoxModelFilterSetForm):
    model = models.NetworkFabric
