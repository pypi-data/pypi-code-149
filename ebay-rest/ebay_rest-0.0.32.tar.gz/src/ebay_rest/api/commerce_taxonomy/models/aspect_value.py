# coding: utf-8

"""
    Taxonomy API

    Use the Taxonomy API to discover the most appropriate eBay categories under which sellers can offer inventory items for sale, and the most likely categories under which buyers can browse or search for items to purchase. In addition, the Taxonomy API provides metadata about the required and recommended category aspects to include in listings, and also has two operations to retrieve parts compatibility information.  # noqa: E501

    OpenAPI spec version: v1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AspectValue(object):
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
        'localized_value': 'str',
        'value_constraints': 'list[ValueConstraint]'
    }

    attribute_map = {
        'localized_value': 'localizedValue',
        'value_constraints': 'valueConstraints'
    }

    def __init__(self, localized_value=None, value_constraints=None):  # noqa: E501
        """AspectValue - a model defined in Swagger"""  # noqa: E501
        self._localized_value = None
        self._value_constraints = None
        self.discriminator = None
        if localized_value is not None:
            self.localized_value = localized_value
        if value_constraints is not None:
            self.value_constraints = value_constraints

    @property
    def localized_value(self):
        """Gets the localized_value of this AspectValue.  # noqa: E501

        The localized value of this aspect.<br /><br />          <span class=\"tablenote\"> <strong>Note:</strong> This value is always localized for the specified marketplace. </span>  # noqa: E501

        :return: The localized_value of this AspectValue.  # noqa: E501
        :rtype: str
        """
        return self._localized_value

    @localized_value.setter
    def localized_value(self, localized_value):
        """Sets the localized_value of this AspectValue.

        The localized value of this aspect.<br /><br />          <span class=\"tablenote\"> <strong>Note:</strong> This value is always localized for the specified marketplace. </span>  # noqa: E501

        :param localized_value: The localized_value of this AspectValue.  # noqa: E501
        :type: str
        """

        self._localized_value = localized_value

    @property
    def value_constraints(self):
        """Gets the value_constraints of this AspectValue.  # noqa: E501

        <i>Not returned if</i> the value of the <b>localizedValue</b> field can always be selected for this aspect of the specified category.<br /><br />Contains a list of the dependencies that identify when the value of the <b>localizedValue</b> field is available for the current aspect. Each dependency specifies the values of another aspect of the same category (a <i>control</i> aspect), for which the current value of the current aspect can also be selected by the seller. <br /><br />          <b>Example:</b> A shirt is available in three sizes and three colors, but only the Small and Medium sizes come in Green. Thus for the Color aspect, the value Green is constrained by its dependency on Size (the control aspect). Only when the Size aspect value is Small or Medium, can the Color aspect value of Green be selected by the seller.  # noqa: E501

        :return: The value_constraints of this AspectValue.  # noqa: E501
        :rtype: list[ValueConstraint]
        """
        return self._value_constraints

    @value_constraints.setter
    def value_constraints(self, value_constraints):
        """Sets the value_constraints of this AspectValue.

        <i>Not returned if</i> the value of the <b>localizedValue</b> field can always be selected for this aspect of the specified category.<br /><br />Contains a list of the dependencies that identify when the value of the <b>localizedValue</b> field is available for the current aspect. Each dependency specifies the values of another aspect of the same category (a <i>control</i> aspect), for which the current value of the current aspect can also be selected by the seller. <br /><br />          <b>Example:</b> A shirt is available in three sizes and three colors, but only the Small and Medium sizes come in Green. Thus for the Color aspect, the value Green is constrained by its dependency on Size (the control aspect). Only when the Size aspect value is Small or Medium, can the Color aspect value of Green be selected by the seller.  # noqa: E501

        :param value_constraints: The value_constraints of this AspectValue.  # noqa: E501
        :type: list[ValueConstraint]
        """

        self._value_constraints = value_constraints

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
        if issubclass(AspectValue, dict):
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
        if not isinstance(other, AspectValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
