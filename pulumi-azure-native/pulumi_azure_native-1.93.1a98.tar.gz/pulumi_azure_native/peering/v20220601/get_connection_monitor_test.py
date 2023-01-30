# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetConnectionMonitorTestResult',
    'AwaitableGetConnectionMonitorTestResult',
    'get_connection_monitor_test',
    'get_connection_monitor_test_output',
]

@pulumi.output_type
class GetConnectionMonitorTestResult:
    """
    The Connection Monitor Test class.
    """
    def __init__(__self__, destination=None, destination_port=None, id=None, is_test_successful=None, name=None, path=None, provisioning_state=None, source_agent=None, test_frequency_in_sec=None, type=None):
        if destination and not isinstance(destination, str):
            raise TypeError("Expected argument 'destination' to be a str")
        pulumi.set(__self__, "destination", destination)
        if destination_port and not isinstance(destination_port, int):
            raise TypeError("Expected argument 'destination_port' to be a int")
        pulumi.set(__self__, "destination_port", destination_port)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_test_successful and not isinstance(is_test_successful, bool):
            raise TypeError("Expected argument 'is_test_successful' to be a bool")
        pulumi.set(__self__, "is_test_successful", is_test_successful)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if path and not isinstance(path, list):
            raise TypeError("Expected argument 'path' to be a list")
        pulumi.set(__self__, "path", path)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if source_agent and not isinstance(source_agent, str):
            raise TypeError("Expected argument 'source_agent' to be a str")
        pulumi.set(__self__, "source_agent", source_agent)
        if test_frequency_in_sec and not isinstance(test_frequency_in_sec, int):
            raise TypeError("Expected argument 'test_frequency_in_sec' to be a int")
        pulumi.set(__self__, "test_frequency_in_sec", test_frequency_in_sec)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def destination(self) -> Optional[str]:
        """
        The Connection Monitor test destination
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[int]:
        """
        The Connection Monitor test destination port
        """
        return pulumi.get(self, "destination_port")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isTestSuccessful")
    def is_test_successful(self) -> bool:
        """
        The flag that indicates if the Connection Monitor test is successful or not.
        """
        return pulumi.get(self, "is_test_successful")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> Sequence[str]:
        """
        The path representing the Connection Monitor test.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourceAgent")
    def source_agent(self) -> Optional[str]:
        """
        The Connection Monitor test source agent
        """
        return pulumi.get(self, "source_agent")

    @property
    @pulumi.getter(name="testFrequencyInSec")
    def test_frequency_in_sec(self) -> Optional[int]:
        """
        The Connection Monitor test frequency in seconds
        """
        return pulumi.get(self, "test_frequency_in_sec")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetConnectionMonitorTestResult(GetConnectionMonitorTestResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectionMonitorTestResult(
            destination=self.destination,
            destination_port=self.destination_port,
            id=self.id,
            is_test_successful=self.is_test_successful,
            name=self.name,
            path=self.path,
            provisioning_state=self.provisioning_state,
            source_agent=self.source_agent,
            test_frequency_in_sec=self.test_frequency_in_sec,
            type=self.type)


def get_connection_monitor_test(connection_monitor_test_name: Optional[str] = None,
                                peering_service_name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectionMonitorTestResult:
    """
    The Connection Monitor Test class.


    :param str connection_monitor_test_name: The name of the connection monitor test
    :param str peering_service_name: The name of the peering service.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['connectionMonitorTestName'] = connection_monitor_test_name
    __args__['peeringServiceName'] = peering_service_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:peering/v20220601:getConnectionMonitorTest', __args__, opts=opts, typ=GetConnectionMonitorTestResult).value

    return AwaitableGetConnectionMonitorTestResult(
        destination=__ret__.destination,
        destination_port=__ret__.destination_port,
        id=__ret__.id,
        is_test_successful=__ret__.is_test_successful,
        name=__ret__.name,
        path=__ret__.path,
        provisioning_state=__ret__.provisioning_state,
        source_agent=__ret__.source_agent,
        test_frequency_in_sec=__ret__.test_frequency_in_sec,
        type=__ret__.type)


@_utilities.lift_output_func(get_connection_monitor_test)
def get_connection_monitor_test_output(connection_monitor_test_name: Optional[pulumi.Input[str]] = None,
                                       peering_service_name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConnectionMonitorTestResult]:
    """
    The Connection Monitor Test class.


    :param str connection_monitor_test_name: The name of the connection monitor test
    :param str peering_service_name: The name of the peering service.
    :param str resource_group_name: The name of the resource group.
    """
    ...
