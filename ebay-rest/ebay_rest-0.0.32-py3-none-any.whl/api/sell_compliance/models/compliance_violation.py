# coding: utf-8

"""
    Compliance API

    Service for providing information to sellers about their listings being non-compliant, or at risk for becoming non-compliant, against eBay listing policies.  # noqa: E501

    OpenAPI spec version: 1.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ComplianceViolation(object):
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
        'compliance_type': 'str',
        'listing_id': 'str',
        'sku': 'str',
        'offer_id': 'str',
        'violations': 'list[ComplianceDetail]'
    }

    attribute_map = {
        'compliance_type': 'complianceType',
        'listing_id': 'listingId',
        'sku': 'sku',
        'offer_id': 'offerId',
        'violations': 'violations'
    }

    def __init__(self, compliance_type=None, listing_id=None, sku=None, offer_id=None, violations=None):  # noqa: E501
        """ComplianceViolation - a model defined in Swagger"""  # noqa: E501
        self._compliance_type = None
        self._listing_id = None
        self._sku = None
        self._offer_id = None
        self._violations = None
        self.discriminator = None
        if compliance_type is not None:
            self.compliance_type = compliance_type
        if listing_id is not None:
            self.listing_id = listing_id
        if sku is not None:
            self.sku = sku
        if offer_id is not None:
            self.offer_id = offer_id
        if violations is not None:
            self.violations = violations

    @property
    def compliance_type(self):
        """Gets the compliance_type of this ComplianceViolation.  # noqa: E501

        This enumeration value indicates the compliance type of listing violation. See ComplianceTypeEnum for more information on each compliance type. This will always be returned for each listing violation that is found. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/compliance/types/com:ComplianceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The compliance_type of this ComplianceViolation.  # noqa: E501
        :rtype: str
        """
        return self._compliance_type

    @compliance_type.setter
    def compliance_type(self, compliance_type):
        """Sets the compliance_type of this ComplianceViolation.

        This enumeration value indicates the compliance type of listing violation. See ComplianceTypeEnum for more information on each compliance type. This will always be returned for each listing violation that is found. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/compliance/types/com:ComplianceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param compliance_type: The compliance_type of this ComplianceViolation.  # noqa: E501
        :type: str
        """

        self._compliance_type = compliance_type

    @property
    def listing_id(self):
        """Gets the listing_id of this ComplianceViolation.  # noqa: E501

        The unique identifier of the eBay listing that currently has the corresponding listing violation{s). This field will always be returned for each listing that has one or more violations.  # noqa: E501

        :return: The listing_id of this ComplianceViolation.  # noqa: E501
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """Sets the listing_id of this ComplianceViolation.

        The unique identifier of the eBay listing that currently has the corresponding listing violation{s). This field will always be returned for each listing that has one or more violations.  # noqa: E501

        :param listing_id: The listing_id of this ComplianceViolation.  # noqa: E501
        :type: str
        """

        self._listing_id = listing_id

    @property
    def sku(self):
        """Gets the sku of this ComplianceViolation.  # noqa: E501

        The seller-defined SKU value of the product in the listing with the violation{s). This field is only returned if defined in the listing. SKU values are optional in listings except when creating listings using the Inventory API model.  # noqa: E501

        :return: The sku of this ComplianceViolation.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this ComplianceViolation.

        The seller-defined SKU value of the product in the listing with the violation{s). This field is only returned if defined in the listing. SKU values are optional in listings except when creating listings using the Inventory API model.  # noqa: E501

        :param sku: The sku of this ComplianceViolation.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def offer_id(self):
        """Gets the offer_id of this ComplianceViolation.  # noqa: E501

        Note: This field is for future use, and will not be returned, even for listings created through the Inventory API. The unique identifier of the offer. This field is only applicable and returned for listings that were created through the Inventory API. To convert an Inventory Item object into an eBay listing, an Offer object must be created and published.  # noqa: E501

        :return: The offer_id of this ComplianceViolation.  # noqa: E501
        :rtype: str
        """
        return self._offer_id

    @offer_id.setter
    def offer_id(self, offer_id):
        """Sets the offer_id of this ComplianceViolation.

        Note: This field is for future use, and will not be returned, even for listings created through the Inventory API. The unique identifier of the offer. This field is only applicable and returned for listings that were created through the Inventory API. To convert an Inventory Item object into an eBay listing, an Offer object must be created and published.  # noqa: E501

        :param offer_id: The offer_id of this ComplianceViolation.  # noqa: E501
        :type: str
        """

        self._offer_id = offer_id

    @property
    def violations(self):
        """Gets the violations of this ComplianceViolation.  # noqa: E501

        This container consists of an array of one or more listing violations applicable to the eBay listing specified in the listingId field. This array is returned for each eBay listing that has one or more violations. For each returned violation, the fields that are returned and the details that are given will depend on the listing violation.  # noqa: E501

        :return: The violations of this ComplianceViolation.  # noqa: E501
        :rtype: list[ComplianceDetail]
        """
        return self._violations

    @violations.setter
    def violations(self, violations):
        """Sets the violations of this ComplianceViolation.

        This container consists of an array of one or more listing violations applicable to the eBay listing specified in the listingId field. This array is returned for each eBay listing that has one or more violations. For each returned violation, the fields that are returned and the details that are given will depend on the listing violation.  # noqa: E501

        :param violations: The violations of this ComplianceViolation.  # noqa: E501
        :type: list[ComplianceDetail]
        """

        self._violations = violations

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
        if issubclass(ComplianceViolation, dict):
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
        if not isinstance(other, ComplianceViolation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
