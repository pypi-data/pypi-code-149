from django.urls import path
from netbox.api.routers import NetBoxRouter

from . import views

app_name = 'netos_core'
router = NetBoxRouter()
##
# Hardware
##
router.register('hardware_device', views.NetosHardwareDeviceViewSet, basename="netoshardwaredevice")
##
# Report
##
router.register('report_device', views.NetosEoLReportDeviceViewSet, basename="netoseolreportdevice")
router.register('report_module', views.NetosEoLReportModuleViewSet, basename="netoseloreportmodule")
router.register('report_inventory', views.NetosEoLReportInventoryViewSet, basename="netoseolreportinventory")
##
# Summary
##
router.register('summary_device', views.NetosSummaryDeviceViewSet, basename = 'netossummarydevice')
router.register('summary_module', views.NetosSummaryModuleViewSet, basename = 'netossummarymodule')
router.register('summary_inventory', views.NetosSummaryInventoryViewSet, basename = 'netossummaryinventory')
##
# Software
##
router.register('software_device', views.NetosSoftwareDeviceViewSet, basename = 'netossoftwaredevice')
router.register('report_collect', views.NetosReportCollectViewSet, basename='netosreportcollect')

urlpatterns = router.urls

#report/collect