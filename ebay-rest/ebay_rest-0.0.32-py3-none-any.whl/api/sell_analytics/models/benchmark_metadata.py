# coding: utf-8

"""
     Seller Service Metrics API 

    The <i>Analytics API</i> provides data and information about a seller and their eBay business.  <br><br>The resources and methods in this API let sellers review information on their listing performance, metrics on their customer service performance, and details on their eBay seller performance rating.  <br><br>The three resources in the Analytics API provide the following data and information: <ul><li><b>Customer Service Metric</b> &ndash; Returns data on a seller's customer service performance as compared to other seller's in the same peer group.</li> <li><b>Traffic Report</b> &ndash; Returns data that shows how buyers are engaging with a seller's listings.</li> <li><b>Seller Standards Profile</b> &ndash; Returns data pertaining to a seller's performance rating.</li></ul> Sellers can use the data and information returned by the various Analytics API methods to determine where they can make improvements to increase sales and how they might improve their seller status as viewed by eBay buyers.  <br><br>For details on using this API, see <a href=\"/api-docs/sell/static/performance/analyzing-performance.html\" title=\"Selling Integration Guide\">Analyzing seller performance</a>.  # noqa: E501

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BenchmarkMetadata(object):
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
        'average': 'str'
    }

    attribute_map = {
        'average': 'average'
    }

    def __init__(self, average=None):  # noqa: E501
        """BenchmarkMetadata - a model defined in Swagger"""  # noqa: E501
        self._average = None
        self.discriminator = None
        if average is not None:
            self.average = average

    @property
    def average(self):
        """Gets the average of this BenchmarkMetadata.  # noqa: E501

        This field returns the average value for the group, as defined by the specified basis. When the benchmark basis is set to PEER_BENCHMARK, the value returned in this field is the benchmark value to which the seller's metric value is compared to determine the seller's rating for the customer service metric.  # noqa: E501

        :return: The average of this BenchmarkMetadata.  # noqa: E501
        :rtype: str
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this BenchmarkMetadata.

        This field returns the average value for the group, as defined by the specified basis. When the benchmark basis is set to PEER_BENCHMARK, the value returned in this field is the benchmark value to which the seller's metric value is compared to determine the seller's rating for the customer service metric.  # noqa: E501

        :param average: The average of this BenchmarkMetadata.  # noqa: E501
        :type: str
        """

        self._average = average

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
        if issubclass(BenchmarkMetadata, dict):
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
        if not isinstance(other, BenchmarkMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
