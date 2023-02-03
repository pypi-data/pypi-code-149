from django.forms import (
    CharField,
)

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from ocp_project_plugin.models import ResourceQuota


class ResourceQuotaForm(NetBoxModelForm):
    """Form for creating a new Resource Quota object."""
    limits_cpu = CharField(
        label="Limits CPU",
        help_text="E.g. 2",
    )
    limits_memory = CharField(
        label="Limits Memory",
        help_text="E.g. 200Mi",
    )
    requests_cpu = CharField(
        label="Request CPU",
        help_text="E.g. 1",
    )
    requests_memory = CharField(
        label="Request Memory",
        help_text="E.g. 100Mi",
    )

    class Meta:
        model = ResourceQuota

        fields = ["requests_cpu", "requests_memory", "limits_cpu", "limits_memory", "app_environment"]


class ResourceQuotaFilterForm(NetBoxModelFilterSetForm):
    """Form for filtering App Environment instances."""

    model = ResourceQuota

    limits_cpu = CharField(
        required=False,
        label="Limits CPU",
        help_text="E.g. 2",
    )
    limits_memory = CharField(
        required=False,
        label="Limits Memory",
        help_text="E.g. 200Mi",
    )
    requests_cpu = CharField(
        required=False,
        label="Request CPU",
        help_text="E.g. 1",
    )
    requests_memory = CharField(
        required=False,
        label="Request Memory",
        help_text="E.g. 100Mi",
    )


class ResourceQuotaImportForm(NetBoxModelImportForm):
    limits_cpu = CharField(
        label="Limits CPU",
        help_text="E.g. 2",
    )
    limits_memory = CharField(
        label="Limits Memory",
        help_text="E.g. 200Mi",
    )
    requests_cpu = CharField(
        label="Request CPU",
        help_text="E.g. 1",
    )
    requests_memory = CharField(
        label="Request Memory",
        help_text="E.g. 100Mi",
    )

    class Meta:
        model = ResourceQuota

        fields = ["requests_cpu", "requests_memory", "limits_cpu", "limits_memory", "app_environment"]


class ResourceQuotaBulkEditForm(NetBoxModelBulkEditForm):
    model = ResourceQuota

    limits_cpu = CharField(
        required=False,
        label="Limits CPU",
        help_text="E.g. 2",
    )
    limits_memory = CharField(
        required=False,
        label="Limits Memory",
        help_text="E.g. 200Mi",
    )
    requests_cpu = CharField(
        required=False,
        label="Request CPU",
        help_text="E.g. 1",
    )
    requests_memory = CharField(
        required=False,
        label="Request Memory",
        help_text="E.g. 100Mi",
    )
