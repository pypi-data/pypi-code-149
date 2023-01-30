# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EbayVaultProgram(object):
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
        'fulfillment_type': 'str'
    }

    attribute_map = {
        'fulfillment_type': 'fulfillmentType'
    }

    def __init__(self, fulfillment_type=None):  # noqa: E501
        """EbayVaultProgram - a model defined in Swagger"""  # noqa: E501
        self._fulfillment_type = None
        self.discriminator = None
        if fulfillment_type is not None:
            self.fulfillment_type = fulfillment_type

    @property
    def fulfillment_type(self):
        """Gets the fulfillment_type of this EbayVaultProgram.  # noqa: E501

        This field specifies how an eBay vault order will be fulfilled. Supported options are:<ul><li><b>Seller to Vault</b>: the order will be shipped by the seller to an authenticator.</li><li><b>Vault to Vault</b>: the order will be shipped from an eBay vault to the buyer's vault.</li><li><b>Vault to Buyer</b>: the order will be shipped from an eBay vault to the buyer's shipping address.</li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:EbayVaultFulfillmentTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The fulfillment_type of this EbayVaultProgram.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_type

    @fulfillment_type.setter
    def fulfillment_type(self, fulfillment_type):
        """Sets the fulfillment_type of this EbayVaultProgram.

        This field specifies how an eBay vault order will be fulfilled. Supported options are:<ul><li><b>Seller to Vault</b>: the order will be shipped by the seller to an authenticator.</li><li><b>Vault to Vault</b>: the order will be shipped from an eBay vault to the buyer's vault.</li><li><b>Vault to Buyer</b>: the order will be shipped from an eBay vault to the buyer's shipping address.</li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:EbayVaultFulfillmentTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param fulfillment_type: The fulfillment_type of this EbayVaultProgram.  # noqa: E501
        :type: str
        """

        self._fulfillment_type = fulfillment_type

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
        if issubclass(EbayVaultProgram, dict):
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
        if not isinstance(other, EbayVaultProgram):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
