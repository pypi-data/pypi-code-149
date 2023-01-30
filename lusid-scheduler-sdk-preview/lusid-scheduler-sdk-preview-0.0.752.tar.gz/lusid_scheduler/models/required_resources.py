# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.752
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_scheduler.configuration import Configuration


class RequiredResources(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'lusid_apis': 'list[str]',
        'lusid_file_system': 'list[str]',
        'external_calls': 'list[str]'
    }

    attribute_map = {
        'lusid_apis': 'lusidApis',
        'lusid_file_system': 'lusidFileSystem',
        'external_calls': 'externalCalls'
    }

    required_map = {
        'lusid_apis': 'optional',
        'lusid_file_system': 'optional',
        'external_calls': 'optional'
    }

    def __init__(self, lusid_apis=None, lusid_file_system=None, external_calls=None, local_vars_configuration=None):  # noqa: E501
        """RequiredResources - a model defined in OpenAPI"
        
        :param lusid_apis:  List of LUSID APIs the job needs access to
        :type lusid_apis: list[str]
        :param lusid_file_system:  List of S3 bucket or folder names that the job can access
        :type lusid_file_system: list[str]
        :param external_calls:  External URLs that the job can call
        :type external_calls: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._lusid_apis = None
        self._lusid_file_system = None
        self._external_calls = None
        self.discriminator = None

        self.lusid_apis = lusid_apis
        self.lusid_file_system = lusid_file_system
        self.external_calls = external_calls

    @property
    def lusid_apis(self):
        """Gets the lusid_apis of this RequiredResources.  # noqa: E501

        List of LUSID APIs the job needs access to  # noqa: E501

        :return: The lusid_apis of this RequiredResources.  # noqa: E501
        :rtype: list[str]
        """
        return self._lusid_apis

    @lusid_apis.setter
    def lusid_apis(self, lusid_apis):
        """Sets the lusid_apis of this RequiredResources.

        List of LUSID APIs the job needs access to  # noqa: E501

        :param lusid_apis: The lusid_apis of this RequiredResources.  # noqa: E501
        :type lusid_apis: list[str]
        """

        self._lusid_apis = lusid_apis

    @property
    def lusid_file_system(self):
        """Gets the lusid_file_system of this RequiredResources.  # noqa: E501

        List of S3 bucket or folder names that the job can access  # noqa: E501

        :return: The lusid_file_system of this RequiredResources.  # noqa: E501
        :rtype: list[str]
        """
        return self._lusid_file_system

    @lusid_file_system.setter
    def lusid_file_system(self, lusid_file_system):
        """Sets the lusid_file_system of this RequiredResources.

        List of S3 bucket or folder names that the job can access  # noqa: E501

        :param lusid_file_system: The lusid_file_system of this RequiredResources.  # noqa: E501
        :type lusid_file_system: list[str]
        """

        self._lusid_file_system = lusid_file_system

    @property
    def external_calls(self):
        """Gets the external_calls of this RequiredResources.  # noqa: E501

        External URLs that the job can call  # noqa: E501

        :return: The external_calls of this RequiredResources.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_calls

    @external_calls.setter
    def external_calls(self, external_calls):
        """Sets the external_calls of this RequiredResources.

        External URLs that the job can call  # noqa: E501

        :param external_calls: The external_calls of this RequiredResources.  # noqa: E501
        :type external_calls: list[str]
        """

        self._external_calls = external_calls

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RequiredResources):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequiredResources):
            return True

        return self.to_dict() != other.to_dict()
