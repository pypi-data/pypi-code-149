import datetime as dt

from dcim.models.device_components import InventoryItem
from dcim.models.devices import Device, Module
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel


##
# Hardware
##
class NetosHardware(NetBoxModel):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    product_data_sheet = models.URLField(
        blank=True,
        null=True,
        verbose_name='Product Data Sheet URL',
    )
    eol_anncouncement = models.DateField(null=False)
    eol_maintanance = models.DateField(null=False)
    eol_vulnerability = models.DateField(null=False)
    eol_support = models.DateField(null=False)

    manufacturer = models.ForeignKey(
        to='dcim.Manufacturer',
        on_delete=models.PROTECT,
        related_name='+',
        null=False
    )

    device_type = models.ForeignKey(
        to='dcim.DeviceType',
        on_delete=models.PROTECT,
        related_name='netos_hardware'
    )

    replacement_model = models.ForeignKey(
        to='NetosHardware',
        on_delete=models.PROTECT,
        related_name='+',
        null=True,
        blank=True
    )

    @property
    def eol_maintanance_days(self) -> int:
        return (self.eol_maintanance - dt.datetime.now().date()).days

    @property
    def eol_vulnerability_days(self) -> int:
        return (self.eol_vulnerability - dt.datetime.now().date()).days

    @property
    def eol_support_days(self) -> int:
        return (self.eol_support - dt.datetime.now().date()).days

    @property
    def eol_anncouncement_days(self) -> int:
        return (self.eol_anncouncement - dt.datetime.now().date()).days

    def get_absolute_url(self):
        return reverse('plugins:netos_core:netoshardwaredevice', args=[self.pk])

    def __str__(self):
        return self.name

##
# Software
##
class NetosSoftware(NetBoxModel):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    product_data_sheet = models.URLField(
        blank=True,
        null=True,
        verbose_name='Product Data Sheet URL',
    )
    eol_anncouncement = models.DateField(null=False)
    eol_maintanance = models.DateField(null=False)
    eol_vulnerability = models.DateField(null=False)
    eol_support = models.DateField(null=False)

    version = models.CharField(max_length=50)
    standard_version = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=100)

    manufacturer = models.ForeignKey(
        to='dcim.Manufacturer',
        on_delete=models.PROTECT,
        related_name='+',
        null=False
    )

    device_type = models.ForeignKey(
        to='dcim.DeviceType',
        on_delete=models.PROTECT,
        related_name='netos_software'
    )

    replacement_model = models.ForeignKey(
        to='NetosSoftware',
        on_delete=models.PROTECT,
        related_name='+',
        null=True,
        blank=True
    )

    @property
    def eol_maintanance_days(self) -> int:
        return (self.eol_maintanance - dt.datetime.now().date()).days

    @property
    def eol_vulnerability_days(self) -> int:
        return (self.eol_vulnerability - dt.datetime.now().date()).days

    @property
    def eol_support_days(self) -> int:
        return (self.eol_support - dt.datetime.now().date()).days

    @property
    def eol_anncouncement_days(self) -> int:
        return (self.eol_anncouncement - dt.datetime.now().date()).days

    def get_absolute_url(self):
        return reverse('plugins:netos_core:netossoftwaredevice', args=[self.pk])

    def __str__(self):
        return self.name
##
# Report
##


class NetosEoLReportBase(NetBoxModel):
    class Meta:
        abstract = True


    eol_anncouncement = models.DateField(null=False)
    eol_maintanance = models.DateField(null=False)
    eol_vulnerability = models.DateField(null=False)
    eol_support = models.DateField(null=False)

    created = models.DateTimeField(auto_now_add=True)

    @property
    def eol_anncouncement_days(self) -> int:
        return (self.eol_anncouncement - self.created.date()).days

    @property
    def eol_maintanance_days(self) -> int:
        return (self.eol_maintanance - self.created.date()).days

    @property
    def eol_vulnerability_days(self) -> int:
        return (self.eol_vulnerability - self.created.date()).days

    @property
    def eol_support_days(self) -> int:
        return (self.eol_support - self.created.date()).days

    @property
    def inner_device(self):
        obj = self.device
        if isinstance(obj, Device):
            return obj
        elif isinstance(obj, Module):
            return obj.device
        elif isinstance(obj, InventoryItem):
            return obj.device
        else:
            return None

    @property
    def device_type(self):
        if self.inner_device:
            return str(self.inner_device.device_type)
        else:
            return None

    @property
    def device_type_id(self):
        if self.inner_device and self.inner_device.device_type:
            return self.inner_device.device_type.id
        else:
            return None

    @property
    def device_model(self):
        if self.inner_device and self.inner_device.device_type:
            return self.inner_device.device_type.model
        else:
            return None

    @property
    def device_model_id(self):
        if self.inner_device and self.inner_device.device_type:
            return self.inner_device.device_type.model
        else:
            return None

    @property
    def site(self):
        if self.inner_device:
            return str(self.inner_device.site)
        else:
            return None

    @property
    def site_id(self):
        if self.inner_device and self.inner_device.site:
            return self.inner_device.site.id
        else:
            return None

    @property
    def location(self):
        if self.inner_device:
            return str(self.inner_device.location)
        else:
            return None

    @property
    def location_id(self):
        if self.inner_device and self.inner_device.location:
            return self.inner_device.location.id
        else:
            return None

    @property
    def device_role(self):
        if self.inner_device:
            return str(self.inner_device.device_role)
        else:
            return None

    @property
    def device_role_id(self):
        if self.inner_device and self.inner_device.device_role:
            return self.inner_device.device_role.id
        else:
            return None

    @property
    def manufacturer_display(self):
        if self.inner_device and self.inner_device.device_type:
            return str(self.inner_device.device_type.manufacturer)
        else:
            return None

    @property
    def manufacturer_id(self):
        if self.inner_device and self.inner_device.device_type:
            return str(self.inner_device.device_type.manufacturer_id)
        else:
            return None

    @property
    def region_id(self):
        if self.inner_device and self.inner_device.site and self.inner_device.site.region:
            return self.inner_device.site.region.id
        else:
            return None

    @property
    def region(self):
        if self.inner_device and self.inner_device.site:
            return str(self.inner_device.site.region)
        else:
            return None


class NetosEoLReportDevice(NetosEoLReportBase):
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT,
        related_name='netos_report'
    )

    def get_absolute_url(self):
        return reverse('plugins:netos_core:netoseolreportdevice', args=[self.pk])


class NetosEoLReportModule(NetosEoLReportBase):
    device = models.ForeignKey(
        to='dcim.Module',
        on_delete=models.PROTECT,
        related_name='netos_report'
    )

    def get_absolute_url(self):
        return reverse('plugins:netos_core:netoseolreportmodule', args=[self.pk])


class NetosEoLReportInventory(NetosEoLReportBase):
    device = models.ForeignKey(
        to='dcim.InventoryItem',
        on_delete=models.PROTECT,
        related_name='netos_report'
    )

    class Meta:
        verbose_name_plural = "Netos EoL Report Inventories"

    def get_absolute_url(self):
        return reverse('plugins:netos_core:netoseolreportinventory', args=[self.pk])
