# coding: utf-8

"""
    Order API

    <span class=\"tablenote\"><b>Note:</b> The Order API (v2) currently only supports the guest payment/checkout flow. If you need to support member payment/checkout flow, use the <a href=\"/api-docs/buy/order_v1/resources/methods\">v1_beta version</a> of the Order API.</span><br /><br /><span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"><img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\"  alt=\"Limited Release\" title=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The Order API provides interfaces that let shoppers pay for items. It also returns payment and shipping status of the order.  # noqa: E501

    OpenAPI spec version: v2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LineItemInput(object):
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
        'item_id': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'item_id': 'itemId',
        'quantity': 'quantity'
    }

    def __init__(self, item_id=None, quantity=None):  # noqa: E501
        """LineItemInput - a model defined in Swagger"""  # noqa: E501
        self._item_id = None
        self._quantity = None
        self.discriminator = None
        if item_id is not None:
            self.item_id = item_id
        if quantity is not None:
            self.quantity = quantity

    @property
    def item_id(self):
        """Gets the item_id of this LineItemInput.  # noqa: E501

        The unique eBay-assigned identifier of an item. This ID is returned by the <b>Browse</b> and <b>Feed</b> API methods. The ID must be in RESTful item ID format.<br /><br /><b>For example:</b> <code>v1|2**********6|5**********4</code> or <code>v1|1**********9|0</code>.<br /><br />For more information about item IDs for RESTful APIs, see <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API compatibility</a>.<br /><br />Each <b>itemId</b> will become a single line item.<br /><br /><b>Maximum:</b>10 per checkout  # noqa: E501

        :return: The item_id of this LineItemInput.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this LineItemInput.

        The unique eBay-assigned identifier of an item. This ID is returned by the <b>Browse</b> and <b>Feed</b> API methods. The ID must be in RESTful item ID format.<br /><br /><b>For example:</b> <code>v1|2**********6|5**********4</code> or <code>v1|1**********9|0</code>.<br /><br />For more information about item IDs for RESTful APIs, see <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API compatibility</a>.<br /><br />Each <b>itemId</b> will become a single line item.<br /><br /><b>Maximum:</b>10 per checkout  # noqa: E501

        :param item_id: The item_id of this LineItemInput.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def quantity(self):
        """Gets the quantity of this LineItemInput.  # noqa: E501

        The quantity ordered in this line item.  # noqa: E501

        :return: The quantity of this LineItemInput.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this LineItemInput.

        The quantity ordered in this line item.  # noqa: E501

        :param quantity: The quantity of this LineItemInput.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if issubclass(LineItemInput, dict):
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
        if not isinstance(other, LineItemInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
