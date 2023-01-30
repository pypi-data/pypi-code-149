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

class UpdateKeywordRequest(object):
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
        'bid': 'Amount',
        'keyword_status': 'str'
    }

    attribute_map = {
        'bid': 'bid',
        'keyword_status': 'keywordStatus'
    }

    def __init__(self, bid=None, keyword_status=None):  # noqa: E501
        """UpdateKeywordRequest - a model defined in Swagger"""  # noqa: E501
        self._bid = None
        self._keyword_status = None
        self.discriminator = None
        if bid is not None:
            self.bid = bid
        if keyword_status is not None:
            self.keyword_status = keyword_status

    @property
    def bid(self):
        """Gets the bid of this UpdateKeywordRequest.  # noqa: E501


        :return: The bid of this UpdateKeywordRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this UpdateKeywordRequest.


        :param bid: The bid of this UpdateKeywordRequest.  # noqa: E501
        :type: Amount
        """

        self._bid = bid

    @property
    def keyword_status(self):
        """Gets the keyword_status of this UpdateKeywordRequest.  # noqa: E501

        Include this field if you wish to change the status of the keyword. The status value specified here must be different than the keyword's current status. To confirm the current status of a keyword, you can use the <a href=\"/api-docs/sell/marketing/resources/keyword/methods/getKeyword\">getKeyword</a> method.</p><p>If the status of the ad is currently <code>ACTIVE</code>, you can change status to <code>PAUSED</code> or <code>ARCHIVED</code>. If ad group is currently in <code>PAUSED</code> status, you can change the status back to <code>ACTIVE</code>. Ads that are currently in <code>ARCHIVED</code> status cannot be made <code>ACTIVE</code> again. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:KeywordStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The keyword_status of this UpdateKeywordRequest.  # noqa: E501
        :rtype: str
        """
        return self._keyword_status

    @keyword_status.setter
    def keyword_status(self, keyword_status):
        """Sets the keyword_status of this UpdateKeywordRequest.

        Include this field if you wish to change the status of the keyword. The status value specified here must be different than the keyword's current status. To confirm the current status of a keyword, you can use the <a href=\"/api-docs/sell/marketing/resources/keyword/methods/getKeyword\">getKeyword</a> method.</p><p>If the status of the ad is currently <code>ACTIVE</code>, you can change status to <code>PAUSED</code> or <code>ARCHIVED</code>. If ad group is currently in <code>PAUSED</code> status, you can change the status back to <code>ACTIVE</code>. Ads that are currently in <code>ARCHIVED</code> status cannot be made <code>ACTIVE</code> again. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:KeywordStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param keyword_status: The keyword_status of this UpdateKeywordRequest.  # noqa: E501
        :type: str
        """

        self._keyword_status = keyword_status

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
        if issubclass(UpdateKeywordRequest, dict):
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
        if not isinstance(other, UpdateKeywordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
