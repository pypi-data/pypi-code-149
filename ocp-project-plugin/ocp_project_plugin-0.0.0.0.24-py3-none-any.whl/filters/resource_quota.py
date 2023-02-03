import django_filters
from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from ocp_project_plugin.models import AppEnvironment, ResourceQuota


class ResourceQuotaFilter(NetBoxModelFilterSet):
    """Filter capabilities for App Environment instances."""
    app_environment = django_filters.ModelMultipleChoiceFilter(
        field_name='app_environment__app_env',
        queryset=AppEnvironment.objects.all(),
        to_field_name='name',
        label='App Environment (app_env)',
    )

    class Meta:
        model = ResourceQuota
        fields = ["requests_cpu", "requests_memory", "limits_cpu", "limits_memory", "app_environment"]

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
            Q(requests_cpu__icontains=value)
            | Q(requests_memory__icontains=value)
            | Q(limits_cpu__icontains=value)
            | Q(limits_memory__icontains=value)
        )
        return queryset.filter(qs_filter)
