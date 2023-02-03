from netbox.views.generic import ObjectView, ObjectListView, ObjectEditView, ObjectDeleteView, BulkImportView, \
    BulkEditView, BulkDeleteView

from ocp_project_plugin.filters import ResourceQuotaFilter
from ocp_project_plugin.forms import (
    ResourceQuotaImportForm,
    ResourceQuotaFilterForm,
    ResourceQuotaForm,
    ResourceQuotaBulkEditForm
)
from ocp_project_plugin.models import ResourceQuota
from ocp_project_plugin.tables import ResourceQuotaTable


class ResourceQuotaListView(ObjectListView):
    queryset = ResourceQuota.objects.all()
    filterset = ResourceQuotaFilter
    filterset_form = ResourceQuotaFilterForm
    table = ResourceQuotaTable


class ResourceQuotaView(ObjectView):
    """Display Resource Quota details"""

    queryset = ResourceQuota.objects.all()


class ResourceQuotaEditView(ObjectEditView):
    """View for editing Resource Quota instance."""

    queryset = ResourceQuota.objects.all()
    form = ResourceQuotaForm
    default_return_url = "plugins:ocp_project_plugin:resourcequota_list"


class ResourceQuotaDeleteView(ObjectDeleteView):
    queryset = ResourceQuota.objects.all()
    default_return_url = "plugins:ocp_project_plugin:resourcequota_list"


class ResourceQuotaBulkImportView(BulkImportView):
    queryset = ResourceQuota.objects.all()
    model_form = ResourceQuotaImportForm
    table = ResourceQuotaTable
    default_return_url = "plugins:ocp_project_plugin:resourcequota_list"


class ResourceQuotaBulkEditView(BulkEditView):
    queryset = ResourceQuota.objects.all()
    filterset = ResourceQuotaFilter
    table = ResourceQuotaTable
    form = ResourceQuotaBulkEditForm


class ResourceQuotaBulkDeleteView(BulkDeleteView):
    queryset = ResourceQuota.objects.all()
    table = ResourceQuotaTable
