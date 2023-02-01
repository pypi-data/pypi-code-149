from django.urls import path
from netbox.views.generic.feature_views import (ObjectChangeLogView,
                                                ObjectJournalView)

from . import models, views

urlpatterns = (
    # NetosSoftwareReport
    path('software_report/', views.NetosSoftwareReportListView.as_view(), name='netossoftwarereport_list'),
    path('software_report/<int:pk>', views.NetosSoftwareReportView.as_view(), name='netossoftwarereport'),
    path('software_report/<int:pk>/delete/', views.NetosSoftwareReportDeleteView.as_view(), name='netossoftwarereport_delete'),

    path('software_report/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='netossoftwarereport_changelog', kwargs={'model': models.NetosSoftwareReport}),
    path('software_report/<int:pk>/journal/', ObjectJournalView.as_view(), name='netossoftwarereport_journal', kwargs={'model': models.NetosSoftwareReport}),

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
