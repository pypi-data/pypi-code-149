# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br/><br/>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class KycResponse(object):
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
        'kyc_checks': 'list[KycCheck]'
    }

    attribute_map = {
        'kyc_checks': 'kycChecks'
    }

    def __init__(self, kyc_checks=None):  # noqa: E501
        """KycResponse - a model defined in Swagger"""  # noqa: E501
        self._kyc_checks = None
        self.discriminator = None
        if kyc_checks is not None:
            self.kyc_checks = kyc_checks

    @property
    def kyc_checks(self):
        """Gets the kyc_checks of this KycResponse.  # noqa: E501

        This array contains one or more KYC checks required from a managed payments seller. The seller may need to provide more documentation and/or information about themselves, their company, or the bank account they are using for seller payouts.<br/><br/>If no KYC checks are currently required from the seller, this array is not returned, and the seller only receives a <code>204 No Content</code> HTTP status code.  # noqa: E501

        :return: The kyc_checks of this KycResponse.  # noqa: E501
        :rtype: list[KycCheck]
        """
        return self._kyc_checks

    @kyc_checks.setter
    def kyc_checks(self, kyc_checks):
        """Sets the kyc_checks of this KycResponse.

        This array contains one or more KYC checks required from a managed payments seller. The seller may need to provide more documentation and/or information about themselves, their company, or the bank account they are using for seller payouts.<br/><br/>If no KYC checks are currently required from the seller, this array is not returned, and the seller only receives a <code>204 No Content</code> HTTP status code.  # noqa: E501

        :param kyc_checks: The kyc_checks of this KycResponse.  # noqa: E501
        :type: list[KycCheck]
        """

        self._kyc_checks = kyc_checks

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
        if issubclass(KycResponse, dict):
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
        if not isinstance(other, KycResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
