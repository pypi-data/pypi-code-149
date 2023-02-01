from django.urls import path
from netbox.views.generic.feature_views import ObjectChangeLogView

from . import models, views

urlpatterns = (
    ##
    # Hardware
    ##

    path('hardware/', views.NetosHardwareListView.as_view(), name='netoshardware_list'),
    path('hardware/add', views.NetosHardwareEditView.as_view(), name='netoshardware_add'),
    path('hardware/<int:pk>/', views.NetosHardwareView.as_view(), name='netoshardwaredevice'),
    path('hardware/<int:pk>/edit', views.NetosHardwareEditView.as_view(), name='netoshardware_edit'),
    path('hardware/<int:pk>/delete', views.NetosHardwareDeleteView.as_view(), name='netoshardware_delete'),
    path('hardware/<int:pk>/changelog', ObjectChangeLogView.as_view(), name='netoshardware_changelog', kwargs={'model': models.NetosHardware}),
    
    ##
    # Software 
    ##
    path('software/device/', views.NetosSoftwareDeviceListView.as_view(), name="netossoftware_list"),
    path('software/device/add', views.NetosSoftwareDeviceEditView.as_view(), name='netossoftware_add'),
    path('software/device/<int:pk>', views.NetosSoftwareDeviceView.as_view(), name='netossoftwaredevice'),
    path('software/device/<int:pk>/edit', views.NetosSoftwareDeviceEditView.as_view(), name='netossoftware_edit'),
    path('software/device/<int:pk>/delete', views.NetosSoftwareDeviceDeleteView.as_view(), name='netossoftware_delete'),
    path('software/device/<int:pk>/changelog', ObjectChangeLogView.as_view(), name='netossoftware_changelog', kwargs={'model': models.NetosSoftware}),

    ##
    # Report 
    ##

    # Device
    path('report/', views.NetosEoLReportListView.as_view(), name="netoseolreportdevice_list"),
    path('report/add', views.NetosEoLReportEditView.as_view(), name='netoseolreportdevice_add'),
    path('report/<int:pk>', views.NetosEoLReportView.as_view(), name='netoseolreportdevice'),
    path('report/<int:pk>/edit', views.NetosEoLReportEditView.as_view(), name='netoseolreportdevice_edit'),
    path('report/<int:pk>/delete', views.NetosEoLReportDeviceDeleteView.as_view(), name='netoseolreportdevice_delete'),
    path('report/module/<int:pk>/changelog', ObjectChangeLogView.as_view(), name='netoseolreportdevice_changelog', kwargs={'model': models.NetosEoLReportDevice}),

    # Module 
    path('report/module', views.NetosEoLReportModuleListView.as_view(), name="netoseolreportmodule_list"),
    path('report/module/add', views.NetosEoLReportModuleEditView.as_view(), name='netoseolreportmodule_add'),
    path('report/module/<int:pk>', views.NetosEoLReportModuleView.as_view(), name='netoseolreportmodule'),
    path('report/module/<int:pk>/edit', views.NetosEoLReportModuleEditView.as_view(), name='netoseolreportmodule_edit'),
    path('report/module/<int:pk>/delete', views.NetosEoLReportModuleDeleteView.as_view(), name='netoseolreportmodule_delete'),
    path('report/module/<int:pk>/changelog', ObjectChangeLogView.as_view(), name='netoseolreportmodule_changelog', kwargs={'model': models.NetosEoLReportModule}),

    # Inventory 
    path('report/inventory/', views.NetosEoLReportInventoryListView.as_view(), name="netoseolreportinventory_list"),
    path('report/inventory/add', views.NetosEoLReportInventoryEditView.as_view(), name='netoseolreportinventory_add'),
    path('report/inventory/<int:pk>', views.NetosEoLReportInventoryView.as_view(), name='netoseolreportinventory'),
    path('report/inventory/<int:pk>/edit', views.NetosEoLReportInventoryEditView.as_view(), name='netoseolreportinventory_edit'),
    path('report/inventory/<int:pk>/delete', views.NetosEoLReportInventoryDeleteView.as_view(), name='netoseolreportinventory_delete'),
    path('report/inventory/<int:pk>/changelog', ObjectChangeLogView.as_view(), name='netoseolreportinventory_changelog', kwargs={'model': models.NetosEoLReportInventory}),


)
