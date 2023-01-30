# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.16.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BestOffer(object):
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
        'auto_accept_price': 'Amount',
        'auto_decline_price': 'Amount',
        'best_offer_enabled': 'bool'
    }

    attribute_map = {
        'auto_accept_price': 'autoAcceptPrice',
        'auto_decline_price': 'autoDeclinePrice',
        'best_offer_enabled': 'bestOfferEnabled'
    }

    def __init__(self, auto_accept_price=None, auto_decline_price=None, best_offer_enabled=None):  # noqa: E501
        """BestOffer - a model defined in Swagger"""  # noqa: E501
        self._auto_accept_price = None
        self._auto_decline_price = None
        self._best_offer_enabled = None
        self.discriminator = None
        if auto_accept_price is not None:
            self.auto_accept_price = auto_accept_price
        if auto_decline_price is not None:
            self.auto_decline_price = auto_decline_price
        if best_offer_enabled is not None:
            self.best_offer_enabled = best_offer_enabled

    @property
    def auto_accept_price(self):
        """Gets the auto_accept_price of this BestOffer.  # noqa: E501


        :return: The auto_accept_price of this BestOffer.  # noqa: E501
        :rtype: Amount
        """
        return self._auto_accept_price

    @auto_accept_price.setter
    def auto_accept_price(self, auto_accept_price):
        """Sets the auto_accept_price of this BestOffer.


        :param auto_accept_price: The auto_accept_price of this BestOffer.  # noqa: E501
        :type: Amount
        """

        self._auto_accept_price = auto_accept_price

    @property
    def auto_decline_price(self):
        """Gets the auto_decline_price of this BestOffer.  # noqa: E501


        :return: The auto_decline_price of this BestOffer.  # noqa: E501
        :rtype: Amount
        """
        return self._auto_decline_price

    @auto_decline_price.setter
    def auto_decline_price(self, auto_decline_price):
        """Sets the auto_decline_price of this BestOffer.


        :param auto_decline_price: The auto_decline_price of this BestOffer.  # noqa: E501
        :type: Amount
        """

        self._auto_decline_price = auto_decline_price

    @property
    def best_offer_enabled(self):
        """Gets the best_offer_enabled of this BestOffer.  # noqa: E501

        This field indicates whether or not the Best Offer feature is enabled for the listing. A seller can enable the Best Offer feature for a listing as long as the category supports the Best Offer feature.<br><br>The seller includes this field and sets its value to <code>true</code> to enable Best Offer feature.  # noqa: E501

        :return: The best_offer_enabled of this BestOffer.  # noqa: E501
        :rtype: bool
        """
        return self._best_offer_enabled

    @best_offer_enabled.setter
    def best_offer_enabled(self, best_offer_enabled):
        """Sets the best_offer_enabled of this BestOffer.

        This field indicates whether or not the Best Offer feature is enabled for the listing. A seller can enable the Best Offer feature for a listing as long as the category supports the Best Offer feature.<br><br>The seller includes this field and sets its value to <code>true</code> to enable Best Offer feature.  # noqa: E501

        :param best_offer_enabled: The best_offer_enabled of this BestOffer.  # noqa: E501
        :type: bool
        """

        self._best_offer_enabled = best_offer_enabled

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
        if issubclass(BestOffer, dict):
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
        if not isinstance(other, BestOffer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
