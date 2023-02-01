from django.urls import path

from netbox.views.generic.feature_views import ObjectChangeLogView
from . import models, views

urlpatterns = (
    # Recon device
    path('recondevice/', views.ReconDeviceListView.as_view(), name='recondevice_list'),
    path('recondevice/recon/', views.ReconDeviceBulkReconView.as_view(), name='recondevice_recon'),

    path('recondevice/<int:pk>/', views.ReconDeviceView.as_view(), name='recondevice'),
    path('recondevice/<int:pk>/edit/', views.ReconDeviceEditView.as_view(), name='recondevice_edit'),
    path('recondevice/<int:pk>/delete/', views.ReconDeviceDeleteView.as_view(), name='recondevice_delete'),
    path('recondevice/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='recondevice_changelog', kwargs={'model': models.ReconDevice}),

    # Recon module
    path('reconmodule/', views.ReconModuleListView.as_view(), name='reconmodule_list'),
    path('reconmodule/recon/', views.ReconModuleBulkReconView.as_view(), name='reconmodule_recon'),

    path('reconmodule/<int:pk>/', views.ReconModuleView.as_view(), name='reconmodule'),
    path('reconmodule/<int:pk>/edit/', views.ReconModuleEditView.as_view(), name='reconmodule_edit'),
    path('reconmodule/<int:pk>/delete/', views.ReconModuleDeleteView.as_view(), name='reconmodule_delete'),
    path('reconmodule/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='reconmodule_changelog', kwargs={'model': models.ReconModule}),

    # Recon inventory item
    path('reconinventoryitem/', views.ReconInventoryItemListView.as_view(), name='reconinventoryitem_list'),
    path('reconinventoryitem/recon/', views.ReconInventoryItemBulkReconView.as_view(), name='reconinventoryitem_recon'),

    path('reconinventoryitem/<int:pk>/', views.ReconInventoryItemView.as_view(), name='reconinventoryitem'),
    path('reconinventoryitem/<int:pk>/edit/', views.ReconInventoryItemEditView.as_view(), name='reconinventoryitem_edit'),
    path('reconinventoryitem/<int:pk>/delete/', views.ReconInventoryItemDeleteView.as_view(), name='reconinventoryitem_delete'),
    path('reconinventoryitem/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='reconinventoryitem_changelog', kwargs={'model': models.ReconInventoryItem}),


    # Logical Last Detected
    path('vrf-detected/', views.VRFDetectedListView.as_view(), name="vrfdetected_list"),
    path('vrf-detected/delete', views.VRFDetectedBulkDeleteView.as_view(), name="vrfdetected_bulk_delete"),
    path('vrf-detected/edit', views.VRFDetectedBulkEditView.as_view(), name="vrfdetected_bulk_edit"),

    path('vlan-detected/', views.VLANDetectedListView.as_view(), name="vlandetected_list"),
    path('vlan-detected/delete', views.VLANDetectedBulkDeleteView.as_view(), name="vlandetected_bulk_delete"),
    path('vlan-detected/edit', views.VLANDetectedBulkEditView.as_view(), name="vlandetected_bulk_edit"),

    path('fhrpgroup-detected/', views.FHRPGroupDetectedListView.as_view(), name="fhrpgroupdetected_list"),
    path('fhrpgroup-detected/delete', views.FHRPGroupDetectedBulkDeleteView.as_view(), name="fhrpgroupdetected_bulk_delete"),
    path('fhrpgroup-detected/edit', views.FHRPGroupDetectedBulkEditView.as_view(), name="fhrpgroupdetected_bulk_edit"),

    path('asn-detected/', views.ASNDetectedListView.as_view(), name="asndetected_list"),
    path('asn-detected/delete', views.ASNDetectedBulkDeleteView.as_view(), name="asndetected_bulk_delete"),
    path('asn-detected/edit', views.ASNDetectedBulkEditView.as_view(), name="asndetected_bulk_edit"),

    path('ipaddress-detected/', views.IPAddressDetectedListView.as_view(), name="ipaddressdetected_list"),
    path('ipaddress-detected/delete', views.IPAddressDetectedBulkDeleteView.as_view(), name="ipaddressdetected_bulk_delete"),
    path('ipaddress-detected/edit', views.IPAddressDetectedBulkEditView.as_view(), name="ipaddressdetected_bulk_edit"),

    path('prefix-detected/', views.PrefixDetectedListView.as_view(), name="prefixdetected_list"),
    path('prefix-detected/delete', views.PrefixDetectedBulkDeleteView.as_view(), name="prefixdetected_bulk_delete"),
    path('prefix-detected/edit', views.PrefixDetectedBulkEditView.as_view(), name="prefixdetected_bulk_edit"),

    path('wirelesslan-detected/', views.WirelessLANDetectedListView.as_view(), name="wirelesslandetected_list"),
    path('wirelesslan-detected/delete', views.WirelessLANDetectedBulkDeleteView.as_view(), name="wirelesslandetected_bulk_delete"),
    path('wirelesslan-detected/edit', views.WirelessLANDetectedBulkEditView.as_view(), name="wirelesslandetected_bulk_edit"),

    # Hardware Last Detected
    path('device-detected/', views.DeviceDetectedListView.as_view(), name="devicedetected_list"),
    path('device-detected/delete/', views.DeviceDetectedBulkDeleteView.as_view(), name='devicedetected_bulk_delete'),
    path('device-detected/edit/', views.DeviceDetectedBulkEditView.as_view(), name='devicedetected_bulk_edit'),

    path('interface-detected/', views.InterfaceDetectedListView.as_view(), name="interfacedetected_list"),
    path('interface-detected/delete', views.InterfaceDetectedBulkDeleteView.as_view(), name="interfacedetected_bulk_delete"),
    path('interface-detected/edit', views.InterfaceDetectedBulkEditView.as_view(), name="interfacedetected_bulk_edit"),

    path('module-detected/', views.ModuleDetectedListView.as_view(), name="moduledetected_list"),
    path('module-detected/delete', views.ModuleDetectedBulkDeleteView.as_view(), name="moduledetected_bulk_delete"),
    path('module-detected/edit', views.ModuleDetectedBulkEditView.as_view(), name="moduledetected_bulk_edit"),

    path('cable-detected/', views.CableDetectedListView.as_view(), name="cabledetected_list"),
    path('cable-detected/delete', views.CableDetectedBulkDeleteView.as_view(), name="cabledetected_bulk_delete"),
    path('cable-detected/edit', views.CableDetectedBulkEditView.as_view(), name="cabledetected_bulk_edit"),

    # LAN Consolidation Report
    path('lanconsolidationreport/', views.LANConsolidationReportListView.as_view(), name="lanconsolidationreport_list"),
    #path('lanconsolidationreport/<int:pk>/edit/', views.LANConsolidationReportListView.as_view(), name="lanconsolidationreport_edit"),
    #path('lanconsolidationreport/<int:pk>/delete/', views.LANConsolidationReportDeleteView.as_view(), name="lanconsolidationreport_delete"),
    #path('lanconsolidationreport/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name="lanconsolidationreport_changelog", kwargs={'model': models.LANConsolidationReport}),

)
