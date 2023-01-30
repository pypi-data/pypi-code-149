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

class StandardsProfile(object):
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
        'cycle': 'Cycle',
        'default_program': 'bool',
        'evaluation_reason': 'str',
        'metrics': 'list[Metric]',
        'program': 'str',
        'standards_level': 'str'
    }

    attribute_map = {
        'cycle': 'cycle',
        'default_program': 'defaultProgram',
        'evaluation_reason': 'evaluationReason',
        'metrics': 'metrics',
        'program': 'program',
        'standards_level': 'standardsLevel'
    }

    def __init__(self, cycle=None, default_program=None, evaluation_reason=None, metrics=None, program=None, standards_level=None):  # noqa: E501
        """StandardsProfile - a model defined in Swagger"""  # noqa: E501
        self._cycle = None
        self._default_program = None
        self._evaluation_reason = None
        self._metrics = None
        self._program = None
        self._standards_level = None
        self.discriminator = None
        if cycle is not None:
            self.cycle = cycle
        if default_program is not None:
            self.default_program = default_program
        if evaluation_reason is not None:
            self.evaluation_reason = evaluation_reason
        if metrics is not None:
            self.metrics = metrics
        if program is not None:
            self.program = program
        if standards_level is not None:
            self.standards_level = standards_level

    @property
    def cycle(self):
        """Gets the cycle of this StandardsProfile.  # noqa: E501


        :return: The cycle of this StandardsProfile.  # noqa: E501
        :rtype: Cycle
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this StandardsProfile.


        :param cycle: The cycle of this StandardsProfile.  # noqa: E501
        :type: Cycle
        """

        self._cycle = cycle

    @property
    def default_program(self):
        """Gets the default_program of this StandardsProfile.  # noqa: E501

        If set to true, this flag indicates this is the default program for the seller. Except for sellers in China, a seller's default program is the marketplace where they registered with eBay. Seller's in China select their default program when they register.  # noqa: E501

        :return: The default_program of this StandardsProfile.  # noqa: E501
        :rtype: bool
        """
        return self._default_program

    @default_program.setter
    def default_program(self, default_program):
        """Sets the default_program of this StandardsProfile.

        If set to true, this flag indicates this is the default program for the seller. Except for sellers in China, a seller's default program is the marketplace where they registered with eBay. Seller's in China select their default program when they register.  # noqa: E501

        :param default_program: The default_program of this StandardsProfile.  # noqa: E501
        :type: bool
        """

        self._default_program = default_program

    @property
    def evaluation_reason(self):
        """Gets the evaluation_reason of this StandardsProfile.  # noqa: E501

        Specifies how the overall seller level was calculated. In the event of special circumstances (as determined by eBay), eBay may override the calculated seller level. In general, such overrides protect a seller's level. The usual value for both cycle types is &quot;Seller level generated by standards monthly evaluation cycle.&quot;  # noqa: E501

        :return: The evaluation_reason of this StandardsProfile.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_reason

    @evaluation_reason.setter
    def evaluation_reason(self, evaluation_reason):
        """Sets the evaluation_reason of this StandardsProfile.

        Specifies how the overall seller level was calculated. In the event of special circumstances (as determined by eBay), eBay may override the calculated seller level. In general, such overrides protect a seller's level. The usual value for both cycle types is &quot;Seller level generated by standards monthly evaluation cycle.&quot;  # noqa: E501

        :param evaluation_reason: The evaluation_reason of this StandardsProfile.  # noqa: E501
        :type: str
        """

        self._evaluation_reason = evaluation_reason

    @property
    def metrics(self):
        """Gets the metrics of this StandardsProfile.  # noqa: E501

        A list of the metrics upon which a seller's profile is evaluated. Each program's applicable metrics and requirements are listed at eBay Top Rated seller program standards.  # noqa: E501

        :return: The metrics of this StandardsProfile.  # noqa: E501
        :rtype: list[Metric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this StandardsProfile.

        A list of the metrics upon which a seller's profile is evaluated. Each program's applicable metrics and requirements are listed at eBay Top Rated seller program standards.  # noqa: E501

        :param metrics: The metrics of this StandardsProfile.  # noqa: E501
        :type: list[Metric]
        """

        self._metrics = metrics

    @property
    def program(self):
        """Gets the program of this StandardsProfile.  # noqa: E501

        Indicates the program used to generate the profile data. Values can be PROGRAM_DE, PROGRAM_UK, PROGRAM_US, or PROGRAM_GLOBAL. For implementation help, refer to <a href='https://developer.ebay.com/devzone/rest/api-ref/analytics/types/ProgramEnum.html'>eBay API documentation</a>  # noqa: E501

        :return: The program of this StandardsProfile.  # noqa: E501
        :rtype: str
        """
        return self._program

    @program.setter
    def program(self, program):
        """Sets the program of this StandardsProfile.

        Indicates the program used to generate the profile data. Values can be PROGRAM_DE, PROGRAM_UK, PROGRAM_US, or PROGRAM_GLOBAL. For implementation help, refer to <a href='https://developer.ebay.com/devzone/rest/api-ref/analytics/types/ProgramEnum.html'>eBay API documentation</a>  # noqa: E501

        :param program: The program of this StandardsProfile.  # noqa: E501
        :type: str
        """

        self._program = program

    @property
    def standards_level(self):
        """Gets the standards_level of this StandardsProfile.  # noqa: E501

        The overall standards level of the seller, one of TOP_RATED, ABOVE_STANDARD, or BELOW_STANDARD. For implementation help, refer to <a href='https://developer.ebay.com/devzone/rest/api-ref/analytics/types/StandardsLevelEnum.html'>eBay API documentation</a>  # noqa: E501

        :return: The standards_level of this StandardsProfile.  # noqa: E501
        :rtype: str
        """
        return self._standards_level

    @standards_level.setter
    def standards_level(self, standards_level):
        """Sets the standards_level of this StandardsProfile.

        The overall standards level of the seller, one of TOP_RATED, ABOVE_STANDARD, or BELOW_STANDARD. For implementation help, refer to <a href='https://developer.ebay.com/devzone/rest/api-ref/analytics/types/StandardsLevelEnum.html'>eBay API documentation</a>  # noqa: E501

        :param standards_level: The standards_level of this StandardsProfile.  # noqa: E501
        :type: str
        """

        self._standards_level = standards_level

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
        if issubclass(StandardsProfile, dict):
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
        if not isinstance(other, StandardsProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
