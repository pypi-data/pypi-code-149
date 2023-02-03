from rest_framework.serializers import HyperlinkedIdentityField

from netbox.api.serializers import NetBoxModelSerializer
from ocp_project_plugin.api.nested_serializers import NestedAppEnvironmentSerializer, NestedOCPProjectSerializer
from ocp_project_plugin.models import AppEnvironment, OCPProject, ResourceQuota
from tenancy.api.nested_serializers import NestedTenantSerializer, NestedContactSerializer


class AppEnvironmentSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(view_name="plugins-api:ocp_project_plugin-api:appenvironment-detail")
    ocp_project = NestedOCPProjectSerializer(required=False, allow_null=True)

    class Meta:
        model = AppEnvironment
        fields = ["url", "id", "app_env", "mtls", "repo", "branch", "path", "egress_ip", "helm", "monitoring",
                  "postgres_monitoring", "kustomize", "ocp_project", "created", "last_updated", "custom_fields"]


class OCPProjectSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(view_name="plugins-api:ocp_project_plugin-api:ocpproject-detail")
    customer = NestedTenantSerializer()
    contact = NestedContactSerializer()
    owner = NestedContactSerializer()

    class Meta:
        model = OCPProject
        fields = ["url", "id", "name", "description", "display_name", "owner", "contact", "customer", "docu_url",
                  "workload", "request", "created", "last_updated", "custom_fields"]


class ResourceQuotaSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(view_name="plugins-api:ocp_project_plugin-api:resourcequota-detail")
    app_environment = NestedAppEnvironmentSerializer()

    class Meta:
        model = ResourceQuota
        fields = ["url", "id", "requests_cpu", "requests_memory", "limits_cpu", "limits_memory", "app_environment",
                  "created", "last_updated", "custom_fields"]
