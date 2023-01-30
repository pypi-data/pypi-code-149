# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, refer to the <a href=\"/api-docs/sell/static/marketing/pl-landing.html\">Promoted Listings playbook</a>.</li><li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProposedBid(object):
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
        'currency': 'str',
        'range_end': 'str',
        'range_start': 'str',
        'value': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        'range_end': 'rangeEnd',
        'range_start': 'rangeStart',
        'value': 'value'
    }

    def __init__(self, currency=None, range_end=None, range_start=None, value=None):  # noqa: E501
        """ProposedBid - a model defined in Swagger"""  # noqa: E501
        self._currency = None
        self._range_end = None
        self._range_start = None
        self._value = None
        self.discriminator = None
        if currency is not None:
            self.currency = currency
        if range_end is not None:
            self.range_end = range_end
        if range_start is not None:
            self.range_start = range_start
        if value is not None:
            self.value = value

    @property
    def currency(self):
        """Gets the currency of this ProposedBid.  # noqa: E501

        The base currency applied to the <b>value</b> field to establish a monetary amount.  <br><br>The currency is represented as a 3-letter <a href=\"https://www.iso.org/iso-4217-currency-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 4217</a> currency code. For example, the code for the Canadian Dollar is <code>CAD</code>.  <br><br><b>Default:</b> The default currency of the eBay marketplace that hosts the listing. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/ba:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The currency of this ProposedBid.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ProposedBid.

        The base currency applied to the <b>value</b> field to establish a monetary amount.  <br><br>The currency is represented as a 3-letter <a href=\"https://www.iso.org/iso-4217-currency-codes.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 4217</a> currency code. For example, the code for the Canadian Dollar is <code>CAD</code>.  <br><br><b>Default:</b> The default currency of the eBay marketplace that hosts the listing. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/ba:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param currency: The currency of this ProposedBid.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def range_end(self):
        """Gets the range_end of this ProposedBid.  # noqa: E501

        The end of the range specified for the bid.  # noqa: E501

        :return: The range_end of this ProposedBid.  # noqa: E501
        :rtype: str
        """
        return self._range_end

    @range_end.setter
    def range_end(self, range_end):
        """Sets the range_end of this ProposedBid.

        The end of the range specified for the bid.  # noqa: E501

        :param range_end: The range_end of this ProposedBid.  # noqa: E501
        :type: str
        """

        self._range_end = range_end

    @property
    def range_start(self):
        """Gets the range_start of this ProposedBid.  # noqa: E501

        The start of the range specified for the bid.  # noqa: E501

        :return: The range_start of this ProposedBid.  # noqa: E501
        :rtype: str
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """Sets the range_start of this ProposedBid.

        The start of the range specified for the bid.  # noqa: E501

        :param range_start: The range_start of this ProposedBid.  # noqa: E501
        :type: str
        """

        self._range_start = range_start

    @property
    def value(self):
        """Gets the value of this ProposedBid.  # noqa: E501

        The value of the proposed bid.  # noqa: E501

        :return: The value of this ProposedBid.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ProposedBid.

        The value of the proposed bid.  # noqa: E501

        :param value: The value of this ProposedBid.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(ProposedBid, dict):
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
        if not isinstance(other, ProposedBid):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
