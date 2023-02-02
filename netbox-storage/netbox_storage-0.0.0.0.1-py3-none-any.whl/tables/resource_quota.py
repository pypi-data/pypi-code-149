import django_tables2 as tables

from netbox.tables import (
    NetBoxTable,
    ToggleColumn,
)

from ocp_project_plugin.models import OCPProject, ResourceQuota


class ResourceQuotaTable(NetBoxTable):
    """Table for displaying Resource Quota objects."""

    requests_cpu = tables.Column(
        linkify=True
    )
    requests_memory = tables.Column(
        linkify=True
    )
    limits_cpu = tables.Column(
        linkify=True
    )
    limits_memory = tables.Column(
        linkify=True
    )
    app_environment = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = ResourceQuota

        fields = ["requests_cpu", "requests_memory", "limits_cpu", "limits_memory", "app_environment"]

        default_columns = ["requests_cpu", "requests_memory", "limits_cpu", "limits_memory", "app_environment"]
