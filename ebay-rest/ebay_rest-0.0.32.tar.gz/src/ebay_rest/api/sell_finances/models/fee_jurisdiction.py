# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: v1.15.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FeeJurisdiction(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'region_name': 'str',
        'region_type': 'str'
    }

    attribute_map = {
        'region_name': 'regionName',
        'region_type': 'regionType'
    }

    def __init__(self, region_name=None, region_type=None):  # noqa: E501
        """FeeJurisdiction - a model defined in Swagger"""  # noqa: E501
        self._region_name = None
        self._region_type = None
        self.discriminator = None
        if region_name is not None:
            self.region_name = region_name
        if region_type is not None:
            self.region_type = region_type

    @property
    def region_name(self):
        """Gets the region_name of this FeeJurisdiction.  # noqa: E501

        String value that indicates the name of the region to which a region-specific fee applies.<br><br>The set of valid <b>regionName</b> values that may be returned is determined by the <b>regionType</b> value.<br><br><span class=\"tablenote\"><strong>Note:</strong> Currently, supported <b>regionName</b> values that may be returned are standard two-character country or state codes.<br><br>Typical examples include:<ul><li><b>MX</b> [Mexico]</li><li><b>IN</b> [India]</li><li><b>US</b> [United States]</li><li>CA [California]</li><li>VT [Vermont]</li><li>ME [Maine]</li></ul></span>  # noqa: E501

        :return: The region_name of this FeeJurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this FeeJurisdiction.

        String value that indicates the name of the region to which a region-specific fee applies.<br><br>The set of valid <b>regionName</b> values that may be returned is determined by the <b>regionType</b> value.<br><br><span class=\"tablenote\"><strong>Note:</strong> Currently, supported <b>regionName</b> values that may be returned are standard two-character country or state codes.<br><br>Typical examples include:<ul><li><b>MX</b> [Mexico]</li><li><b>IN</b> [India]</li><li><b>US</b> [United States]</li><li>CA [California]</li><li>VT [Vermont]</li><li>ME [Maine]</li></ul></span>  # noqa: E501

        :param region_name: The region_name of this FeeJurisdiction.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def region_type(self):
        """Gets the region_type of this FeeJurisdiction.  # noqa: E501

        The enumeration value returned here indicates the type of region that is collecting the corresponding fee. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/finances/types/pay:RegionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The region_type of this FeeJurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._region_type

    @region_type.setter
    def region_type(self, region_type):
        """Sets the region_type of this FeeJurisdiction.

        The enumeration value returned here indicates the type of region that is collecting the corresponding fee. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/finances/types/pay:RegionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param region_type: The region_type of this FeeJurisdiction.  # noqa: E501
        :type: str
        """

        self._region_type = region_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FeeJurisdiction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FeeJurisdiction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
