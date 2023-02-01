from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netos_inventory'

router = NetBoxRouter()
router.register('recondevice', views.ReconDeviceViewSet)
router.register('reconmodule', views.ReconModuleViewSet)
router.register('reconinventoryitem', views.ReconInventoryItemViewSet)
router.register('vrfdetected', views.VRFDetectedViewSet)
urlpatterns = router.urls
