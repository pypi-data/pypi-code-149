from django.db import models
from dcim.fields import MACAddressField
from ipam.fields import IPAddressField
from netbox.models import NetBoxModel
from django.urls import reverse

##
# Fabric
##
class NetworkFabric(NetBoxModel):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    ip_address = IPAddressField(
        help_text='IPv4 or IPv6 address (with mask)'
    )

    mac_address = MACAddressField(
        null=True,
        blank=True,
        verbose_name='MAC Address'
    )

    ieee_mac_vendor_prefix = models.CharField(
        max_length=30,
        verbose_name='IEEE MAC Vendor Prefix'
    )

    ieee_mac_vendor = models.CharField(
        max_length=100,
        verbose_name='IEEE MAC Vendor'
    )

    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='fabric'
    )

    interface = models.ForeignKey(
        to='dcim.Interface',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='fabric'
    )

    vlan = models.ForeignKey(
        to='ipam.VLAN',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='fabric'
    )

    prefix = models.ForeignKey(
        to='ipam.Prefix',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='fabric'
    )

    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='fabric'
    )

    region = models.ForeignKey(
        to='dcim.Region',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='fabric'
    )

    dns_record = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    whois = models.CharField(max_length=400)

    whois_link = models.URLField()

    last_detected = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('plugins:netos_fabric:networkfabric', kwargs={'pk': self.pk})

    
    def __str__(self):
        return self.name
