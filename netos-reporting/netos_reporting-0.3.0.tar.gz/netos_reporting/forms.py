from dcim.models.devices import DeviceRole, DeviceType
from django import forms
from dcim.forms.filtersets import DeviceFilterForm
from dcim.forms.filtersets import ModuleFilterForm
from dcim.models.sites import Site, Region
from dcim.models.device_components import InventoryItemRole
from utilities.forms.fields.dynamic import DynamicModelMultipleChoiceField
from utilities.forms.widgets import StaticSelect
from utilities.forms.constants import BOOLEAN_WITH_BLANK_CHOICES
from dcim.models.device_components import InventoryItem
from dcim.models.devices import Device, DeviceType, Manufacturer, Module
from django import forms
from netbox.forms import NetBoxModelForm
from netbox.forms.base import NetBoxModelFilterSetForm
from utilities.forms.widgets import DatePicker
from django.utils.translation import gettext as _

from . import models


###
# Filter
###
class NetosSoftwareReprotFilterForm(DeviceFilterForm):
    model = models.NetosSoftwareReport

    fieldsets = (
        (None, ('q', 'tag', 'compliance')),
        ('Location', ('region_id', 'site_group_id',
         'site_id', 'location_id', 'rack_id')),
        ('Operation', ('status', 'role_id', 'airflow',
         'serial', 'asset_tag', 'mac_address')),
        ('Hardware', ('manufacturer_id', 'device_type_id', 'platform_id')),
        ('Tenant', ('tenant_group_id', 'tenant_id')),
        ('Contacts', ('contact', 'contact_role', 'contact_group')),
        ('Components', (
            'console_ports', 'console_server_ports', 'power_ports', 'power_outlets', 'interfaces', 'pass_through_ports',
        )),
        ('Miscellaneous', ('has_primary_ip',
         'virtual_chassis_member', 'local_context_data'))
    )

    compliance = forms.NullBooleanField(
        required=False,
        label='Is software compliant',
        widget=StaticSelect(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )

##
# Report
##


class NetosEoLReportBaseForm(NetBoxModelForm):
    eol_anncouncement = forms.DateField(
        required=True,
        widget=DatePicker()
    )

    eol_maintanance = forms.DateField(
        required=True,
        widget=DatePicker()
    )

    eol_vulnerability = forms.DateField(
        required=True,
        widget=DatePicker()
    )

    eol_support = forms.DateField(
        required=True,
        widget=DatePicker()
    )


class NetosEoLReportForm(NetosEoLReportBaseForm):

    device = forms.ModelChoiceField(
        queryset=Device.objects.all()
    )

    class Meta:
        model = models.NetosEoLReportDevice
        fields = (
            'eol_anncouncement',
            'eol_maintanance',
            'eol_vulnerability',
            'eol_support',
            'device'
        )


class NetosEoLReportModuleForm(NetosEoLReportBaseForm):
    device = forms.ModelChoiceField(
        queryset=Module.objects.all()
    )

    class Meta:
        model = models.NetosEoLReportModule
        fields = (
            'eol_anncouncement',
            'eol_maintanance',
            'eol_vulnerability',
            'eol_support',
            'device'
        )


class NetosEoLReportInventoryForm(NetosEoLReportBaseForm):
    device = forms.ModelChoiceField(
        queryset=InventoryItem.objects.all()
    )

    class Meta:
        model = models.NetosEoLReportInventory
        fields = (
            'eol_anncouncement',
            'eol_maintanance',
            'eol_vulnerability',
            'eol_support',
            'device'
        )


class NetosEoLReportDeviceFilterForm(DeviceFilterForm):
    model = models.NetosEoLReportDevice


class NetosEoLReportModuleFilterForm(ModuleFilterForm):
    model = models.NetosEoLReportDevice
    fieldsets = (
        (None, ('q', 'site_id', 'device_type_id',
         'device_role_id', 'region_id', 'device_model')),
        ('Hardware', ('manufacturer_id', 'module_type_id', 'serial', 'asset_tag')),
    )

    site_id = DynamicModelMultipleChoiceField(
        queryset=Site.objects.all(),
        required=False
    )
    device_type_id = DynamicModelMultipleChoiceField(
        queryset=DeviceType.objects.all(),
        required=False
    )
    device_role_id = DynamicModelMultipleChoiceField(
        queryset=DeviceRole.objects.all(),
        required=False
    )
    region_id = forms.IntegerField(required=False)
    device_model = forms.CharField(required=False)


class NetosEoLReportInventoryFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosEoLReportDevice
    fieldsets = (
        (None, ('q',  )),
        ('Attributes', ('role_id', 'manufacturer_id', 'serial')),
        ('Device', ('region_id', 'site_id', 'device_type_id', 'device_role_id')),
    )
    role_id = DynamicModelMultipleChoiceField(
        queryset=InventoryItemRole.objects.all(),
        required=False,
        label=_('Role'),
        fetch_trigger='open'
    )
    manufacturer_id = DynamicModelMultipleChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        label=_('Manufacturer')
    )
    serial = forms.CharField(
        required=False
    )

    site_id = DynamicModelMultipleChoiceField(
        queryset=Site.objects.all(),
        required=False
    )
    device_type_id = DynamicModelMultipleChoiceField(
        queryset=DeviceType.objects.all(),
        required=False
    )
    device_role_id = DynamicModelMultipleChoiceField(
        queryset=DeviceRole.objects.all(),
        required=False
    )
    region_id = DynamicModelMultipleChoiceField(
        queryset=Region.objects.all(),
        required=False
    )
    device_model = forms.CharField(required=False)
