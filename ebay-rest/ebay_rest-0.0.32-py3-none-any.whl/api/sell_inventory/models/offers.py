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

class Offers(object):
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
        'href': 'str',
        'limit': 'int',
        'next': 'str',
        'offers': 'list[EbayOfferDetailsWithAll]',
        'prev': 'str',
        'size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'href': 'href',
        'limit': 'limit',
        'next': 'next',
        'offers': 'offers',
        'prev': 'prev',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, href=None, limit=None, next=None, offers=None, prev=None, size=None, total=None):  # noqa: E501
        """Offers - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._limit = None
        self._next = None
        self._offers = None
        self._prev = None
        self._size = None
        self._total = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if offers is not None:
            self.offers = offers
        if prev is not None:
            self.prev = prev
        if size is not None:
            self.size = size
        if total is not None:
            self.total = total

    @property
    def href(self):
        """Gets the href of this Offers.  # noqa: E501

        This is the URL to the current page of offers.  # noqa: E501

        :return: The href of this Offers.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Offers.

        This is the URL to the current page of offers.  # noqa: E501

        :param href: The href of this Offers.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def limit(self):
        """Gets the limit of this Offers.  # noqa: E501

        This integer value is the number of offers that will be displayed on each results page.  # noqa: E501

        :return: The limit of this Offers.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this Offers.

        This integer value is the number of offers that will be displayed on each results page.  # noqa: E501

        :param limit: The limit of this Offers.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this Offers.  # noqa: E501

        This is the URL to the next page of offers. This field will only be returned if there are additional offers to view.  # noqa: E501

        :return: The next of this Offers.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Offers.

        This is the URL to the next page of offers. This field will only be returned if there are additional offers to view.  # noqa: E501

        :param next: The next of this Offers.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def offers(self):
        """Gets the offers of this Offers.  # noqa: E501

        This container is an array of one or more of the seller's offers for the SKU value that is passed in through the required <strong>sku</strong> query parameter.<br><br> <span class=\"tablenote\"> <strong>Note:</strong> Currently, the Inventory API does not support the same SKU across multiple eBay marketplaces, so the <strong>getOffers</strong> call will only return one offer.</span><br><br><strong>Max Occurs:</strong> 25  # noqa: E501

        :return: The offers of this Offers.  # noqa: E501
        :rtype: list[EbayOfferDetailsWithAll]
        """
        return self._offers

    @offers.setter
    def offers(self, offers):
        """Sets the offers of this Offers.

        This container is an array of one or more of the seller's offers for the SKU value that is passed in through the required <strong>sku</strong> query parameter.<br><br> <span class=\"tablenote\"> <strong>Note:</strong> Currently, the Inventory API does not support the same SKU across multiple eBay marketplaces, so the <strong>getOffers</strong> call will only return one offer.</span><br><br><strong>Max Occurs:</strong> 25  # noqa: E501

        :param offers: The offers of this Offers.  # noqa: E501
        :type: list[EbayOfferDetailsWithAll]
        """

        self._offers = offers

    @property
    def prev(self):
        """Gets the prev of this Offers.  # noqa: E501

        This is the URL to the previous page of offers. This field will only be returned if there are previous offers to view.  # noqa: E501

        :return: The prev of this Offers.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this Offers.

        This is the URL to the previous page of offers. This field will only be returned if there are previous offers to view.  # noqa: E501

        :param prev: The prev of this Offers.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def size(self):
        """Gets the size of this Offers.  # noqa: E501

        This integer value indicates the number of offers being displayed on the current page of results. This number will generally be the same as the <strong>limit</strong> value if there are additional pages of results to view.<br><br> <span class=\"tablenote\"> <strong>Note:</strong> Currently, the Inventory API does not support the same SKU across multiple eBay marketplaces, so the <strong>Get Offers</strong> call will only return one offer, so this value should always be <code>1</code>.</span>  # noqa: E501

        :return: The size of this Offers.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Offers.

        This integer value indicates the number of offers being displayed on the current page of results. This number will generally be the same as the <strong>limit</strong> value if there are additional pages of results to view.<br><br> <span class=\"tablenote\"> <strong>Note:</strong> Currently, the Inventory API does not support the same SKU across multiple eBay marketplaces, so the <strong>Get Offers</strong> call will only return one offer, so this value should always be <code>1</code>.</span>  # noqa: E501

        :param size: The size of this Offers.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def total(self):
        """Gets the total of this Offers.  # noqa: E501

        This integer value is the total number of offers that exist for the specified SKU value. Based on this number and on the <strong>limit</strong> value, the seller may have to toggle through multiple pages to view all offers.<br><br> <span class=\"tablenote\"> <strong>Note:</strong> Currently, the Inventory API does not support the same SKU across multiple eBay marketplaces, so the <strong>Get Offers</strong> call will only return one offer, so this value should always be <code>1</code>.</span>  # noqa: E501

        :return: The total of this Offers.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Offers.

        This integer value is the total number of offers that exist for the specified SKU value. Based on this number and on the <strong>limit</strong> value, the seller may have to toggle through multiple pages to view all offers.<br><br> <span class=\"tablenote\"> <strong>Note:</strong> Currently, the Inventory API does not support the same SKU across multiple eBay marketplaces, so the <strong>Get Offers</strong> call will only return one offer, so this value should always be <code>1</code>.</span>  # noqa: E501

        :param total: The total of this Offers.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(Offers, dict):
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
        if not isinstance(other, Offers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
