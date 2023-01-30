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

class CartItem(object):
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
        'cart_item_id': 'str',
        'cart_item_subtotal': 'Amount',
        'image': 'Image',
        'item_id': 'str',
        'item_web_url': 'str',
        'price': 'Price',
        'quantity': 'int',
        'title': 'str'
    }

    attribute_map = {
        'cart_item_id': 'cartItemId',
        'cart_item_subtotal': 'cartItemSubtotal',
        'image': 'image',
        'item_id': 'itemId',
        'item_web_url': 'itemWebUrl',
        'price': 'price',
        'quantity': 'quantity',
        'title': 'title'
    }

    def __init__(self, cart_item_id=None, cart_item_subtotal=None, image=None, item_id=None, item_web_url=None, price=None, quantity=None, title=None):  # noqa: E501
        """CartItem - a model defined in Swagger"""  # noqa: E501
        self._cart_item_id = None
        self._cart_item_subtotal = None
        self._image = None
        self._item_id = None
        self._item_web_url = None
        self._price = None
        self._quantity = None
        self._title = None
        self.discriminator = None
        if cart_item_id is not None:
            self.cart_item_id = cart_item_id
        if cart_item_subtotal is not None:
            self.cart_item_subtotal = cart_item_subtotal
        if image is not None:
            self.image = image
        if item_id is not None:
            self.item_id = item_id
        if item_web_url is not None:
            self.item_web_url = item_web_url
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity
        if title is not None:
            self.title = title

    @property
    def cart_item_id(self):
        """Gets the cart_item_id of this CartItem.  # noqa: E501

        The identifier for the item being added to the cart. This is generated when the item is added to the cart.  # noqa: E501

        :return: The cart_item_id of this CartItem.  # noqa: E501
        :rtype: str
        """
        return self._cart_item_id

    @cart_item_id.setter
    def cart_item_id(self, cart_item_id):
        """Sets the cart_item_id of this CartItem.

        The identifier for the item being added to the cart. This is generated when the item is added to the cart.  # noqa: E501

        :param cart_item_id: The cart_item_id of this CartItem.  # noqa: E501
        :type: str
        """

        self._cart_item_id = cart_item_id

    @property
    def cart_item_subtotal(self):
        """Gets the cart_item_subtotal of this CartItem.  # noqa: E501


        :return: The cart_item_subtotal of this CartItem.  # noqa: E501
        :rtype: Amount
        """
        return self._cart_item_subtotal

    @cart_item_subtotal.setter
    def cart_item_subtotal(self, cart_item_subtotal):
        """Sets the cart_item_subtotal of this CartItem.


        :param cart_item_subtotal: The cart_item_subtotal of this CartItem.  # noqa: E501
        :type: Amount
        """

        self._cart_item_subtotal = cart_item_subtotal

    @property
    def image(self):
        """Gets the image of this CartItem.  # noqa: E501


        :return: The image of this CartItem.  # noqa: E501
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this CartItem.


        :param image: The image of this CartItem.  # noqa: E501
        :type: Image
        """

        self._image = image

    @property
    def item_id(self):
        """Gets the item_id of this CartItem.  # noqa: E501

        The RESTful identifier of the item. This identifier is generated when the item was listed. <br /><br /> <b>RESTful Item ID Format: </b><code>v1</code>|<code><i>#</i></code>|<code><i>#</i></code> <br /><b> For example: </b><br /> <code>v1|2**********2|0</code> <br /><code>v1|1**********2|4**********2</code>  # noqa: E501

        :return: The item_id of this CartItem.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this CartItem.

        The RESTful identifier of the item. This identifier is generated when the item was listed. <br /><br /> <b>RESTful Item ID Format: </b><code>v1</code>|<code><i>#</i></code>|<code><i>#</i></code> <br /><b> For example: </b><br /> <code>v1|2**********2|0</code> <br /><code>v1|1**********2|4**********2</code>  # noqa: E501

        :param item_id: The item_id of this CartItem.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def item_web_url(self):
        """Gets the item_web_url of this CartItem.  # noqa: E501

        The URL of the eBay view item page for the item.  # noqa: E501

        :return: The item_web_url of this CartItem.  # noqa: E501
        :rtype: str
        """
        return self._item_web_url

    @item_web_url.setter
    def item_web_url(self, item_web_url):
        """Sets the item_web_url of this CartItem.

        The URL of the eBay view item page for the item.  # noqa: E501

        :param item_web_url: The item_web_url of this CartItem.  # noqa: E501
        :type: str
        """

        self._item_web_url = item_web_url

    @property
    def price(self):
        """Gets the price of this CartItem.  # noqa: E501


        :return: The price of this CartItem.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this CartItem.


        :param price: The price of this CartItem.  # noqa: E501
        :type: Price
        """

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this CartItem.  # noqa: E501

        The number of this item the buyer wants to purchase.  # noqa: E501

        :return: The quantity of this CartItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CartItem.

        The number of this item the buyer wants to purchase.  # noqa: E501

        :param quantity: The quantity of this CartItem.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def title(self):
        """Gets the title of this CartItem.  # noqa: E501

        The title of the item. This can be written by the seller or come from the eBay product catalog.  # noqa: E501

        :return: The title of this CartItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CartItem.

        The title of the item. This can be written by the seller or come from the eBay product catalog.  # noqa: E501

        :param title: The title of this CartItem.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(CartItem, dict):
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
        if not isinstance(other, CartItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
