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

class PostSaleAuthenticationProgram(object):
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
        'outcome_reason': 'str',
        'status': 'str'
    }

    attribute_map = {
        'outcome_reason': 'outcomeReason',
        'status': 'status'
    }

    def __init__(self, outcome_reason=None, status=None):  # noqa: E501
        """PostSaleAuthenticationProgram - a model defined in Swagger"""  # noqa: E501
        self._outcome_reason = None
        self._status = None
        self.discriminator = None
        if outcome_reason is not None:
            self.outcome_reason = outcome_reason
        if status is not None:
            self.status = status

    @property
    def outcome_reason(self):
        """Gets the outcome_reason of this PostSaleAuthenticationProgram.  # noqa: E501

        This field indicates the result of the authenticity verification inspection on an order line item. This field is not returned when the status value of the order line item is <code>PENDING</code> or <code>PASSED</code>. The possible values returned here are <code>NOT_AUTHENTIC</code>, <code>NOT_AS_DESCRIBED</code>, <code>CUSTOMIZED</code>, <code>MISCATEGORIZED</code>, or <code>NOT_AUTHENTIC_NO_RETURN</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AuthenticityVerificationReasonEnum'>eBay API documentation</a>  # noqa: E501

        :return: The outcome_reason of this PostSaleAuthenticationProgram.  # noqa: E501
        :rtype: str
        """
        return self._outcome_reason

    @outcome_reason.setter
    def outcome_reason(self, outcome_reason):
        """Sets the outcome_reason of this PostSaleAuthenticationProgram.

        This field indicates the result of the authenticity verification inspection on an order line item. This field is not returned when the status value of the order line item is <code>PENDING</code> or <code>PASSED</code>. The possible values returned here are <code>NOT_AUTHENTIC</code>, <code>NOT_AS_DESCRIBED</code>, <code>CUSTOMIZED</code>, <code>MISCATEGORIZED</code>, or <code>NOT_AUTHENTIC_NO_RETURN</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AuthenticityVerificationReasonEnum'>eBay API documentation</a>  # noqa: E501

        :param outcome_reason: The outcome_reason of this PostSaleAuthenticationProgram.  # noqa: E501
        :type: str
        """

        self._outcome_reason = outcome_reason

    @property
    def status(self):
        """Gets the status of this PostSaleAuthenticationProgram.  # noqa: E501

        The value in this field indicates whether the order line item has passed or failed the authenticity verification inspection, or if the inspection and/or results are still pending. The possible values returned here are <code>PENDING</code>, <code>PASSED</code>, <code>FAILED</code>, or <code>PASSED_WITH_EXCEPTION</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AuthenticityVerificationStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The status of this PostSaleAuthenticationProgram.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PostSaleAuthenticationProgram.

        The value in this field indicates whether the order line item has passed or failed the authenticity verification inspection, or if the inspection and/or results are still pending. The possible values returned here are <code>PENDING</code>, <code>PASSED</code>, <code>FAILED</code>, or <code>PASSED_WITH_EXCEPTION</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AuthenticityVerificationStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param status: The status of this PostSaleAuthenticationProgram.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(PostSaleAuthenticationProgram, dict):
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
        if not isinstance(other, PostSaleAuthenticationProgram):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
