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

class ShippingStep(object):
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
        'ship_to': 'ExtendedContact',
        'ship_to_reference_id': 'str',
        'shipping_carrier_code': 'str',
        'shipping_service_code': 'str'
    }

    attribute_map = {
        'ship_to': 'shipTo',
        'ship_to_reference_id': 'shipToReferenceId',
        'shipping_carrier_code': 'shippingCarrierCode',
        'shipping_service_code': 'shippingServiceCode'
    }

    def __init__(self, ship_to=None, ship_to_reference_id=None, shipping_carrier_code=None, shipping_service_code=None):  # noqa: E501
        """ShippingStep - a model defined in Swagger"""  # noqa: E501
        self._ship_to = None
        self._ship_to_reference_id = None
        self._shipping_carrier_code = None
        self._shipping_service_code = None
        self.discriminator = None
        if ship_to is not None:
            self.ship_to = ship_to
        if ship_to_reference_id is not None:
            self.ship_to_reference_id = ship_to_reference_id
        if shipping_carrier_code is not None:
            self.shipping_carrier_code = shipping_carrier_code
        if shipping_service_code is not None:
            self.shipping_service_code = shipping_service_code

    @property
    def ship_to(self):
        """Gets the ship_to of this ShippingStep.  # noqa: E501


        :return: The ship_to of this ShippingStep.  # noqa: E501
        :rtype: ExtendedContact
        """
        return self._ship_to

    @ship_to.setter
    def ship_to(self, ship_to):
        """Sets the ship_to of this ShippingStep.


        :param ship_to: The ship_to of this ShippingStep.  # noqa: E501
        :type: ExtendedContact
        """

        self._ship_to = ship_to

    @property
    def ship_to_reference_id(self):
        """Gets the ship_to_reference_id of this ShippingStep.  # noqa: E501

        This is the unique identifer of the Global Shipping Program (GSP) shipment. This field is only returned if the line item is being shipped via GSP (the value of the <b>fulfillmentStartInstructions.ebaySupportedFulfillment</b> field will be <code>true</code>. The international shipping provider uses the <b>shipToReferenceId</b> value as the primary reference number to retrieve the relevant details about the buyer, the order, and the fulfillment, so the shipment can be completed. <br /><br />Sellers must include this value on the shipping label immediately above the street address of the international shipping provider. <br /><br />Example: \"Reference #1234567890123456\" <br /><br /><span class=\"tablenote\"><strong>Note:</strong> This value is the same as the <b>ShipToAddress.ReferenceID</b> value returned by the Trading API's GetOrders call.</span>  # noqa: E501

        :return: The ship_to_reference_id of this ShippingStep.  # noqa: E501
        :rtype: str
        """
        return self._ship_to_reference_id

    @ship_to_reference_id.setter
    def ship_to_reference_id(self, ship_to_reference_id):
        """Sets the ship_to_reference_id of this ShippingStep.

        This is the unique identifer of the Global Shipping Program (GSP) shipment. This field is only returned if the line item is being shipped via GSP (the value of the <b>fulfillmentStartInstructions.ebaySupportedFulfillment</b> field will be <code>true</code>. The international shipping provider uses the <b>shipToReferenceId</b> value as the primary reference number to retrieve the relevant details about the buyer, the order, and the fulfillment, so the shipment can be completed. <br /><br />Sellers must include this value on the shipping label immediately above the street address of the international shipping provider. <br /><br />Example: \"Reference #1234567890123456\" <br /><br /><span class=\"tablenote\"><strong>Note:</strong> This value is the same as the <b>ShipToAddress.ReferenceID</b> value returned by the Trading API's GetOrders call.</span>  # noqa: E501

        :param ship_to_reference_id: The ship_to_reference_id of this ShippingStep.  # noqa: E501
        :type: str
        """

        self._ship_to_reference_id = ship_to_reference_id

    @property
    def shipping_carrier_code(self):
        """Gets the shipping_carrier_code of this ShippingStep.  # noqa: E501

        The unique identifier of the shipping carrier being used to ship the line item. <br /><br /><span class=\"tablenote\"><strong>Note:</strong> The Trading API's <a href=\"https://developer.ebay.com/devzone/XML/docs/Reference/eBay/GeteBayDetails.html \" target=\"_blank\">GeteBayDetails</a> call can be used to retrieve the latest shipping carrier and shipping service option enumeration values.</span>  # noqa: E501

        :return: The shipping_carrier_code of this ShippingStep.  # noqa: E501
        :rtype: str
        """
        return self._shipping_carrier_code

    @shipping_carrier_code.setter
    def shipping_carrier_code(self, shipping_carrier_code):
        """Sets the shipping_carrier_code of this ShippingStep.

        The unique identifier of the shipping carrier being used to ship the line item. <br /><br /><span class=\"tablenote\"><strong>Note:</strong> The Trading API's <a href=\"https://developer.ebay.com/devzone/XML/docs/Reference/eBay/GeteBayDetails.html \" target=\"_blank\">GeteBayDetails</a> call can be used to retrieve the latest shipping carrier and shipping service option enumeration values.</span>  # noqa: E501

        :param shipping_carrier_code: The shipping_carrier_code of this ShippingStep.  # noqa: E501
        :type: str
        """

        self._shipping_carrier_code = shipping_carrier_code

    @property
    def shipping_service_code(self):
        """Gets the shipping_service_code of this ShippingStep.  # noqa: E501

        The unique identifier of the shipping service option being used to ship the line item.<br /><br /><span class=\"tablenote\"><strong>Note:</strong> Use the Trading API's <a href=\"https://developer.ebay.com/devzone/XML/docs/Reference/eBay/GeteBayDetails.html \" target=\"_blank\">GeteBayDetails</a> call to retrieve the latest shipping carrier and shipping service option enumeration values. When making the <a href=\"https://developer.ebay.com/devzone/XML/docs/Reference/eBay/GeteBayDetails.html \" target=\"_blank\">GeteBayDetails</a> call, include the <strong>DetailName</strong> field in the request payload and set its value to <code>ShippingServiceDetails</code>. Each valid shipping service option (returned in <strong>ShippingServiceDetails.ShippingService</strong> field) and corresponding shipping carrier (returned in <strong>ShippingServiceDetails.ShippingCarrier</strong> field) is returned in response payload.</span>  # noqa: E501

        :return: The shipping_service_code of this ShippingStep.  # noqa: E501
        :rtype: str
        """
        return self._shipping_service_code

    @shipping_service_code.setter
    def shipping_service_code(self, shipping_service_code):
        """Sets the shipping_service_code of this ShippingStep.

        The unique identifier of the shipping service option being used to ship the line item.<br /><br /><span class=\"tablenote\"><strong>Note:</strong> Use the Trading API's <a href=\"https://developer.ebay.com/devzone/XML/docs/Reference/eBay/GeteBayDetails.html \" target=\"_blank\">GeteBayDetails</a> call to retrieve the latest shipping carrier and shipping service option enumeration values. When making the <a href=\"https://developer.ebay.com/devzone/XML/docs/Reference/eBay/GeteBayDetails.html \" target=\"_blank\">GeteBayDetails</a> call, include the <strong>DetailName</strong> field in the request payload and set its value to <code>ShippingServiceDetails</code>. Each valid shipping service option (returned in <strong>ShippingServiceDetails.ShippingService</strong> field) and corresponding shipping carrier (returned in <strong>ShippingServiceDetails.ShippingCarrier</strong> field) is returned in response payload.</span>  # noqa: E501

        :param shipping_service_code: The shipping_service_code of this ShippingStep.  # noqa: E501
        :type: str
        """

        self._shipping_service_code = shipping_service_code

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
        if issubclass(ShippingStep, dict):
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
        if not isinstance(other, ShippingStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
