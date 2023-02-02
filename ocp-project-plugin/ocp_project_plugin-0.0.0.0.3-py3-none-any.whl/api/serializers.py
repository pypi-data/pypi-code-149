from rest_framework.serializers import HyperlinkedIdentityField

from netbox.api.serializers import NetBoxModelSerializer
from ocp_project_plugin.api.nested_serializers import NestedAppEnvironmentSerializer, NestedOCPProjectSerializer
from ocp_project_plugin.models import AppEnvironment, OCPProject, ResourceQuota


class AppEnvironmentSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(view_name="plugins-api:ocp_project_plugin-api:appenvironment-detail")
    drive = NestedOCPProjectSerializer(required=False, allow_null=True)

    class Meta:
        model = AppEnvironment
        fields = ["id", "app_env", "mtls", "repo", "branch", "path", "egress_ip", "helm", "monitoring",
                  "postgres_monitoring", "kustomize", "ocp_project", "created", "last_updated", "custom_fields"]


class OCPProjectSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(view_name="plugins-api:ocp_project_plugin-api:ocpproject-detail")

    class Meta:
        model = OCPProject
        fields = ["id", "name", "description", "display_name", "owner", "contact", "customer", "url", "workload",
                  "request", "created", "last_updated", "custom_fields"]


class ResourceQuotaSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(view_name="plugins-api:ocp_project_plugin-api:resourcequota-detail")
    drive = NestedAppEnvironmentSerializer(required=False, allow_null=True)

    class Meta:
        model = ResourceQuota
        fields = ["id", "requests_cpu", "requests_memory", "limits_cpu", "limits_memory", "app_environment", "created",
                  "last_updated", "custom_fields"]
