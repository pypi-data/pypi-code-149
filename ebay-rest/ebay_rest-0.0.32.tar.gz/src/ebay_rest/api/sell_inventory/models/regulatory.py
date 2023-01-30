# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.16.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Regulatory(object):
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
        'hazmat': 'Hazmat',
        'repair_score': 'float'
    }

    attribute_map = {
        'hazmat': 'hazmat',
        'repair_score': 'repairScore'
    }

    def __init__(self, hazmat=None, repair_score=None):  # noqa: E501
        """Regulatory - a model defined in Swagger"""  # noqa: E501
        self._hazmat = None
        self._repair_score = None
        self.discriminator = None
        if hazmat is not None:
            self.hazmat = hazmat
        if repair_score is not None:
            self.repair_score = repair_score

    @property
    def hazmat(self):
        """Gets the hazmat of this Regulatory.  # noqa: E501


        :return: The hazmat of this Regulatory.  # noqa: E501
        :rtype: Hazmat
        """
        return self._hazmat

    @hazmat.setter
    def hazmat(self, hazmat):
        """Sets the hazmat of this Regulatory.


        :param hazmat: The hazmat of this Regulatory.  # noqa: E501
        :type: Hazmat
        """

        self._hazmat = hazmat

    @property
    def repair_score(self):
        """Gets the repair_score of this Regulatory.  # noqa: E501

        This field represents the repair index for the listing.<br><br>The repair index identifies the manufacturer's repair score for a product (i.e., how easy is it to repair the product.) This field is a floating point value between 0.0 (i.e., difficult to repair,) and 10.0 (i.e., easily repaired.)<br><br>The format for <b>repairScore</b> is limited to one decimal place. For example:<ul><li><code>7.9</code> and <code>0.0</code> are both valid scores</li><li><code>5.645</code> and <code>2.10</code> are both invalid scores</li></ul><br><span class=\"tablenote\"><b>Note:</b> This field is currently only applicable to a limited number of categories in the French marketplace. Use the <a href=\"/api-docs/sell/metadata/resources/marketplace/methods/getExtendedProducerResponsibilityPolicies\" target=\"_blank\">getExtendedProducerResponsibilityPolicies</a> method to return the list of categories that support repair score. In the response, look for all categories that show REPAIR_SCORE in the <a href=\"/api-docs/sell/metadata/resources/marketplace/methods/getExtendedProducerResponsibilityPolicies#response.extendedProducerResponsibilities.supportedAttributes.name\" target=\"_blank\">supportedAttributes.name</a> field, and the corresponding usage field will indicate if repair score is optional, recommended, or required for that category.</span>  # noqa: E501

        :return: The repair_score of this Regulatory.  # noqa: E501
        :rtype: float
        """
        return self._repair_score

    @repair_score.setter
    def repair_score(self, repair_score):
        """Sets the repair_score of this Regulatory.

        This field represents the repair index for the listing.<br><br>The repair index identifies the manufacturer's repair score for a product (i.e., how easy is it to repair the product.) This field is a floating point value between 0.0 (i.e., difficult to repair,) and 10.0 (i.e., easily repaired.)<br><br>The format for <b>repairScore</b> is limited to one decimal place. For example:<ul><li><code>7.9</code> and <code>0.0</code> are both valid scores</li><li><code>5.645</code> and <code>2.10</code> are both invalid scores</li></ul><br><span class=\"tablenote\"><b>Note:</b> This field is currently only applicable to a limited number of categories in the French marketplace. Use the <a href=\"/api-docs/sell/metadata/resources/marketplace/methods/getExtendedProducerResponsibilityPolicies\" target=\"_blank\">getExtendedProducerResponsibilityPolicies</a> method to return the list of categories that support repair score. In the response, look for all categories that show REPAIR_SCORE in the <a href=\"/api-docs/sell/metadata/resources/marketplace/methods/getExtendedProducerResponsibilityPolicies#response.extendedProducerResponsibilities.supportedAttributes.name\" target=\"_blank\">supportedAttributes.name</a> field, and the corresponding usage field will indicate if repair score is optional, recommended, or required for that category.</span>  # noqa: E501

        :param repair_score: The repair_score of this Regulatory.  # noqa: E501
        :type: float
        """

        self._repair_score = repair_score

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
        if issubclass(Regulatory, dict):
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
        if not isinstance(other, Regulatory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
