# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Resource\" title=\"Experimental Resource\" />&nbsp;(Experimental Resource)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Resource\" title=\"Experimental Resource\" />&nbsp;(Experimental Resource)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.18.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShippingOption(object):
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
        'additional_shipping_cost_per_unit': 'ConvertedAmount',
        'cut_off_date_used_for_estimate': 'str',
        'fulfilled_through': 'str',
        'guaranteed_delivery': 'bool',
        'import_charges': 'ConvertedAmount',
        'max_estimated_delivery_date': 'str',
        'min_estimated_delivery_date': 'str',
        'quantity_used_for_estimate': 'int',
        'shipping_carrier_code': 'str',
        'shipping_cost': 'ConvertedAmount',
        'shipping_cost_type': 'str',
        'shipping_service_code': 'str',
        'ship_to_location_used_for_estimate': 'ShipToLocation',
        'trademark_symbol': 'str',
        'type': 'str'
    }

    attribute_map = {
        'additional_shipping_cost_per_unit': 'additionalShippingCostPerUnit',
        'cut_off_date_used_for_estimate': 'cutOffDateUsedForEstimate',
        'fulfilled_through': 'fulfilledThrough',
        'guaranteed_delivery': 'guaranteedDelivery',
        'import_charges': 'importCharges',
        'max_estimated_delivery_date': 'maxEstimatedDeliveryDate',
        'min_estimated_delivery_date': 'minEstimatedDeliveryDate',
        'quantity_used_for_estimate': 'quantityUsedForEstimate',
        'shipping_carrier_code': 'shippingCarrierCode',
        'shipping_cost': 'shippingCost',
        'shipping_cost_type': 'shippingCostType',
        'shipping_service_code': 'shippingServiceCode',
        'ship_to_location_used_for_estimate': 'shipToLocationUsedForEstimate',
        'trademark_symbol': 'trademarkSymbol',
        'type': 'type'
    }

    def __init__(self, additional_shipping_cost_per_unit=None, cut_off_date_used_for_estimate=None, fulfilled_through=None, guaranteed_delivery=None, import_charges=None, max_estimated_delivery_date=None, min_estimated_delivery_date=None, quantity_used_for_estimate=None, shipping_carrier_code=None, shipping_cost=None, shipping_cost_type=None, shipping_service_code=None, ship_to_location_used_for_estimate=None, trademark_symbol=None, type=None):  # noqa: E501
        """ShippingOption - a model defined in Swagger"""  # noqa: E501
        self._additional_shipping_cost_per_unit = None
        self._cut_off_date_used_for_estimate = None
        self._fulfilled_through = None
        self._guaranteed_delivery = None
        self._import_charges = None
        self._max_estimated_delivery_date = None
        self._min_estimated_delivery_date = None
        self._quantity_used_for_estimate = None
        self._shipping_carrier_code = None
        self._shipping_cost = None
        self._shipping_cost_type = None
        self._shipping_service_code = None
        self._ship_to_location_used_for_estimate = None
        self._trademark_symbol = None
        self._type = None
        self.discriminator = None
        if additional_shipping_cost_per_unit is not None:
            self.additional_shipping_cost_per_unit = additional_shipping_cost_per_unit
        if cut_off_date_used_for_estimate is not None:
            self.cut_off_date_used_for_estimate = cut_off_date_used_for_estimate
        if fulfilled_through is not None:
            self.fulfilled_through = fulfilled_through
        if guaranteed_delivery is not None:
            self.guaranteed_delivery = guaranteed_delivery
        if import_charges is not None:
            self.import_charges = import_charges
        if max_estimated_delivery_date is not None:
            self.max_estimated_delivery_date = max_estimated_delivery_date
        if min_estimated_delivery_date is not None:
            self.min_estimated_delivery_date = min_estimated_delivery_date
        if quantity_used_for_estimate is not None:
            self.quantity_used_for_estimate = quantity_used_for_estimate
        if shipping_carrier_code is not None:
            self.shipping_carrier_code = shipping_carrier_code
        if shipping_cost is not None:
            self.shipping_cost = shipping_cost
        if shipping_cost_type is not None:
            self.shipping_cost_type = shipping_cost_type
        if shipping_service_code is not None:
            self.shipping_service_code = shipping_service_code
        if ship_to_location_used_for_estimate is not None:
            self.ship_to_location_used_for_estimate = ship_to_location_used_for_estimate
        if trademark_symbol is not None:
            self.trademark_symbol = trademark_symbol
        if type is not None:
            self.type = type

    @property
    def additional_shipping_cost_per_unit(self):
        """Gets the additional_shipping_cost_per_unit of this ShippingOption.  # noqa: E501


        :return: The additional_shipping_cost_per_unit of this ShippingOption.  # noqa: E501
        :rtype: ConvertedAmount
        """
        return self._additional_shipping_cost_per_unit

    @additional_shipping_cost_per_unit.setter
    def additional_shipping_cost_per_unit(self, additional_shipping_cost_per_unit):
        """Sets the additional_shipping_cost_per_unit of this ShippingOption.


        :param additional_shipping_cost_per_unit: The additional_shipping_cost_per_unit of this ShippingOption.  # noqa: E501
        :type: ConvertedAmount
        """

        self._additional_shipping_cost_per_unit = additional_shipping_cost_per_unit

    @property
    def cut_off_date_used_for_estimate(self):
        """Gets the cut_off_date_used_for_estimate of this ShippingOption.  # noqa: E501

        The deadline date that the item must be purchased by in order to be received by the buyer within the delivery window (<b> maxEstimatedDeliveryDate</b> and  <b> minEstimatedDeliveryDate</b> fields). This field is returned only for items that are eligible for 'Same Day Handling'. For these items, the value of this field is what is displayed in the <b> Delivery</b> line on the View Item page.  <br /><br />This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.  # noqa: E501

        :return: The cut_off_date_used_for_estimate of this ShippingOption.  # noqa: E501
        :rtype: str
        """
        return self._cut_off_date_used_for_estimate

    @cut_off_date_used_for_estimate.setter
    def cut_off_date_used_for_estimate(self, cut_off_date_used_for_estimate):
        """Sets the cut_off_date_used_for_estimate of this ShippingOption.

        The deadline date that the item must be purchased by in order to be received by the buyer within the delivery window (<b> maxEstimatedDeliveryDate</b> and  <b> minEstimatedDeliveryDate</b> fields). This field is returned only for items that are eligible for 'Same Day Handling'. For these items, the value of this field is what is displayed in the <b> Delivery</b> line on the View Item page.  <br /><br />This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.  # noqa: E501

        :param cut_off_date_used_for_estimate: The cut_off_date_used_for_estimate of this ShippingOption.  # noqa: E501
        :type: str
        """

        self._cut_off_date_used_for_estimate = cut_off_date_used_for_estimate

    @property
    def fulfilled_through(self):
        """Gets the fulfilled_through of this ShippingOption.  # noqa: E501

        If the item is being shipped by the eBay <a href=\"https://pages.ebay.com/seller-center/shipping/global-shipping-program.html \">Global Shipping program</a>, this field returns <code>GLOBAL_SHIPPING</code>.<br /><br />If the item is being shipped using the eBay International Shipping program, this field returns <code>INTERNATIONAL_SHIPPING</code>. <br /><br />Otherwise, this field is null. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:FulfilledThroughEnum'>eBay API documentation</a>  # noqa: E501

        :return: The fulfilled_through of this ShippingOption.  # noqa: E501
        :rtype: str
        """
        return self._fulfilled_through

    @fulfilled_through.setter
    def fulfilled_through(self, fulfilled_through):
        """Sets the fulfilled_through of this ShippingOption.

        If the item is being shipped by the eBay <a href=\"https://pages.ebay.com/seller-center/shipping/global-shipping-program.html \">Global Shipping program</a>, this field returns <code>GLOBAL_SHIPPING</code>.<br /><br />If the item is being shipped using the eBay International Shipping program, this field returns <code>INTERNATIONAL_SHIPPING</code>. <br /><br />Otherwise, this field is null. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:FulfilledThroughEnum'>eBay API documentation</a>  # noqa: E501

        :param fulfilled_through: The fulfilled_through of this ShippingOption.  # noqa: E501
        :type: str
        """

        self._fulfilled_through = fulfilled_through

    @property
    def guaranteed_delivery(self):
        """Gets the guaranteed_delivery of this ShippingOption.  # noqa: E501

        Indicates if the seller has committed to shipping the item with eBay Guaranteed Delivery. With eBay Guaranteed Delivery, the  seller is committed to getting the line item to the buyer within 4 business days or less. See the <a href=\"https://www.ebay.com/help/buying/shipping-delivery/buying-items-ebay-guaranteed-delivery?id=4641 \">Buying items with eBay Guaranteed Delivery</a> help topic for more details about eBay Guaranteed Delivery.  # noqa: E501

        :return: The guaranteed_delivery of this ShippingOption.  # noqa: E501
        :rtype: bool
        """
        return self._guaranteed_delivery

    @guaranteed_delivery.setter
    def guaranteed_delivery(self, guaranteed_delivery):
        """Sets the guaranteed_delivery of this ShippingOption.

        Indicates if the seller has committed to shipping the item with eBay Guaranteed Delivery. With eBay Guaranteed Delivery, the  seller is committed to getting the line item to the buyer within 4 business days or less. See the <a href=\"https://www.ebay.com/help/buying/shipping-delivery/buying-items-ebay-guaranteed-delivery?id=4641 \">Buying items with eBay Guaranteed Delivery</a> help topic for more details about eBay Guaranteed Delivery.  # noqa: E501

        :param guaranteed_delivery: The guaranteed_delivery of this ShippingOption.  # noqa: E501
        :type: bool
        """

        self._guaranteed_delivery = guaranteed_delivery

    @property
    def import_charges(self):
        """Gets the import_charges of this ShippingOption.  # noqa: E501


        :return: The import_charges of this ShippingOption.  # noqa: E501
        :rtype: ConvertedAmount
        """
        return self._import_charges

    @import_charges.setter
    def import_charges(self, import_charges):
        """Sets the import_charges of this ShippingOption.


        :param import_charges: The import_charges of this ShippingOption.  # noqa: E501
        :type: ConvertedAmount
        """

        self._import_charges = import_charges

    @property
    def max_estimated_delivery_date(self):
        """Gets the max_estimated_delivery_date of this ShippingOption.  # noqa: E501

        The end date of the delivery window (latest projected delivery date).  This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer. <br /> <br /> <span class=\"tablenote\"> <b> Note: </b> For the best accuracy, always include the location of where the item is be shipped in the <code> contextualLocation</code> values of the <a href=\"/api-docs/buy/static/api-browse.html#Headers\"> <code>X-EBAY-C-ENDUSERCTX</code></a> request header.</span>   # noqa: E501

        :return: The max_estimated_delivery_date of this ShippingOption.  # noqa: E501
        :rtype: str
        """
        return self._max_estimated_delivery_date

    @max_estimated_delivery_date.setter
    def max_estimated_delivery_date(self, max_estimated_delivery_date):
        """Sets the max_estimated_delivery_date of this ShippingOption.

        The end date of the delivery window (latest projected delivery date).  This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer. <br /> <br /> <span class=\"tablenote\"> <b> Note: </b> For the best accuracy, always include the location of where the item is be shipped in the <code> contextualLocation</code> values of the <a href=\"/api-docs/buy/static/api-browse.html#Headers\"> <code>X-EBAY-C-ENDUSERCTX</code></a> request header.</span>   # noqa: E501

        :param max_estimated_delivery_date: The max_estimated_delivery_date of this ShippingOption.  # noqa: E501
        :type: str
        """

        self._max_estimated_delivery_date = max_estimated_delivery_date

    @property
    def min_estimated_delivery_date(self):
        """Gets the min_estimated_delivery_date of this ShippingOption.  # noqa: E501

        The start date of the delivery window (earliest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer. <br /> <br /><span class=\"tablenote\"> <b> Note: </b> For the best accuracy, always include the location of where the item is be shipped in the <code> contextualLocation</code> values of the <a href=\"/api-docs/buy/static/api-browse.html#Headers\"> <code>X-EBAY-C-ENDUSERCTX</code></a> request header.</span>  # noqa: E501

        :return: The min_estimated_delivery_date of this ShippingOption.  # noqa: E501
        :rtype: str
        """
        return self._min_estimated_delivery_date

    @min_estimated_delivery_date.setter
    def min_estimated_delivery_date(self, min_estimated_delivery_date):
        """Sets the min_estimated_delivery_date of this ShippingOption.

        The start date of the delivery window (earliest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer. <br /> <br /><span class=\"tablenote\"> <b> Note: </b> For the best accuracy, always include the location of where the item is be shipped in the <code> contextualLocation</code> values of the <a href=\"/api-docs/buy/static/api-browse.html#Headers\"> <code>X-EBAY-C-ENDUSERCTX</code></a> request header.</span>  # noqa: E501

        :param min_estimated_delivery_date: The min_estimated_delivery_date of this ShippingOption.  # noqa: E501
        :type: str
        """

        self._min_estimated_delivery_date = min_estimated_delivery_date

    @property
    def quantity_used_for_estimate(self):
        """Gets the quantity_used_for_estimate of this ShippingOption.  # noqa: E501

        The number of items used when calculating the estimation information.  # noqa: E501

        :return: The quantity_used_for_estimate of this ShippingOption.  # noqa: E501
        :rtype: int
        """
        return self._quantity_used_for_estimate

    @quantity_used_for_estimate.setter
    def quantity_used_for_estimate(self, quantity_used_for_estimate):
        """Sets the quantity_used_for_estimate of this ShippingOption.

        The number of items used when calculating the estimation information.  # noqa: E501

        :param quantity_used_for_estimate: The quantity_used_for_estimate of this ShippingOption.  # noqa: E501
        :type: int
        """

        self._quantity_used_for_estimate = quantity_used_for_estimate

    @property
    def shipping_carrier_code(self):
        """Gets the shipping_carrier_code of this ShippingOption.  # noqa: E501

        The name of the shipping provider, such as FedEx, or USPS.  # noqa: E501

        :return: The shipping_carrier_code of this ShippingOption.  # noqa: E501
        :rtype: str
        """
        return self._shipping_carrier_code

    @shipping_carrier_code.setter
    def shipping_carrier_code(self, shipping_carrier_code):
        """Sets the shipping_carrier_code of this ShippingOption.

        The name of the shipping provider, such as FedEx, or USPS.  # noqa: E501

        :param shipping_carrier_code: The shipping_carrier_code of this ShippingOption.  # noqa: E501
        :type: str
        """

        self._shipping_carrier_code = shipping_carrier_code

    @property
    def shipping_cost(self):
        """Gets the shipping_cost of this ShippingOption.  # noqa: E501


        :return: The shipping_cost of this ShippingOption.  # noqa: E501
        :rtype: ConvertedAmount
        """
        return self._shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, shipping_cost):
        """Sets the shipping_cost of this ShippingOption.


        :param shipping_cost: The shipping_cost of this ShippingOption.  # noqa: E501
        :type: ConvertedAmount
        """

        self._shipping_cost = shipping_cost

    @property
    def shipping_cost_type(self):
        """Gets the shipping_cost_type of this ShippingOption.  # noqa: E501

        Indicates the class of the shipping cost. <br /><br /><b> Valid Values: </b> FIXED or CALCULATED <br /><br />Code so that your app gracefully handles any future changes to this list.   # noqa: E501

        :return: The shipping_cost_type of this ShippingOption.  # noqa: E501
        :rtype: str
        """
        return self._shipping_cost_type

    @shipping_cost_type.setter
    def shipping_cost_type(self, shipping_cost_type):
        """Sets the shipping_cost_type of this ShippingOption.

        Indicates the class of the shipping cost. <br /><br /><b> Valid Values: </b> FIXED or CALCULATED <br /><br />Code so that your app gracefully handles any future changes to this list.   # noqa: E501

        :param shipping_cost_type: The shipping_cost_type of this ShippingOption.  # noqa: E501
        :type: str
        """

        self._shipping_cost_type = shipping_cost_type

    @property
    def shipping_service_code(self):
        """Gets the shipping_service_code of this ShippingOption.  # noqa: E501

        The type of shipping service. For example, USPS First Class.  # noqa: E501

        :return: The shipping_service_code of this ShippingOption.  # noqa: E501
        :rtype: str
        """
        return self._shipping_service_code

    @shipping_service_code.setter
    def shipping_service_code(self, shipping_service_code):
        """Sets the shipping_service_code of this ShippingOption.

        The type of shipping service. For example, USPS First Class.  # noqa: E501

        :param shipping_service_code: The shipping_service_code of this ShippingOption.  # noqa: E501
        :type: str
        """

        self._shipping_service_code = shipping_service_code

    @property
    def ship_to_location_used_for_estimate(self):
        """Gets the ship_to_location_used_for_estimate of this ShippingOption.  # noqa: E501


        :return: The ship_to_location_used_for_estimate of this ShippingOption.  # noqa: E501
        :rtype: ShipToLocation
        """
        return self._ship_to_location_used_for_estimate

    @ship_to_location_used_for_estimate.setter
    def ship_to_location_used_for_estimate(self, ship_to_location_used_for_estimate):
        """Sets the ship_to_location_used_for_estimate of this ShippingOption.


        :param ship_to_location_used_for_estimate: The ship_to_location_used_for_estimate of this ShippingOption.  # noqa: E501
        :type: ShipToLocation
        """

        self._ship_to_location_used_for_estimate = ship_to_location_used_for_estimate

    @property
    def trademark_symbol(self):
        """Gets the trademark_symbol of this ShippingOption.  # noqa: E501

        Any trademark symbol, such as &#8482; or &reg;, that needs to be shown in superscript next to the shipping service name.  # noqa: E501

        :return: The trademark_symbol of this ShippingOption.  # noqa: E501
        :rtype: str
        """
        return self._trademark_symbol

    @trademark_symbol.setter
    def trademark_symbol(self, trademark_symbol):
        """Sets the trademark_symbol of this ShippingOption.

        Any trademark symbol, such as &#8482; or &reg;, that needs to be shown in superscript next to the shipping service name.  # noqa: E501

        :param trademark_symbol: The trademark_symbol of this ShippingOption.  # noqa: E501
        :type: str
        """

        self._trademark_symbol = trademark_symbol

    @property
    def type(self):
        """Gets the type of this ShippingOption.  # noqa: E501

        The type of a shipping option, such as EXPEDITED, ONE_DAY, STANDARD, ECONOMY, PICKUP, etc.  # noqa: E501

        :return: The type of this ShippingOption.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShippingOption.

        The type of a shipping option, such as EXPEDITED, ONE_DAY, STANDARD, ECONOMY, PICKUP, etc.  # noqa: E501

        :param type: The type of this ShippingOption.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ShippingOption, dict):
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
        if not isinstance(other, ShippingOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
