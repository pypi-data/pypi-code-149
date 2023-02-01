from dcim.filtersets import DeviceFilterSet
from dcim.forms.filtersets import DeviceFilterForm
from netbox.views import generic
from django.db.models import F, Q, Case, When, FloatField
from django.db.models.functions import JSONObject
from django.db.models import BooleanField, ExpressionWrapper, Q
from django.conf import settings

from . import models, tables, filtersets, forms
config = settings.PLUGINS_CONFIG["netos_reporting"]

###
# NetosSoftwareReport
##


class NetosSoftwareReportView(generic.ObjectView):
    queryset = models.NetosSoftwareReport.objects.all()


class NetosSoftwareReportListView(generic.ObjectListView):
    template_name = "netos_reporting/netossoftwarereport_list.html"
    detected_name = config["software_fields"]["detected_software"]
    current_name = config["software_fields"]["current_software"]
    std_name = config["software_fields"]["standard_software"]
    
    # return None for empty otherwise check if equal
    queryset = models.NetosSoftwareReport.objects.annotate(
        compliance=Case(
            When(
                 Q(**{f'custom_field_data__{current_name}': None}),
                 then=None
            ),
            default=ExpressionWrapper(
            Q(custom_field_data__contains=JSONObject(**{current_name: F(f'custom_field_data__{detected_name}')}))|
            Q(custom_field_data__contains=JSONObject(**{current_name: F(f'custom_field_data__{std_name}')})),
            output_field=BooleanField()))
    )
    table = tables.NetosSoftwareReportTable
    filterset = filtersets.NetosSoftwareReportFilterSet
    filterset_form = forms.NetosSoftwareReprotFilterForm


class NetosSoftwareReportDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosSoftwareReport.objects.all()

##
# Reports
##

# Device


class NetosEoLReportListView(generic.ObjectListView):
    queryset = models.NetosEoLReportDevice.objects.all()
    table = tables.NetosEoLReportTable
    template_name = 'netos_reporting/base_report.html'
    filterset = filtersets.NetosEoLReportDeviceFilterSet
    filterset_form = forms.NetosEoLReportDeviceFilterForm

    def get_extra_context(self, request):
        return {
            'active_tab': 'device'
        }


class NetosEoLReportView(generic.ObjectView):
    queryset = models.NetosEoLReportDevice.objects.all()


class NetosEoLReportEditView(generic.ObjectEditView):
    queryset = models.NetosEoLReportDevice.objects.all()
    form = forms.NetosEoLReportForm


class NetosEoLReportDeviceDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosEoLReportDevice.objects.all()

# Module


class NetosEoLReportModuleListView(generic.ObjectListView):
    queryset = models.NetosEoLReportModule.objects.all()
    table = tables.NetosEoLReportModuleTable
    template_name = 'netos_reporting/base_report.html'
    filterset = filtersets.NetosEoLReportModuleFilterSet
    filterset_form = forms.NetosEoLReportModuleFilterForm

    def get_extra_context(self, request):
        return {
            'active_tab': 'module'
        }


class NetosEoLReportModuleView(generic.ObjectView):
    queryset = models.NetosEoLReportModule.objects.all()


class NetosEoLReportModuleEditView(generic.ObjectEditView):
    queryset = models.NetosEoLReportModule.objects.all()
    form = forms.NetosEoLReportModuleForm


class NetosEoLReportModuleDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosEoLReportModule.objects.all()


# Inventory

class NetosEoLReportInventoryListView(generic.ObjectListView):
    queryset = models.NetosEoLReportInventory.objects.all()
    table = tables.NetosEoLReportInventoryTable
    template_name = 'netos_reporting/base_report.html'
    filterset = filtersets.NetosEoLReportInventoryFilterSet
    filterset_form = forms.NetosEoLReportInventoryFilterForm

    def get_extra_context(self, request):
        return {
            'active_tab': 'inventory'
        }


class NetosEoLReportInventoryView(generic.ObjectView):
    queryset = models.NetosEoLReportInventory.objects.all()


class NetosEoLReportInventoryEditView(generic.ObjectEditView):
    queryset = models.NetosEoLReportInventory.objects.all()
    form = forms.NetosEoLReportInventoryForm


class NetosEoLReportInventoryDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosEoLReportInventory.objects.all()
