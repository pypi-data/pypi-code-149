from netbox.views.generic import ObjectView, ObjectListView, ObjectEditView, ObjectDeleteView, BulkImportView, \
    BulkEditView, BulkDeleteView

from ocp_project_plugin.filters import OCPProjectFilter
from ocp_project_plugin.forms import (
    OCPProjectImportForm,
    OCPProjectFilterForm,
    OCPProjectForm,
    OCPProjectBulkEditForm
)
from ocp_project_plugin.models import OCPProject
from ocp_project_plugin.tables import OCPProjectTable


class OCPProjectListView(ObjectListView):
    queryset = OCPProject.objects.all()
    filterset = OCPProjectFilter
    filterset_form = OCPProjectFilterForm
    table = OCPProjectTable


class OCPProjectView(ObjectView):
    """Display OCP Project details"""
    template_name = 'ocp_project_plugin/ocp_project/ocp_project.html'
    queryset = OCPProject.objects.all()


class OCPProjectEditView(ObjectEditView):
    """View for editing OCP Project instance."""

    queryset = OCPProject.objects.all()
    form = OCPProjectForm
    default_return_url = "plugins:ocp_project_plugin:ocpproject_list"


class OCPProjectDeleteView(ObjectDeleteView):
    queryset = OCPProject.objects.all()
    default_return_url = "plugins:ocp_project_plugin:ocpproject_list"


class OCPProjectBulkImportView(BulkImportView):
    queryset = OCPProject.objects.all()
    model_form = OCPProjectImportForm
    table = OCPProjectTable
    default_return_url = "plugins:ocp_project_plugin:ocpproject_list"


class OCPProjectBulkEditView(BulkEditView):
    queryset = OCPProject.objects.all()
    filterset = OCPProjectFilter
    table = OCPProjectTable
    form = OCPProjectBulkEditForm


class OCPProjectBulkDeleteView(BulkDeleteView):
    queryset = OCPProject.objects.all()
    table = OCPProjectTable
