from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.routers import APIRootView

from netbox.api.viewsets import NetBoxModelViewSet

from ocp_project_plugin.api.serializers import AppEnvironmentSerializer, OCPProjectSerializer, ResourceQuotaSerializer
from ocp_project_plugin.filters import AppEnvironmentFilter, OCPProjectFilter, ResourceQuotaFilter
from ocp_project_plugin.models import AppEnvironment, OCPProject, ResourceQuota


class OCPProjectPluginRootView(APIRootView):
    """
    OCP Project Plugin API root view
    """

    def get_view_name(self):
        return "OCPProjectPlugin"


class AppEnvironmentViewSet(NetBoxModelViewSet):
    queryset = AppEnvironment.objects.all()
    serializer_class = AppEnvironmentSerializer
    filterset_class = AppEnvironmentFilter

    @action(detail=True, methods=["get"])
    def appenvironment(self, request, pk=None):
        appenvironment = AppEnvironment.objects.filter(appenvironment__id=pk)
        serializer = AppEnvironmentSerializer(appenvironment, many=True, context={"request": request})
        return Response(serializer.data)


class OCPProjectViewSet(NetBoxModelViewSet):
    queryset = OCPProject.objects.all()
    serializer_class = OCPProjectSerializer
    filterset_class = OCPProjectFilter

    @action(detail=True, methods=["get"])
    def ocpproject(self, request, pk=None):
        ocpproject = OCPProject.objects.filter(ocpproject__id=pk)
        serializer = OCPProjectSerializer(ocpproject, many=True, context={"request": request})
        return Response(serializer.data)


class ResourceQuotaViewSet(NetBoxModelViewSet):
    queryset = ResourceQuota.objects.all()
    serializer_class = ResourceQuotaSerializer
    filterset_class = ResourceQuotaFilter

    @action(detail=True, methods=["get"])
    def resourcequota(self, request, pk=None):
        resourcequota = ResourceQuota.objects.filter(resourcequota__id=pk)
        serializer = ResourceQuotaSerializer(resourcequota, many=True, context={"request": request})
        return Response(serializer.data)
