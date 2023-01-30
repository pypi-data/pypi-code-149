# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetKubernetesRoleResult',
    'AwaitableGetKubernetesRoleResult',
    'get_kubernetes_role',
    'get_kubernetes_role_output',
]

@pulumi.output_type
class GetKubernetesRoleResult:
    """
    The limited preview of Kubernetes Cluster Management from the Azure supports:
    1. Using a simple turn-key option in Azure Portal, deploy a Kubernetes cluster on your Azure Stack Edge device. 
    2. Configure Kubernetes cluster running on your device with Arc enabled Kubernetes with a click of a button in the Azure Portal. 
     Azure Arc enables organizations to view, manage, and govern their on-premises Kubernetes clusters using the Azure Portal, command line tools, and APIs.
    3. Easily configure Persistent Volumes using SMB and NFS shares for storing container data. 
     For more information, refer to the document here: https://databoxupdatepackages.blob.core.windows.net/documentation/Microsoft-Azure-Stack-Edge-K8-Cloud-Management-20210323.pdf 
     Or Demo: https://databoxupdatepackages.blob.core.windows.net/documentation/Microsoft-Azure-Stack-Edge-K8S-Cloud-Management-20210323.mp4
     By using this feature, you agree to the preview legal terms. See the https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/
    """
    def __init__(__self__, host_platform=None, host_platform_type=None, id=None, kind=None, kubernetes_cluster_info=None, kubernetes_role_resources=None, name=None, provisioning_state=None, role_status=None, system_data=None, type=None):
        if host_platform and not isinstance(host_platform, str):
            raise TypeError("Expected argument 'host_platform' to be a str")
        pulumi.set(__self__, "host_platform", host_platform)
        if host_platform_type and not isinstance(host_platform_type, str):
            raise TypeError("Expected argument 'host_platform_type' to be a str")
        pulumi.set(__self__, "host_platform_type", host_platform_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if kubernetes_cluster_info and not isinstance(kubernetes_cluster_info, dict):
            raise TypeError("Expected argument 'kubernetes_cluster_info' to be a dict")
        pulumi.set(__self__, "kubernetes_cluster_info", kubernetes_cluster_info)
        if kubernetes_role_resources and not isinstance(kubernetes_role_resources, dict):
            raise TypeError("Expected argument 'kubernetes_role_resources' to be a dict")
        pulumi.set(__self__, "kubernetes_role_resources", kubernetes_role_resources)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if role_status and not isinstance(role_status, str):
            raise TypeError("Expected argument 'role_status' to be a str")
        pulumi.set(__self__, "role_status", role_status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> str:
        """
        Host OS supported by the Kubernetes role.
        """
        return pulumi.get(self, "host_platform")

    @property
    @pulumi.getter(name="hostPlatformType")
    def host_platform_type(self) -> str:
        """
        Platform where the runtime is hosted.
        """
        return pulumi.get(self, "host_platform_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Role type.
        Expected value is 'Kubernetes'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="kubernetesClusterInfo")
    def kubernetes_cluster_info(self) -> 'outputs.KubernetesClusterInfoResponse':
        """
        Kubernetes cluster configuration
        """
        return pulumi.get(self, "kubernetes_cluster_info")

    @property
    @pulumi.getter(name="kubernetesRoleResources")
    def kubernetes_role_resources(self) -> 'outputs.KubernetesRoleResourcesResponse':
        """
        Kubernetes role resources
        """
        return pulumi.get(self, "kubernetes_role_resources")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        State of Kubernetes deployment
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> str:
        """
        Role status.
        """
        return pulumi.get(self, "role_status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of Role
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")


class AwaitableGetKubernetesRoleResult(GetKubernetesRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKubernetesRoleResult(
            host_platform=self.host_platform,
            host_platform_type=self.host_platform_type,
            id=self.id,
            kind=self.kind,
            kubernetes_cluster_info=self.kubernetes_cluster_info,
            kubernetes_role_resources=self.kubernetes_role_resources,
            name=self.name,
            provisioning_state=self.provisioning_state,
            role_status=self.role_status,
            system_data=self.system_data,
            type=self.type)


def get_kubernetes_role(device_name: Optional[str] = None,
                        name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKubernetesRoleResult:
    """
    The limited preview of Kubernetes Cluster Management from the Azure supports:
    1. Using a simple turn-key option in Azure Portal, deploy a Kubernetes cluster on your Azure Stack Edge device.
    2. Configure Kubernetes cluster running on your device with Arc enabled Kubernetes with a click of a button in the Azure Portal.
        Azure Arc enables organizations to view, manage, and govern their on-premises Kubernetes clusters using the Azure Portal, command line tools, and APIs.
    3. Easily configure Persistent Volumes using SMB and NFS shares for storing container data.
        For more information, refer to the document here: https://databoxupdatepackages.blob.core.windows.net/documentation/Microsoft-Azure-Stack-Edge-K8-Cloud-Management-20210323.pdf
        Or Demo: https://databoxupdatepackages.blob.core.windows.net/documentation/Microsoft-Azure-Stack-Edge-K8S-Cloud-Management-20210323.mp4
        By using this feature, you agree to the preview legal terms. See the https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/


    :param str device_name: The device name.
    :param str name: The role name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20220401preview:getKubernetesRole', __args__, opts=opts, typ=GetKubernetesRoleResult).value

    return AwaitableGetKubernetesRoleResult(
        host_platform=__ret__.host_platform,
        host_platform_type=__ret__.host_platform_type,
        id=__ret__.id,
        kind=__ret__.kind,
        kubernetes_cluster_info=__ret__.kubernetes_cluster_info,
        kubernetes_role_resources=__ret__.kubernetes_role_resources,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        role_status=__ret__.role_status,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_kubernetes_role)
def get_kubernetes_role_output(device_name: Optional[pulumi.Input[str]] = None,
                               name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKubernetesRoleResult]:
    """
    The limited preview of Kubernetes Cluster Management from the Azure supports:
    1. Using a simple turn-key option in Azure Portal, deploy a Kubernetes cluster on your Azure Stack Edge device.
    2. Configure Kubernetes cluster running on your device with Arc enabled Kubernetes with a click of a button in the Azure Portal.
        Azure Arc enables organizations to view, manage, and govern their on-premises Kubernetes clusters using the Azure Portal, command line tools, and APIs.
    3. Easily configure Persistent Volumes using SMB and NFS shares for storing container data.
        For more information, refer to the document here: https://databoxupdatepackages.blob.core.windows.net/documentation/Microsoft-Azure-Stack-Edge-K8-Cloud-Management-20210323.pdf
        Or Demo: https://databoxupdatepackages.blob.core.windows.net/documentation/Microsoft-Azure-Stack-Edge-K8S-Cloud-Management-20210323.mp4
        By using this feature, you agree to the preview legal terms. See the https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/


    :param str device_name: The device name.
    :param str name: The role name.
    :param str resource_group_name: The resource group name.
    """
    ...
