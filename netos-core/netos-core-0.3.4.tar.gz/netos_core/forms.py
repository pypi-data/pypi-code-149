from dcim.models.device_components import InventoryItem
from dcim.models.devices import Device, DeviceType, Manufacturer, Module
from django import forms
from extras.models.tags import Tag
from netbox.forms import NetBoxModelForm
from netbox.forms.base import NetBoxModelFilterSetForm
from utilities.choices import ColorChoices
from utilities.forms.fields.dynamic import DynamicModelChoiceField
from utilities.forms.fields.fields import SlugField
from utilities.forms.widgets import DatePicker

from . import models

##
# Device
##


class NetosHardwareForm(NetBoxModelForm):
    slug = SlugField()

    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all()
    )

    device_type = DynamicModelChoiceField(
        queryset=DeviceType.objects.all()
    )

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

    class Meta:
        model = models.NetosHardware
        fields = (
            'name',
            'slug',
            'device_type',
            'eol_anncouncement',
            'eol_maintanance',
            'eol_support',
            'eol_vulnerability',
            'manufacturer',
            'product_data_sheet',
            'replacement_model',
        )

    def save(self, commit: bool = True):
        try:
            tag = Tag.objects.get(name="EoL Hardware")
        except Tag.DoesNotExist:
            tag = None
        if not tag:
            tag = Tag.objects.create(
                name="EoL Hardware", description="Device has EoL hardware report", color=ColorChoices.COLOR_CYAN)

        if len(self.cleaned_data["device_type"].tags.filter(name="EoL Hardware")) == 0:
            self.cleaned_data["device_type"].tags.add(tag)
        return super().save(commit)


class NetosHardwareFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosHardware
    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False
    )
    device_type = forms.ModelChoiceField(
        queryset=DeviceType.objects.all(),
        required=False
    )
    eol_anncouncement = forms.DateField(required=False, widget=DatePicker())
    eol_maintanance = forms.DateField(required=False, widget=DatePicker())
    eol_support = forms.DateField(required=False, widget=DatePicker())
    eol_vulnerability = forms.DateField(required=False, widget=DatePicker())
    replacement_model = forms.ModelChoiceField(
        queryset=models.NetosHardware.objects.all(),
        required=False
    )

##
# Software
##


class NetosSoftwareForm(NetBoxModelForm):
    slug = SlugField()

    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all()
    )

    device_type = DynamicModelChoiceField(
        queryset=DeviceType.objects.all()
    )

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

    version = forms.CharField(required=False)
    standard_version = forms.CharField(required=False)
    operating_system = forms.CharField(required=False)

    class Meta:
        model = models.NetosSoftware
        fields = (
            'name',
            'slug',
            'device_type',
            'eol_anncouncement',
            'eol_maintanance',
            'eol_support',
            'eol_vulnerability',
            'manufacturer',
            'operating_system',
            'product_data_sheet',
            'replacement_model',
            'standard_version',
            'version',
        )

    def save(self, commit: bool = True):
        try:
            tag = Tag.objects.get(name="EoL Software")
        except Tag.DoesNotExist:
            tag = None
        if not tag:
            tag = Tag.objects.create(
                name="EoL Software", description="Device has EoL software report", color=ColorChoices.COLOR_CYAN)

        if len(self.cleaned_data["device_type"].tags.filter(name="EoL Software")) == 0:
            self.cleaned_data["device_type"].tags.add(tag)
        return super().save(commit)


class NetosSoftwareFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosSoftware
    device_type = forms.ModelChoiceField(
        queryset=DeviceType.objects.all(),
        required=False
    )
    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False
    )

    eol_anncouncement = forms.DateField(required=False, widget=DatePicker())
    eol_maintanance = forms.DateField(required=False, widget=DatePicker())
    eol_support = forms.DateField(required=False, widget=DatePicker())
    eol_vulnerability = forms.DateField(required=False, widget=DatePicker())
    replacement_model = forms.ModelChoiceField(
        queryset=models.NetosSoftware.objects.all(),
        required=False
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


class NetosEoLReportDeviceFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosEoLReportDevice
    site_id = forms.IntegerField(required=False)
    site_id = forms.IntegerField(required=False)
    device_type_id = forms.IntegerField(required=False)
    device_role_id = forms.IntegerField(required=False)
    region_id = forms.IntegerField(required=False)
    manufacturer_id = forms.IntegerField(required=False)
    device_model = forms.CharField(required=False)


class NetosEoLReportModuleFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosEoLReportDevice
    site_id = forms.IntegerField(required=False)
    device_type_id = forms.IntegerField(required=False)
    device_role_id = forms.IntegerField(required=False)
    region_id = forms.IntegerField(required=False)
    manufacturer_id = forms.IntegerField(required=False)
    device_model = forms.CharField(required=False)


class NetosEoLReportInventoryFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosEoLReportDevice
    site_id = forms.IntegerField(required=False)
    device_type_id = forms.IntegerField(required=False)
    device_role_id = forms.IntegerField(required=False)
    region_id = forms.IntegerField(required=False)
    manufacturer_id = forms.IntegerField(required=False)
    device_model = forms.CharField(required=False)
