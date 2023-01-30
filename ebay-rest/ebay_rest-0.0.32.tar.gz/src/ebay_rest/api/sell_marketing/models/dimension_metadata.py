# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, refer to the <a href=\"/api-docs/sell/static/marketing/pl-landing.html\">Promoted Listings playbook</a>.</li><li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DimensionMetadata(object):
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
        'data_type': 'str',
        'dimension_key': 'str',
        'dimension_key_annotations': 'list[DimensionKeyAnnotation]'
    }

    attribute_map = {
        'data_type': 'dataType',
        'dimension_key': 'dimensionKey',
        'dimension_key_annotations': 'dimensionKeyAnnotations'
    }

    def __init__(self, data_type=None, dimension_key=None, dimension_key_annotations=None):  # noqa: E501
        """DimensionMetadata - a model defined in Swagger"""  # noqa: E501
        self._data_type = None
        self._dimension_key = None
        self._dimension_key_annotations = None
        self.discriminator = None
        if data_type is not None:
            self.data_type = data_type
        if dimension_key is not None:
            self.dimension_key = dimension_key
        if dimension_key_annotations is not None:
            self.dimension_key_annotations = dimension_key_annotations

    @property
    def data_type(self):
        """Gets the data_type of this DimensionMetadata.  # noqa: E501

        The data type of the dimension value used to create the report. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/plr:DataTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The data_type of this DimensionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this DimensionMetadata.

        The data type of the dimension value used to create the report. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/plr:DataTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param data_type: The data_type of this DimensionMetadata.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def dimension_key(self):
        """Gets the dimension_key of this DimensionMetadata.  # noqa: E501

        The name of the dimension used to create the report.  # noqa: E501

        :return: The dimension_key of this DimensionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._dimension_key

    @dimension_key.setter
    def dimension_key(self, dimension_key):
        """Sets the dimension_key of this DimensionMetadata.

        The name of the dimension used to create the report.  # noqa: E501

        :param dimension_key: The dimension_key of this DimensionMetadata.  # noqa: E501
        :type: str
        """

        self._dimension_key = dimension_key

    @property
    def dimension_key_annotations(self):
        """Gets the dimension_key_annotations of this DimensionMetadata.  # noqa: E501

        An list of annotation keys associated with the specified dimension of the report.  # noqa: E501

        :return: The dimension_key_annotations of this DimensionMetadata.  # noqa: E501
        :rtype: list[DimensionKeyAnnotation]
        """
        return self._dimension_key_annotations

    @dimension_key_annotations.setter
    def dimension_key_annotations(self, dimension_key_annotations):
        """Sets the dimension_key_annotations of this DimensionMetadata.

        An list of annotation keys associated with the specified dimension of the report.  # noqa: E501

        :param dimension_key_annotations: The dimension_key_annotations of this DimensionMetadata.  # noqa: E501
        :type: list[DimensionKeyAnnotation]
        """

        self._dimension_key_annotations = dimension_key_annotations

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
        if issubclass(DimensionMetadata, dict):
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
        if not isinstance(other, DimensionMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
