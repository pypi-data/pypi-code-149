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

class DeleteAdsByInventoryReferenceResponse(object):
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
        'ad_ids': 'list[str]',
        'errors': 'list[Error]',
        'inventory_reference_id': 'str',
        'inventory_reference_type': 'str',
        'status_code': 'int'
    }

    attribute_map = {
        'ad_ids': 'adIds',
        'errors': 'errors',
        'inventory_reference_id': 'inventoryReferenceId',
        'inventory_reference_type': 'inventoryReferenceType',
        'status_code': 'statusCode'
    }

    def __init__(self, ad_ids=None, errors=None, inventory_reference_id=None, inventory_reference_type=None, status_code=None):  # noqa: E501
        """DeleteAdsByInventoryReferenceResponse - a model defined in Swagger"""  # noqa: E501
        self._ad_ids = None
        self._errors = None
        self._inventory_reference_id = None
        self._inventory_reference_type = None
        self._status_code = None
        self.discriminator = None
        if ad_ids is not None:
            self.ad_ids = ad_ids
        if errors is not None:
            self.errors = errors
        if inventory_reference_id is not None:
            self.inventory_reference_id = inventory_reference_id
        if inventory_reference_type is not None:
            self.inventory_reference_type = inventory_reference_type
        if status_code is not None:
            self.status_code = status_code

    @property
    def ad_ids(self):
        """Gets the ad_ids of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501

        The unique identifier of the ad that was deleted, or the ad that the seller attempted to delete.<span class=\"tablenote\"><b>Note:</b>Although the field name is plural and it is an array, only one ad ID will be returned here since there can be only one ad per listing.</span>  # noqa: E501

        :return: The ad_ids of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._ad_ids

    @ad_ids.setter
    def ad_ids(self, ad_ids):
        """Sets the ad_ids of this DeleteAdsByInventoryReferenceResponse.

        The unique identifier of the ad that was deleted, or the ad that the seller attempted to delete.<span class=\"tablenote\"><b>Note:</b>Although the field name is plural and it is an array, only one ad ID will be returned here since there can be only one ad per listing.</span>  # noqa: E501

        :param ad_ids: The ad_ids of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501
        :type: list[str]
        """

        self._ad_ids = ad_ids

    @property
    def errors(self):
        """Gets the errors of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501

        The container for the errors associated with the request.  # noqa: E501

        :return: The errors of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this DeleteAdsByInventoryReferenceResponse.

        The container for the errors associated with the request.  # noqa: E501

        :param errors: The errors of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    @property
    def inventory_reference_id(self):
        """Gets the inventory_reference_id of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501

        The inventory reference ID is a seller-defined SKU value for a single-item listing, or a seller-defined identifier for an inventory item group. Both of these values are defined when using the Inventory API, and an inventory item group is used to create a multiple-variation listing.  # noqa: E501

        :return: The inventory_reference_id of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501
        :rtype: str
        """
        return self._inventory_reference_id

    @inventory_reference_id.setter
    def inventory_reference_id(self, inventory_reference_id):
        """Sets the inventory_reference_id of this DeleteAdsByInventoryReferenceResponse.

        The inventory reference ID is a seller-defined SKU value for a single-item listing, or a seller-defined identifier for an inventory item group. Both of these values are defined when using the Inventory API, and an inventory item group is used to create a multiple-variation listing.  # noqa: E501

        :param inventory_reference_id: The inventory_reference_id of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501
        :type: str
        """

        self._inventory_reference_id = inventory_reference_id

    @property
    def inventory_reference_type(self):
        """Gets the inventory_reference_type of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501

        The enumeration value returned here indicates if the ad was for a single-variation listing or a multiple-variation listing. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:InventoryReferenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The inventory_reference_type of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501
        :rtype: str
        """
        return self._inventory_reference_type

    @inventory_reference_type.setter
    def inventory_reference_type(self, inventory_reference_type):
        """Sets the inventory_reference_type of this DeleteAdsByInventoryReferenceResponse.

        The enumeration value returned here indicates if the ad was for a single-variation listing or a multiple-variation listing. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:InventoryReferenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param inventory_reference_type: The inventory_reference_type of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501
        :type: str
        """

        self._inventory_reference_type = inventory_reference_type

    @property
    def status_code(self):
        """Gets the status_code of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501

        An HTTP status code indicating if the corresponding ad was successfully deleted or not. <code>200 Successful</code> should be returned for successfully deleted ads. <span class=\"tablenote\"><b>Note:</b>A status code is returned for each ad that the seller deletes, or attempts to delete.</span>  # noqa: E501

        :return: The status_code of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this DeleteAdsByInventoryReferenceResponse.

        An HTTP status code indicating if the corresponding ad was successfully deleted or not. <code>200 Successful</code> should be returned for successfully deleted ads. <span class=\"tablenote\"><b>Note:</b>A status code is returned for each ad that the seller deletes, or attempts to delete.</span>  # noqa: E501

        :param status_code: The status_code of this DeleteAdsByInventoryReferenceResponse.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

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
        if issubclass(DeleteAdsByInventoryReferenceResponse, dict):
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
        if not isinstance(other, DeleteAdsByInventoryReferenceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
