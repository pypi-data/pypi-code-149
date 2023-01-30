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

class ReturnPolicyRequest(object):
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
        'category_types': 'list[CategoryType]',
        'description': 'str',
        'extended_holiday_returns_offered': 'bool',
        'international_override': 'InternationalReturnOverrideType',
        'marketplace_id': 'str',
        'name': 'str',
        'refund_method': 'str',
        'restocking_fee_percentage': 'str',
        'return_instructions': 'str',
        'return_method': 'str',
        'return_period': 'TimeDuration',
        'returns_accepted': 'bool',
        'return_shipping_cost_payer': 'str'
    }

    attribute_map = {
        'category_types': 'categoryTypes',
        'description': 'description',
        'extended_holiday_returns_offered': 'extendedHolidayReturnsOffered',
        'international_override': 'internationalOverride',
        'marketplace_id': 'marketplaceId',
        'name': 'name',
        'refund_method': 'refundMethod',
        'restocking_fee_percentage': 'restockingFeePercentage',
        'return_instructions': 'returnInstructions',
        'return_method': 'returnMethod',
        'return_period': 'returnPeriod',
        'returns_accepted': 'returnsAccepted',
        'return_shipping_cost_payer': 'returnShippingCostPayer'
    }

    def __init__(self, category_types=None, description=None, extended_holiday_returns_offered=None, international_override=None, marketplace_id=None, name=None, refund_method=None, restocking_fee_percentage=None, return_instructions=None, return_method=None, return_period=None, returns_accepted=None, return_shipping_cost_payer=None):  # noqa: E501
        """ReturnPolicyRequest - a model defined in Swagger"""  # noqa: E501
        self._category_types = None
        self._description = None
        self._extended_holiday_returns_offered = None
        self._international_override = None
        self._marketplace_id = None
        self._name = None
        self._refund_method = None
        self._restocking_fee_percentage = None
        self._return_instructions = None
        self._return_method = None
        self._return_period = None
        self._returns_accepted = None
        self._return_shipping_cost_payer = None
        self.discriminator = None
        if category_types is not None:
            self.category_types = category_types
        if description is not None:
            self.description = description
        if extended_holiday_returns_offered is not None:
            self.extended_holiday_returns_offered = extended_holiday_returns_offered
        if international_override is not None:
            self.international_override = international_override
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if name is not None:
            self.name = name
        if refund_method is not None:
            self.refund_method = refund_method
        if restocking_fee_percentage is not None:
            self.restocking_fee_percentage = restocking_fee_percentage
        if return_instructions is not None:
            self.return_instructions = return_instructions
        if return_method is not None:
            self.return_method = return_method
        if return_period is not None:
            self.return_period = return_period
        if returns_accepted is not None:
            self.returns_accepted = returns_accepted
        if return_shipping_cost_payer is not None:
            self.return_shipping_cost_payer = return_shipping_cost_payer

    @property
    def category_types(self):
        """Gets the category_types of this ReturnPolicyRequest.  # noqa: E501

        This container indicates which category group that the return policy applies to.<br/><br/><span class=\"tablenote\"><b>Note</b>: Return business policies are not applicable to motor vehicle listings, so the <b>categoryTypes.name</b> value must be set to <code>ALL_EXCLUDING_MOTORS_VEHICLES</code> for return business policies.</span>  # noqa: E501

        :return: The category_types of this ReturnPolicyRequest.  # noqa: E501
        :rtype: list[CategoryType]
        """
        return self._category_types

    @category_types.setter
    def category_types(self, category_types):
        """Sets the category_types of this ReturnPolicyRequest.

        This container indicates which category group that the return policy applies to.<br/><br/><span class=\"tablenote\"><b>Note</b>: Return business policies are not applicable to motor vehicle listings, so the <b>categoryTypes.name</b> value must be set to <code>ALL_EXCLUDING_MOTORS_VEHICLES</code> for return business policies.</span>  # noqa: E501

        :param category_types: The category_types of this ReturnPolicyRequest.  # noqa: E501
        :type: list[CategoryType]
        """

        self._category_types = category_types

    @property
    def description(self):
        """Gets the description of this ReturnPolicyRequest.  # noqa: E501

        A seller-defined description of the return business policy. This description is only for the seller's use, and is not exposed on any eBay pages.  <br/><br/><b>Max length</b>: 250  # noqa: E501

        :return: The description of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReturnPolicyRequest.

        A seller-defined description of the return business policy. This description is only for the seller's use, and is not exposed on any eBay pages.  <br/><br/><b>Max length</b>: 250  # noqa: E501

        :param description: The description of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def extended_holiday_returns_offered(self):
        """Gets the extended_holiday_returns_offered of this ReturnPolicyRequest.  # noqa: E501

        <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> This field is deprecated, since eBay no longer supports extended holiday returns. Any value supplied in this field is neither read nor returned.</p>   # noqa: E501

        :return: The extended_holiday_returns_offered of this ReturnPolicyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._extended_holiday_returns_offered

    @extended_holiday_returns_offered.setter
    def extended_holiday_returns_offered(self, extended_holiday_returns_offered):
        """Sets the extended_holiday_returns_offered of this ReturnPolicyRequest.

        <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> This field is deprecated, since eBay no longer supports extended holiday returns. Any value supplied in this field is neither read nor returned.</p>   # noqa: E501

        :param extended_holiday_returns_offered: The extended_holiday_returns_offered of this ReturnPolicyRequest.  # noqa: E501
        :type: bool
        """

        self._extended_holiday_returns_offered = extended_holiday_returns_offered

    @property
    def international_override(self):
        """Gets the international_override of this ReturnPolicyRequest.  # noqa: E501


        :return: The international_override of this ReturnPolicyRequest.  # noqa: E501
        :rtype: InternationalReturnOverrideType
        """
        return self._international_override

    @international_override.setter
    def international_override(self, international_override):
        """Sets the international_override of this ReturnPolicyRequest.


        :param international_override: The international_override of this ReturnPolicyRequest.  # noqa: E501
        :type: InternationalReturnOverrideType
        """

        self._international_override = international_override

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this ReturnPolicyRequest.  # noqa: E501

        The ID of the eBay marketplace to which this return business policy applies.  For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this ReturnPolicyRequest.

        The ID of the eBay marketplace to which this return business policy applies.  For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def name(self):
        """Gets the name of this ReturnPolicyRequest.  # noqa: E501

        A seller-defined name for this return business policy. Names must be unique for policies assigned to the same marketplace. <br/><br/><b>Max length</b>: 64  # noqa: E501

        :return: The name of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReturnPolicyRequest.

        A seller-defined name for this return business policy. Names must be unique for policies assigned to the same marketplace. <br/><br/><b>Max length</b>: 64  # noqa: E501

        :param name: The name of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def refund_method(self):
        """Gets the refund_method of this ReturnPolicyRequest.  # noqa: E501

        This value indicates the refund method that will be used by the seller for buyer returns.<p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> If this field is not included in a return business policy, it will default to MONEY_BACK.</p> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:RefundMethodEnum'>eBay API documentation</a>  # noqa: E501

        :return: The refund_method of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._refund_method

    @refund_method.setter
    def refund_method(self, refund_method):
        """Sets the refund_method of this ReturnPolicyRequest.

        This value indicates the refund method that will be used by the seller for buyer returns.<p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> If this field is not included in a return business policy, it will default to MONEY_BACK.</p> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:RefundMethodEnum'>eBay API documentation</a>  # noqa: E501

        :param refund_method: The refund_method of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._refund_method = refund_method

    @property
    def restocking_fee_percentage(self):
        """Gets the restocking_fee_percentage of this ReturnPolicyRequest.  # noqa: E501

        <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> This field is deprecated, since eBay no longer allows sellers to charge a restocking fee for buyer remorse returns. If this field is included, it is ignored.</p>  # noqa: E501

        :return: The restocking_fee_percentage of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._restocking_fee_percentage

    @restocking_fee_percentage.setter
    def restocking_fee_percentage(self, restocking_fee_percentage):
        """Sets the restocking_fee_percentage of this ReturnPolicyRequest.

        <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> This field is deprecated, since eBay no longer allows sellers to charge a restocking fee for buyer remorse returns. If this field is included, it is ignored.</p>  # noqa: E501

        :param restocking_fee_percentage: The restocking_fee_percentage of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._restocking_fee_percentage = restocking_fee_percentage

    @property
    def return_instructions(self):
        """Gets the return_instructions of this ReturnPolicyRequest.  # noqa: E501

        This text-based field provides more details on seller-specified return instructions. <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> This field is no longer supported on many eBay marketplaces. To see if a marketplace and eBay category does support this field, call <a href=\"/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies\">getReturnPolicies</a> method of the <b>Metadata API</b>. Then you will look for the <b>policyDescriptionEnabled</b> field with a value of <code>true</code> for the eBay category.</span></p><br/><b>Max length</b>: 5000 (8000 for DE)  # noqa: E501

        :return: The return_instructions of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_instructions

    @return_instructions.setter
    def return_instructions(self, return_instructions):
        """Sets the return_instructions of this ReturnPolicyRequest.

        This text-based field provides more details on seller-specified return instructions. <p class=\"tablenote\"><span  style=\"color: #dd1e31;\"><b>Important!</b></span> This field is no longer supported on many eBay marketplaces. To see if a marketplace and eBay category does support this field, call <a href=\"/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies\">getReturnPolicies</a> method of the <b>Metadata API</b>. Then you will look for the <b>policyDescriptionEnabled</b> field with a value of <code>true</code> for the eBay category.</span></p><br/><b>Max length</b>: 5000 (8000 for DE)  # noqa: E501

        :param return_instructions: The return_instructions of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._return_instructions = return_instructions

    @property
    def return_method(self):
        """Gets the return_method of this ReturnPolicyRequest.  # noqa: E501

        This field can be used if the seller is willing and able to offer a replacement item as an alternative to 'Money Back'. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnMethodEnum'>eBay API documentation</a>  # noqa: E501

        :return: The return_method of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_method

    @return_method.setter
    def return_method(self, return_method):
        """Sets the return_method of this ReturnPolicyRequest.

        This field can be used if the seller is willing and able to offer a replacement item as an alternative to 'Money Back'. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnMethodEnum'>eBay API documentation</a>  # noqa: E501

        :param return_method: The return_method of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._return_method = return_method

    @property
    def return_period(self):
        """Gets the return_period of this ReturnPolicyRequest.  # noqa: E501


        :return: The return_period of this ReturnPolicyRequest.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._return_period

    @return_period.setter
    def return_period(self, return_period):
        """Sets the return_period of this ReturnPolicyRequest.


        :param return_period: The return_period of this ReturnPolicyRequest.  # noqa: E501
        :type: TimeDuration
        """

        self._return_period = return_period

    @property
    def returns_accepted(self):
        """Gets the returns_accepted of this ReturnPolicyRequest.  # noqa: E501

        If set to <code>true</code>, the seller accepts returns. <p><span class=\"tablenote\"><strong>Note:</strong>Top-Rated sellers must accept item returns and the <b>handlingTime</b> should be set to zero days or one day for a listing to receive a Top-Rated Plus badge on the View Item or search result pages. For more information on eBay's Top-Rated seller program, see <a href=\"http://pages.ebay.com/help/sell/top-rated.html \">Becoming a Top Rated Seller and qualifying for Top Rated Plus benefits</a>.</span></p>  # noqa: E501

        :return: The returns_accepted of this ReturnPolicyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._returns_accepted

    @returns_accepted.setter
    def returns_accepted(self, returns_accepted):
        """Sets the returns_accepted of this ReturnPolicyRequest.

        If set to <code>true</code>, the seller accepts returns. <p><span class=\"tablenote\"><strong>Note:</strong>Top-Rated sellers must accept item returns and the <b>handlingTime</b> should be set to zero days or one day for a listing to receive a Top-Rated Plus badge on the View Item or search result pages. For more information on eBay's Top-Rated seller program, see <a href=\"http://pages.ebay.com/help/sell/top-rated.html \">Becoming a Top Rated Seller and qualifying for Top Rated Plus benefits</a>.</span></p>  # noqa: E501

        :param returns_accepted: The returns_accepted of this ReturnPolicyRequest.  # noqa: E501
        :type: bool
        """

        self._returns_accepted = returns_accepted

    @property
    def return_shipping_cost_payer(self):
        """Gets the return_shipping_cost_payer of this ReturnPolicyRequest.  # noqa: E501

        This field indicates who is responsible for paying for the shipping charges for returned items. The field can be set to either <code>BUYER</code> or <code>SELLER</code>.  <br/><br/>Depending on the return policy and specifics of the return, either the buyer or the seller can be responsible for the return shipping costs. Note that the seller is always responsible for return shipping costs for SNAD-related issues.  <br/><br/>This field is conditionally required if <b>returnsAccepted</b> is set to <code>true</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnShippingCostPayerEnum'>eBay API documentation</a>  # noqa: E501

        :return: The return_shipping_cost_payer of this ReturnPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_shipping_cost_payer

    @return_shipping_cost_payer.setter
    def return_shipping_cost_payer(self, return_shipping_cost_payer):
        """Sets the return_shipping_cost_payer of this ReturnPolicyRequest.

        This field indicates who is responsible for paying for the shipping charges for returned items. The field can be set to either <code>BUYER</code> or <code>SELLER</code>.  <br/><br/>Depending on the return policy and specifics of the return, either the buyer or the seller can be responsible for the return shipping costs. Note that the seller is always responsible for return shipping costs for SNAD-related issues.  <br/><br/>This field is conditionally required if <b>returnsAccepted</b> is set to <code>true</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnShippingCostPayerEnum'>eBay API documentation</a>  # noqa: E501

        :param return_shipping_cost_payer: The return_shipping_cost_payer of this ReturnPolicyRequest.  # noqa: E501
        :type: str
        """

        self._return_shipping_cost_payer = return_shipping_cost_payer

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
        if issubclass(ReturnPolicyRequest, dict):
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
        if not isinstance(other, ReturnPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
