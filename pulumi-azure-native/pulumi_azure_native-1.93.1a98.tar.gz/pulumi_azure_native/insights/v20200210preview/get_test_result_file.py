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
    'GetTestResultFileResult',
    'AwaitableGetTestResultFileResult',
    'get_test_result_file',
    'get_test_result_file_output',
]

@pulumi.output_type
class GetTestResultFileResult:
    """
    Test result.
    """
    def __init__(__self__, data=None, next_link=None):
        if data and not isinstance(data, str):
            raise TypeError("Expected argument 'data' to be a str")
        pulumi.set(__self__, "data", data)
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)

    @property
    @pulumi.getter
    def data(self) -> Optional[str]:
        """
        File contents.
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        The URI that can be used to request the next section of the result file in the event the file is too large for a single request.
        """
        return pulumi.get(self, "next_link")


class AwaitableGetTestResultFileResult(GetTestResultFileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTestResultFileResult(
            data=self.data,
            next_link=self.next_link)


def get_test_result_file(continuation_token: Optional[str] = None,
                         download_as: Optional[str] = None,
                         geo_location_id: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         test_successful_criteria: Optional[bool] = None,
                         time_stamp: Optional[int] = None,
                         web_test_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTestResultFileResult:
    """
    Test result.


    :param str continuation_token: The continuation token.
    :param str download_as: The format to use when returning the webtest result.
    :param str geo_location_id: The location ID where the webtest was physically run.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param bool test_successful_criteria: The success state criteria for the webtest result.
    :param int time_stamp: The posix (epoch) time stamp for the webtest result.
    :param str web_test_name: The name of the Application Insights webtest resource.
    """
    __args__ = dict()
    __args__['continuationToken'] = continuation_token
    __args__['downloadAs'] = download_as
    __args__['geoLocationId'] = geo_location_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['testSuccessfulCriteria'] = test_successful_criteria
    __args__['timeStamp'] = time_stamp
    __args__['webTestName'] = web_test_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20200210preview:getTestResultFile', __args__, opts=opts, typ=GetTestResultFileResult).value

    return AwaitableGetTestResultFileResult(
        data=__ret__.data,
        next_link=__ret__.next_link)


@_utilities.lift_output_func(get_test_result_file)
def get_test_result_file_output(continuation_token: Optional[pulumi.Input[Optional[str]]] = None,
                                download_as: Optional[pulumi.Input[str]] = None,
                                geo_location_id: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                test_successful_criteria: Optional[pulumi.Input[Optional[bool]]] = None,
                                time_stamp: Optional[pulumi.Input[int]] = None,
                                web_test_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTestResultFileResult]:
    """
    Test result.


    :param str continuation_token: The continuation token.
    :param str download_as: The format to use when returning the webtest result.
    :param str geo_location_id: The location ID where the webtest was physically run.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param bool test_successful_criteria: The success state criteria for the webtest result.
    :param int time_stamp: The posix (epoch) time stamp for the webtest result.
    :param str web_test_name: The name of the Application Insights webtest resource.
    """
    ...
