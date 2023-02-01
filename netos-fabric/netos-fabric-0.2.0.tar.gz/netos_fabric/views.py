from . import models, tables, forms, filtersets
from netbox.views import generic


class NetworkFabricListView(generic.ObjectListView):
    queryset = models.NetworkFabric.objects.all()
    table = tables.NetworkFabricTable
    filterset = filtersets.NetworkFabricFilterSet
    filterset_form = forms.NetworkFabricFilterForm

class NetworkFabricEditView(generic.ObjectEditView):
    queryset = models.NetworkFabric.objects.all()
    form = forms.NetworkFabricEditForm

class NetworkFabricDeleteView(generic.ObjectDeleteView):
    queryset = models.NetworkFabric.objects.all()

class NetworkFabricView(generic.ObjectView):
    queryset = models.NetworkFabric.objects.all()
