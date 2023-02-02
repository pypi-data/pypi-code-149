from netbox.api.routers import NetBoxRouter
from ocp_project_plugin.api.views import OCPProjectPluginRootView, AppEnvironmentViewSet, OCPProjectViewSet, \
    ResourceQuotaViewSet

router = NetBoxRouter()
router.APIRootView = OCPProjectPluginRootView

router.register("appenvironment", AppEnvironmentViewSet)
router.register("ocpproject", OCPProjectViewSet)
router.register("resourcequota", ResourceQuotaViewSet)

urlpatterns = router.urls
