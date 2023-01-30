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

class CreateAdRequest(object):
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
        'ad_group_id': 'str',
        'bid_percentage': 'str',
        'listing_id': 'str'
    }

    attribute_map = {
        'ad_group_id': 'adGroupId',
        'bid_percentage': 'bidPercentage',
        'listing_id': 'listingId'
    }

    def __init__(self, ad_group_id=None, bid_percentage=None, listing_id=None):  # noqa: E501
        """CreateAdRequest - a model defined in Swagger"""  # noqa: E501
        self._ad_group_id = None
        self._bid_percentage = None
        self._listing_id = None
        self.discriminator = None
        if ad_group_id is not None:
            self.ad_group_id = ad_group_id
        if bid_percentage is not None:
            self.bid_percentage = bid_percentage
        if listing_id is not None:
            self.listing_id = listing_id

    @property
    def ad_group_id(self):
        """Gets the ad_group_id of this CreateAdRequest.  # noqa: E501

        A unique eBay-assigned ID for an ad group in a campaign that uses the Cost Per Click (CPC) funding model. <p><i>Required if</i> the campaign's funding model is Cost Per Click (CPC).</p><p>Create an ad group using the <a href=\"/api-docs/sell/marketing/resources/adgroup/methods/createAdGroup\">createAdGroup</a> method.</p><p>Specify the campaign to associate the ad group with using the <b>campaign_id</b> path parameter. </p><span class=\"tablenote\"><b>Note:</b> You can call the  <a href=\"/api-docs/sell/marketing/resources/adgroup/methods/getAdGroups\">getAdGroups</a> method to retrieve the ad group IDs for a seller.</span>  # noqa: E501

        :return: The ad_group_id of this CreateAdRequest.  # noqa: E501
        :rtype: str
        """
        return self._ad_group_id

    @ad_group_id.setter
    def ad_group_id(self, ad_group_id):
        """Sets the ad_group_id of this CreateAdRequest.

        A unique eBay-assigned ID for an ad group in a campaign that uses the Cost Per Click (CPC) funding model. <p><i>Required if</i> the campaign's funding model is Cost Per Click (CPC).</p><p>Create an ad group using the <a href=\"/api-docs/sell/marketing/resources/adgroup/methods/createAdGroup\">createAdGroup</a> method.</p><p>Specify the campaign to associate the ad group with using the <b>campaign_id</b> path parameter. </p><span class=\"tablenote\"><b>Note:</b> You can call the  <a href=\"/api-docs/sell/marketing/resources/adgroup/methods/getAdGroups\">getAdGroups</a> method to retrieve the ad group IDs for a seller.</span>  # noqa: E501

        :param ad_group_id: The ad_group_id of this CreateAdRequest.  # noqa: E501
        :type: str
        """

        self._ad_group_id = ad_group_id

    @property
    def bid_percentage(self):
        """Gets the bid_percentage of this CreateAdRequest.  # noqa: E501

        The user-defined <b>bid percentage</b> (also known as the <i>ad rate</i>) sets the level that eBay increases the visibility in search results for the associated listing. The higher the <b>bidPercentage</b> value, the more eBay promotes the listing.<br><br><i>Required if</i> the campaign's funding model is Cost Per Sale (CPS).  <br><br>The value specified here is also used to calculate the Promoted Listings fee. This percentage value is multiplied by the final sales price to determine the fee. <br><br>The Promoted Listings fee is determined at the time the transaction completes and the seller is assessed the fee only when an item sells through a Promoted Listings ad campaign. <br><br>The <b>bidPercentage</b> is a single precision value that is guided by the following rules: <ul><li>These values are <b>valid</b>:<br>&nbsp;&nbsp;&nbsp;<code>4.1</code>,&nbsp;&nbsp;&nbsp;<code>5.0</code>, &nbsp;&nbsp;&nbsp;<code>5.5</code>, ...</li>  <li>These values are <b>not valid</b>:<br /> &nbsp;&nbsp;&nbsp;<code>0.01</code>, &nbsp;&nbsp;&nbsp;<code>10.75</code>, &nbsp;&nbsp;&nbsp;<code>99.99</code>,<br /> &nbsp;&nbsp;&nbsp;and so on.</li></ul>This is default bid percentage for the campaigns using the Cost Per Sale (CPS) funding model, and this value will be overridden by any ads in the campaign that have their own set bid percentages.<br /><br />If a bid percentage is not provided for an ad, eBay uses the default bid percentage of the associated campaign.<br /><br /><b>Minimum value:</b> 2.0 <br><b>Maximum value:</b> 100.0  # noqa: E501

        :return: The bid_percentage of this CreateAdRequest.  # noqa: E501
        :rtype: str
        """
        return self._bid_percentage

    @bid_percentage.setter
    def bid_percentage(self, bid_percentage):
        """Sets the bid_percentage of this CreateAdRequest.

        The user-defined <b>bid percentage</b> (also known as the <i>ad rate</i>) sets the level that eBay increases the visibility in search results for the associated listing. The higher the <b>bidPercentage</b> value, the more eBay promotes the listing.<br><br><i>Required if</i> the campaign's funding model is Cost Per Sale (CPS).  <br><br>The value specified here is also used to calculate the Promoted Listings fee. This percentage value is multiplied by the final sales price to determine the fee. <br><br>The Promoted Listings fee is determined at the time the transaction completes and the seller is assessed the fee only when an item sells through a Promoted Listings ad campaign. <br><br>The <b>bidPercentage</b> is a single precision value that is guided by the following rules: <ul><li>These values are <b>valid</b>:<br>&nbsp;&nbsp;&nbsp;<code>4.1</code>,&nbsp;&nbsp;&nbsp;<code>5.0</code>, &nbsp;&nbsp;&nbsp;<code>5.5</code>, ...</li>  <li>These values are <b>not valid</b>:<br /> &nbsp;&nbsp;&nbsp;<code>0.01</code>, &nbsp;&nbsp;&nbsp;<code>10.75</code>, &nbsp;&nbsp;&nbsp;<code>99.99</code>,<br /> &nbsp;&nbsp;&nbsp;and so on.</li></ul>This is default bid percentage for the campaigns using the Cost Per Sale (CPS) funding model, and this value will be overridden by any ads in the campaign that have their own set bid percentages.<br /><br />If a bid percentage is not provided for an ad, eBay uses the default bid percentage of the associated campaign.<br /><br /><b>Minimum value:</b> 2.0 <br><b>Maximum value:</b> 100.0  # noqa: E501

        :param bid_percentage: The bid_percentage of this CreateAdRequest.  # noqa: E501
        :type: str
        """

        self._bid_percentage = bid_percentage

    @property
    def listing_id(self):
        """Gets the listing_id of this CreateAdRequest.  # noqa: E501

        A unique eBay-assigned ID for a listing that is generated when the listing is created.  <p class=\"tablenote\"><b>Note:</b> This field accepts listing IDs, as generated by the Inventory API, and item IDs, as used in the eBay Traditional API set (e.g., the Trading and Finding APIs).</p>  # noqa: E501

        :return: The listing_id of this CreateAdRequest.  # noqa: E501
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """Sets the listing_id of this CreateAdRequest.

        A unique eBay-assigned ID for a listing that is generated when the listing is created.  <p class=\"tablenote\"><b>Note:</b> This field accepts listing IDs, as generated by the Inventory API, and item IDs, as used in the eBay Traditional API set (e.g., the Trading and Finding APIs).</p>  # noqa: E501

        :param listing_id: The listing_id of this CreateAdRequest.  # noqa: E501
        :type: str
        """

        self._listing_id = listing_id

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
        if issubclass(CreateAdRequest, dict):
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
        if not isinstance(other, CreateAdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
