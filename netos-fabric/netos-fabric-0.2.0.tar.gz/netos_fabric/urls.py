from django.urls import path

from netbox.views.generic.feature_views import ObjectChangeLogView
from . import models, views

urlpatterns = (

    # Network Fabric
    path('network-fabric/', views.NetworkFabricListView.as_view(), name="networkfabric_list"),
    path('network-fabric/add/', views.NetworkFabricEditView.as_view(), name="networkfabric_add"),
    path('network-fabric/<int:pk>/', views.NetworkFabricView.as_view(), name="networkfabric"),
    path('network-fabric/<int:pk>/edit/', views.NetworkFabricEditView.as_view(), name="networkfabric_edit"),
    path('network-fabric/<int:pk>/delete/', views.NetworkFabricDeleteView.as_view(), name="networkfabric_delete"),
    path('network-fabric/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name="networkfabric_changelog", kwargs={'model': models.NetworkFabric}),
)
