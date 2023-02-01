from dcim.models.devices import Device, Module
from django.urls import reverse
from django.conf import settings
from django.db import models


from netbox.models import NetBoxModel
from dcim.models.device_components import Interface, InventoryItem
from ipam.models.fhrp import FHRPGroup
from ipam.models.ip import ASN, IPAddress, Prefix
from ipam.models.vlans import VLAN
from ipam.models.vrfs import VRF
from dcim.models.cables import Cable

from wireless.models import WirelessLAN

config = settings.PLUGINS_CONFIG["netos_inventory"]

class ReconDevice(Device):

    recon_fields = config["device_recon_fields"]

    class Meta:
        verbose_name = "device"
        verbose_name_plural = "devices"
        proxy = True

    def get_absolute_url(self):
        return reverse('plugins:netos_inventory:recondevice', args=[self.pk])

    def __str__(self):
        return super().__str__()

    # @property
    # def detected_type_match(self):
    #     detected_col = self.recon_fields["device_type"]
    #     cf_data = self.custom_field_data.get(detected_col)
    #     match = None
    #     if self.device_type is None or cf_data is None:
    #         match = None
    #     elif self.device_type.pk == cf_data:
    #         match = True
    #     else:
    #         match = False

    #     return match

    # @property
    # def serial_match(self):
    #     detected_col = self.recon_fields["serial"]
    #     cf_data = self.custom_field_data.get(detected_col)
    #     match = None
    #     if self.serial is None or cf_data is None:
    #         match = None
    #     elif self.serial == cf_data:
    #         match = True
    #     else:
    #         match = False

    #     return match


class ReconModule(Module):
    recon_fields = config["device_recon_fields"]

    class Meta:
        verbose_name = "module"
        verbose_name_plural = "modules"
        proxy = True

    def get_absolute_url(self):
        return reverse('plugins:netos_inventory:reconmodule', args=[self.pk])

    def __str__(self):
        return super().__str__()

class ReconInventoryItem(InventoryItem):
    recon_fields = config["device_recon_fields"]

    class Meta:
        verbose_name = "intentory item"
        verbose_name_plural = "inventory items"
        proxy = True

    def get_absolute_url(self):
        return reverse('plugins:netos_inventory:reconinventoryitem', args=[self.pk])

    def __str__(self):
        return super().__str__()
##
# Hardware
##


class DeviceDetected(Device):
    class Meta:
        verbose_name = "device detected"
        verbose_name_plural = "devices detected"
        proxy = True


class InterfaceDetected(Interface):
    class Meta:
        verbose_name = "interface detected"
        verbose_name_plural = "interfaces detected"
        proxy = True


class InventoryItemDetected(InventoryItem):
    class Meta:
        verbose_name = "inventory_item_detected"
        verbose_name_plural = "inventory_items_detected"
        proxy = True


class ModuleDetected(Module):
    class Meta:
        verbose_name = "module_detected"
        verbose_name_plural = "modules detected"
        proxy = True


class CableDetected(Cable):
    class Meta:
        verbose_name = "cable detected"
        verbose_name_plural = "cables detected"
        proxy = True

##
# Logical
##


class VRFDetected(VRF):
    class Meta:
        verbose_name = "vrf detected"
        verbose_name_plural = "vrfs detected"
        proxy = True


class VLANDetected(VLAN):
    class Meta:
        verbose_name = "vlan detected"
        verbose_name_plural = "vlans detected"
        proxy = True


class FHRPGroupDetected(FHRPGroup):
    class Meta:
        verbose_name = "fhrp group detected"
        verbose_name_plural = "fhrp groups detected"
        proxy = True


class ASNDetected(ASN):
    class Meta:
        verbose_name = "ans detected"
        verbose_name_plural = "ans detected"
        proxy = True


class IPAddressDetected(IPAddress):
    class Meta:
        verbose_name = "ip address detected"
        verbose_name_plural = "ip addresses detected"
        proxy = True


class PrefixDetected(Prefix):
    class Meta:
        verbose_name = "prefix detected"
        verbose_name_plural = "prefixes detected"
        proxy = True


class WirelessLANDetected(WirelessLAN):
    class Meta:
        verbose_name = "wireless lan detected"
        verbose_name_plural = "wireless lans detected"
        proxy = True

##
# LAN Report
##
class LANConsolidationReport(Device):
    class Meta:
        verbose_name = "LAN consolidation report"
        verbose_name_plural = "LAN consolidation reports"
        proxy = True
