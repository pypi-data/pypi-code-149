from ocp_project_plugin.models import AppEnvironment, OCPProject, ResourceQuota
from netbox.search import SearchIndex, register_search


@register_search
class AppEnvironmentIndex(SearchIndex):
    model = AppEnvironment
    fields = (
        ('app_env', 100),
        ('mtls', 100),
        ('repo', 100),
        ('branch', 100),
        ('path', 100),
        ('egress_ip', 100),
        ('helm', 100),
        ('monitoring', 100),
        ('postgres_monitoring', 100),
        ('kustomize', 100),
    )


@register_search
class OCPProjectIndex(SearchIndex):
    model = OCPProject
    fields = (
        ('name', 100),
        ('description', 100),
        ('display_name', 100),
        ('owner', 100),
        ('contact', 100),
        ('customer', 100),
        ('url', 100),
        ('workload', 100),
        ('request', 100),
    )


@register_search
class ResourceQuotaIndex(SearchIndex):
    model = ResourceQuota
    fields = (
        ('requests_cpu', 100),
        ('requests_memory', 100),
        ('limits_cpu', 100),
        ('limits_memory', 100),
    )
