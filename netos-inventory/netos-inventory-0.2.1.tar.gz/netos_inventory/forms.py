from dcim.forms.bulk_edit import DeviceBulkEditForm, ModuleBulkEditForm, InventoryItemBulkEditForm, CableBulkEditForm, InterfaceBulkEditForm
from ipam.forms.bulk_edit import VRFBulkEditForm, VLANBulkEditForm, FHRPGroupBulkEditForm, ASNBulkEditForm, IPAddressBulkEditForm, PrefixBulkEditForm
from dcim.forms.filtersets import DeviceFilterForm
from dcim.forms.model_forms import DeviceForm, ModuleForm, InventoryItemForm
from dcim.forms.filtersets import ModuleFilterForm
from dcim.forms.filtersets import InventoryItemFilterForm
from dcim.models.sites import Site, Region
from netbox.forms.base import NetBoxModelBulkEditForm
from utilities.forms.fields.dynamic import DynamicModelChoiceField
from utilities.forms.constants import BOOLEAN_WITH_BLANK_CHOICES
from utilities.forms.widgets import StaticSelect
from . import models
from django import forms
from netbox.forms.base import NetBoxModelFilterSetForm
from utilities.forms import widgets
from django.utils.translation import gettext as _

###
# Device
###
class ReconDeviceFilterForm(DeviceFilterForm):

    fieldsets = (
        (None, ('q', 'tag')),
        ('Location', ('region_id', 'site_group_id', 'site_id', 'location_id', 'rack_id')),
        ('Operation', ('status', 'role_id', 'airflow', 'serial', 'asset_tag', 'mac_address')),
        ('Hardware', ('manufacturer_id', 'device_type_id', 'platform_id')),
        ('Tenant', ('tenant_group_id', 'tenant_id')),
        ('Contacts', ('contact', 'contact_role', 'contact_group')),
        ('Components', (
            'console_ports', 'console_server_ports', 'power_ports', 'power_outlets', 'interfaces', 'pass_through_ports',
        )),
        ('Miscellaneous', ('has_primary_ip', 'virtual_chassis_member', 'local_context_data', 'serial_match'
        '', 'device_type_match', 'netos_software_kickstart_version_match', 'netos_software_version_match', 'netos_hostname_match'))
    )

    serial_match = forms.NullBooleanField(
        required=False,
        label='Serial match',
        widget=StaticSelect(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )
    device_type_match = forms.NullBooleanField(
        required=False,
        label='Device type match',
        widget=StaticSelect(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )
    netos_software_kickstart_version_match = forms.NullBooleanField(
        required=False,
        label='Software kickstart version match',
        widget=StaticSelect(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )
    netos_software_version_match = forms.NullBooleanField(
        required=False,
        label='Software version match',
        widget=StaticSelect(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )
    netos_hostname_match = forms.NullBooleanField(
        required=False,
        label='Hostname match',
        widget=StaticSelect(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )

    model = models.ReconDevice


class ReconDeviceEditForm(DeviceForm):
    model = models.ReconDevice


class ReconDeviceBulkEditForm(DeviceBulkEditForm):
    model = models.ReconDevice

###
# Module
###
class ReconModuleFilterForm(ModuleFilterForm):
    fieldsets = (
        (None, ('q', 'tag', 'serial_match', 'site_id', 'region_id')),
        ('Hardware', ('manufacturer_id', 'module_type_id', 'serial', 'asset_tag')),
    )

    serial_match = forms.NullBooleanField(
        required=False,
        label='Serial match',
        widget=StaticSelect(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )

    site_id = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
        label=_('Site')
    )

    region_id = DynamicModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        label=_('Region')
    )

    model = models.ReconModule


class ReconModuleEditForm(ModuleForm):
    model = models.ReconModule


class ReconModuleBulkEditForm(ModuleBulkEditForm):
    model = models.ReconModule

###
# Inventory Item
###
class ReconInventoryItemFilterForm(InventoryItemFilterForm):
    fieldsets = (
        (None, ('q', 'tag', 'serial_match')),
        ('Attributes', ('name', 'label', 'role_id', 'manufacturer_id', 'serial', 'asset_tag', 'discovered')),
        ('Device', ('region_id', 'site_group_id', 'site_id', 'location_id', 'rack_id', 'virtual_chassis_id', 'device_id')),
    )

    serial_match = forms.NullBooleanField(
        required=False,
        label='Serial match',
        widget=StaticSelect(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )

    model = models.ReconInventoryItem


class ReconInventoryItemEditForm(InventoryItemForm):
    model = models.ReconInventoryItem


class ReconInventoryItemBulkEditForm(InventoryItemBulkEditForm):
    model = models.ReconInventoryItem



class LANConsolidationReportEditForm(DeviceForm):
    model = models.LANConsolidationReport


###
# Filter
###
class BaseLastPolledFilterForm(NetBoxModelFilterSetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove default field
        del self.custom_fields["cf_Netos_Last_Polled"]
        del self.fields["cf_Netos_Last_Polled"]

    cf_Netos_Last_Polled__lte = forms.DateField(
        label="Last Polled",
        widget=widgets.DatePicker(),
        required=False,
        help_text="Last polled date marks when model was last time updated.\
            Filter out objects with last polled date older than selected one.")

###
# Hardware Last Detected
###

class DeviceDetectedFilterForm(BaseLastPolledFilterForm):
    model = models.DeviceDetected

class InterfaceDetectedFilterForm(BaseLastPolledFilterForm):
    model = models.InterfaceDetected


class ModuleDetectedFilterForm(BaseLastPolledFilterForm):
    model = models.ModuleDetected


class CableDetectedFilterForm(BaseLastPolledFilterForm):
    model = models.CableDetected

###
# Logical Last Detected
###

class VRFDetectedFilterForm(BaseLastPolledFilterForm):
    model = models.VRFDetected

class VLANDetectedFilterForm(BaseLastPolledFilterForm):
    model = models.VLANDetected

class FHRPGroupDetectedFilterForm(BaseLastPolledFilterForm):
    model = models.FHRPGroupDetected

class ASNDetectedFilterForm(BaseLastPolledFilterForm):
    model = models.ASNDetected

class IPAddressDetectedFilterForm(BaseLastPolledFilterForm):
    model = models.IPAddressDetected

class PrefixDetectedFilterForm(BaseLastPolledFilterForm):
    model = models.PrefixDetected

class WirelessLANDetectedFilterForm(BaseLastPolledFilterForm):
    model = models.WirelessLANDetected


class VRFDetectedBulkEditForm(VRFBulkEditForm):
    model = models.VRFDetected

class VLANDetectedBulkEditForm(VLANBulkEditForm):
    model = models.VLANDetected

class FHRPGroupDetectedBulkEditForm(FHRPGroupBulkEditForm):
    model = models.FHRPGroupDetected

class ASNDetectedBulkEditForm(ASNBulkEditForm):
    model = models.ASNDetected

class IPAddressDetectedBulkEditForm(IPAddressBulkEditForm):
    model = models.IPAddressDetected

class PrefixDetectedBulkEditForm(PrefixBulkEditForm):
    model = models.PrefixDetected

class WirelessLANDetectedBulkEditForm(NetBoxModelBulkEditForm):
    model = models.WirelessLANDetected

###
# Hardware
##
class DeviceDetectedBulkEditForm(DeviceBulkEditForm):
    model = models.DeviceDetected

class InterfaceDetectedBulkEditForm(InterfaceBulkEditForm):
    model = models.InterfaceDetected

class ModuleDetectedBulkEditForm(ModuleBulkEditForm):
    model = models.ModuleDetected

class CableDetectedBulkEditForm(CableBulkEditForm):
    model = models.CableDetected


##
# LAN Report
##
class LANConsolidationReportFilterForm(DeviceFilterForm):

    fieldsets = (
        (None, ('q', 'tag', 'utilization')),
        ('Location', ('region_id', 'site_group_id', 'site_id', 'location_id', 'rack_id')),
        ('Operation', ('status', 'role_id', 'airflow', 'serial', 'asset_tag', 'mac_address')),
        ('Hardware', ('manufacturer_id', 'device_type_id', 'platform_id')),
        ('Tenant', ('tenant_group_id', 'tenant_id')),
        ('Contacts', ('contact', 'contact_role', 'contact_group')),
        ('Components', (
            'console_ports', 'console_server_ports', 'power_ports', 'power_outlets', 'interfaces', 'pass_through_ports',
        )),
        ('Miscellaneous', ('has_primary_ip', 'virtual_chassis_member', 'local_context_data'))
    )

    utilization = forms.IntegerField(
        label="Port Utilization",
        required=False,
        help_text="Percentage of enabled ports on the device. Filter out devices with utilization less than given number.")
    
    model = models.LANConsolidationReport
