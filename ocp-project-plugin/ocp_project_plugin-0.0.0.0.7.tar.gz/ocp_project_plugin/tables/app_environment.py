import django_tables2 as tables

from netbox.tables import (
    NetBoxTable,
    ToggleColumn,
)

from ocp_project_plugin.models import AppEnvironment


class AppEnvironmentTable(NetBoxTable):
    """Table for displaying App Environment objects."""

    pk = ToggleColumn()
    app_env = tables.Column(
        linkify=True
    )
    mtls = tables.Column(
        linkify=True
    )
    repo = tables.Column(
        linkify=True
    )
    branch = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = AppEnvironment

        fields = ["pk", "app_env", "mtls", "repo", "branch", "path", "egress_ip", "helm", "monitoring",
                  "postgres_monitoring", "kustomize", "ocp_project"]

        default_columns = ["app_env", "mtls", "repo", "branch", "path", "egress_ip", "helm", "monitoring",
                           "postgres_monitoring", "kustomize", "ocp_project"]
