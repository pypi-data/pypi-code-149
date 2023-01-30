# coding: utf-8

"""
    Logistics API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The <b>Logistics API</b> resources offer the following capabilities: <ul><li><b>shipping_quote</b> &ndash; Consolidates into a list a set of live shipping rates, or quotes, from which you can select a rate to ship a package.</li> <li><b>shipment</b> &ndash; Creates a \"shipment\" for the selected shipping rate.</li></ul> Call <b>createShippingQuote</b> to get a list of live shipping rates. The rates returned are all valid for a specific time window and all quoted prices are at eBay-negotiated rates. <br><br>Select one of the live rates and using its associated <b>rateId</b>, create a \"shipment\" for the package by calling <b>createFromShippingQuote</b>. Creating a shipment completes an agreement, and the cost of the base service and any added shipping options are summed into the returned <b>totalShippingCost</b> value. This action also generates a shipping label that you can use to ship the package.  The total cost of the shipment is incurred when the package is shipped using the supplied shipping label.  <p class=\"tablenote\"><b>Important!</b> Sellers must set up a payment method via their eBay account before they can use the methods in this API to create a shipment and the associated shipping label.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Dimensions(object):
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
        'height': 'str',
        'length': 'str',
        'unit': 'str',
        'width': 'str'
    }

    attribute_map = {
        'height': 'height',
        'length': 'length',
        'unit': 'unit',
        'width': 'width'
    }

    def __init__(self, height=None, length=None, unit=None, width=None):  # noqa: E501
        """Dimensions - a model defined in Swagger"""  # noqa: E501
        self._height = None
        self._length = None
        self._unit = None
        self._width = None
        self.discriminator = None
        if height is not None:
            self.height = height
        if length is not None:
            self.length = length
        if unit is not None:
            self.unit = unit
        if width is not None:
            self.width = width

    @property
    def height(self):
        """Gets the height of this Dimensions.  # noqa: E501

        The numeric value of the height of the package.  # noqa: E501

        :return: The height of this Dimensions.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Dimensions.

        The numeric value of the height of the package.  # noqa: E501

        :param height: The height of this Dimensions.  # noqa: E501
        :type: str
        """

        self._height = height

    @property
    def length(self):
        """Gets the length of this Dimensions.  # noqa: E501

        The numeric value of the length of the package.  # noqa: E501

        :return: The length of this Dimensions.  # noqa: E501
        :rtype: str
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Dimensions.

        The numeric value of the length of the package.  # noqa: E501

        :param length: The length of this Dimensions.  # noqa: E501
        :type: str
        """

        self._length = length

    @property
    def unit(self):
        """Gets the unit of this Dimensions.  # noqa: E501

        The unit of measure used to express the height, length, and width of the package. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/logistics/types/api:LengthUnitOfMeasureEnum'>eBay API documentation</a>  # noqa: E501

        :return: The unit of this Dimensions.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Dimensions.

        The unit of measure used to express the height, length, and width of the package. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/logistics/types/api:LengthUnitOfMeasureEnum'>eBay API documentation</a>  # noqa: E501

        :param unit: The unit of this Dimensions.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def width(self):
        """Gets the width of this Dimensions.  # noqa: E501

        The numeric value of the width of the package.  # noqa: E501

        :return: The width of this Dimensions.  # noqa: E501
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Dimensions.

        The numeric value of the width of the package.  # noqa: E501

        :param width: The width of this Dimensions.  # noqa: E501
        :type: str
        """

        self._width = width

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
        if issubclass(Dimensions, dict):
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
        if not isinstance(other, Dimensions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
