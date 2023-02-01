from netbox.api.routers import NetBoxRouter

from . import views

app_name = 'netos_reporting'
router = NetBoxRouter()
router.register('software_report',  views.NetosSoftwareReportViewSet)

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


urlpatterns = router.urls
