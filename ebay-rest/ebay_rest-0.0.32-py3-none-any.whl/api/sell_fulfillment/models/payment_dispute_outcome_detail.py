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

class PaymentDisputeOutcomeDetail(object):
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
        'fees': 'SimpleAmount',
        'protected_amount': 'SimpleAmount',
        'protection_status': 'str',
        'reason_for_closure': 'str',
        'recoup_amount': 'SimpleAmount',
        'total_fee_credit': 'SimpleAmount'
    }

    attribute_map = {
        'fees': 'fees',
        'protected_amount': 'protectedAmount',
        'protection_status': 'protectionStatus',
        'reason_for_closure': 'reasonForClosure',
        'recoup_amount': 'recoupAmount',
        'total_fee_credit': 'totalFeeCredit'
    }

    def __init__(self, fees=None, protected_amount=None, protection_status=None, reason_for_closure=None, recoup_amount=None, total_fee_credit=None):  # noqa: E501
        """PaymentDisputeOutcomeDetail - a model defined in Swagger"""  # noqa: E501
        self._fees = None
        self._protected_amount = None
        self._protection_status = None
        self._reason_for_closure = None
        self._recoup_amount = None
        self._total_fee_credit = None
        self.discriminator = None
        if fees is not None:
            self.fees = fees
        if protected_amount is not None:
            self.protected_amount = protected_amount
        if protection_status is not None:
            self.protection_status = protection_status
        if reason_for_closure is not None:
            self.reason_for_closure = reason_for_closure
        if recoup_amount is not None:
            self.recoup_amount = recoup_amount
        if total_fee_credit is not None:
            self.total_fee_credit = total_fee_credit

    @property
    def fees(self):
        """Gets the fees of this PaymentDisputeOutcomeDetail.  # noqa: E501


        :return: The fees of this PaymentDisputeOutcomeDetail.  # noqa: E501
        :rtype: SimpleAmount
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this PaymentDisputeOutcomeDetail.


        :param fees: The fees of this PaymentDisputeOutcomeDetail.  # noqa: E501
        :type: SimpleAmount
        """

        self._fees = fees

    @property
    def protected_amount(self):
        """Gets the protected_amount of this PaymentDisputeOutcomeDetail.  # noqa: E501


        :return: The protected_amount of this PaymentDisputeOutcomeDetail.  # noqa: E501
        :rtype: SimpleAmount
        """
        return self._protected_amount

    @protected_amount.setter
    def protected_amount(self, protected_amount):
        """Sets the protected_amount of this PaymentDisputeOutcomeDetail.


        :param protected_amount: The protected_amount of this PaymentDisputeOutcomeDetail.  # noqa: E501
        :type: SimpleAmount
        """

        self._protected_amount = protected_amount

    @property
    def protection_status(self):
        """Gets the protection_status of this PaymentDisputeOutcomeDetail.  # noqa: E501

        This enumeration value indicates if the seller is fully protected, partially protected, or not protected by eBay for the payment dispute. This field is always returned once the payment dispute is resolved. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:ProtectionStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The protection_status of this PaymentDisputeOutcomeDetail.  # noqa: E501
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        """Sets the protection_status of this PaymentDisputeOutcomeDetail.

        This enumeration value indicates if the seller is fully protected, partially protected, or not protected by eBay for the payment dispute. This field is always returned once the payment dispute is resolved. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:ProtectionStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param protection_status: The protection_status of this PaymentDisputeOutcomeDetail.  # noqa: E501
        :type: str
        """

        self._protection_status = protection_status

    @property
    def reason_for_closure(self):
        """Gets the reason_for_closure of this PaymentDisputeOutcomeDetail.  # noqa: E501

        The enumeration value returned in this field indicates the outcome of the payment dispute for the seller. This field is always returned once the payment dispute is resolved. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:OutcomeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The reason_for_closure of this PaymentDisputeOutcomeDetail.  # noqa: E501
        :rtype: str
        """
        return self._reason_for_closure

    @reason_for_closure.setter
    def reason_for_closure(self, reason_for_closure):
        """Sets the reason_for_closure of this PaymentDisputeOutcomeDetail.

        The enumeration value returned in this field indicates the outcome of the payment dispute for the seller. This field is always returned once the payment dispute is resolved. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:OutcomeEnum'>eBay API documentation</a>  # noqa: E501

        :param reason_for_closure: The reason_for_closure of this PaymentDisputeOutcomeDetail.  # noqa: E501
        :type: str
        """

        self._reason_for_closure = reason_for_closure

    @property
    def recoup_amount(self):
        """Gets the recoup_amount of this PaymentDisputeOutcomeDetail.  # noqa: E501


        :return: The recoup_amount of this PaymentDisputeOutcomeDetail.  # noqa: E501
        :rtype: SimpleAmount
        """
        return self._recoup_amount

    @recoup_amount.setter
    def recoup_amount(self, recoup_amount):
        """Sets the recoup_amount of this PaymentDisputeOutcomeDetail.


        :param recoup_amount: The recoup_amount of this PaymentDisputeOutcomeDetail.  # noqa: E501
        :type: SimpleAmount
        """

        self._recoup_amount = recoup_amount

    @property
    def total_fee_credit(self):
        """Gets the total_fee_credit of this PaymentDisputeOutcomeDetail.  # noqa: E501


        :return: The total_fee_credit of this PaymentDisputeOutcomeDetail.  # noqa: E501
        :rtype: SimpleAmount
        """
        return self._total_fee_credit

    @total_fee_credit.setter
    def total_fee_credit(self, total_fee_credit):
        """Sets the total_fee_credit of this PaymentDisputeOutcomeDetail.


        :param total_fee_credit: The total_fee_credit of this PaymentDisputeOutcomeDetail.  # noqa: E501
        :type: SimpleAmount
        """

        self._total_fee_credit = total_fee_credit

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
        if issubclass(PaymentDisputeOutcomeDetail, dict):
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
        if not isinstance(other, PaymentDisputeOutcomeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
