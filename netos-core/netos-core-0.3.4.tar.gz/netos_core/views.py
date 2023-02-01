from netbox.views import generic

from . import filtersets, forms, models, tables

##
# Hardware
##

# Device


class NetosHardwareView(generic.ObjectView):
    queryset = models.NetosHardware.objects.all()


class NetosHardwareListView(generic.ObjectListView):
    queryset = models.NetosHardware.objects.all()
    table = tables.NetosHardwareTable
    filterset = filtersets.NetosHardwareFilterSet
    filterset_form = forms.NetosHardwareFilterForm


class NetosHardwareEditView(generic.ObjectEditView):
    queryset = models.NetosHardware.objects.all()
    form = forms.NetosHardwareForm


class NetosHardwareDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosHardware.objects.all()


##
# Software
##
class NetosSoftwareDeviceView(generic.ObjectView):
    queryset = models.NetosSoftware.objects.all()


class NetosSoftwareDeviceListView(generic.ObjectListView):
    queryset = models.NetosSoftware.objects.all()
    table = tables.NetosSoftwareDeviceTable
    filterset = filtersets.NetosSoftwareFilterSet
    filterset_form = forms.NetosSoftwareFilterForm


class NetosSoftwareDeviceEditView(generic.ObjectEditView):
    queryset = models.NetosSoftware.objects.all()
    form = forms.NetosSoftwareForm


class NetosSoftwareDeviceDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosSoftware.objects.all()


##
# Reports
##

# Device


class NetosEoLReportListView(generic.ObjectListView):
    queryset = models.NetosEoLReportDevice.objects.all()
    table = tables.NetosEoLReportTable
    template_name = 'netos_core/base_report.html'
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
    template_name = 'netos_core/base_report.html'
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
    template_name = 'netos_core/base_report.html'
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
