from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netos_fabric'

router = NetBoxRouter()
router.register('network-fabric', views.NetworkFabricSViewSet)

urlpatterns = router.urls
