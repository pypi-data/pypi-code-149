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

class Refund(object):
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
        'refund_id': 'str',
        'refund_status': 'str'
    }

    attribute_map = {
        'refund_id': 'refundId',
        'refund_status': 'refundStatus'
    }

    def __init__(self, refund_id=None, refund_status=None):  # noqa: E501
        """Refund - a model defined in Swagger"""  # noqa: E501
        self._refund_id = None
        self._refund_status = None
        self.discriminator = None
        if refund_id is not None:
            self.refund_id = refund_id
        if refund_status is not None:
            self.refund_status = refund_status

    @property
    def refund_id(self):
        """Gets the refund_id of this Refund.  # noqa: E501

        The unique identifier of the order refund. This value is returned unless the refund operation fails (<b>refundStatus</b> value shows <code>FAILED</code>). This identifier can be used to track the status of the refund through a <b>getOrder</b> or <b>getOrders</b> call. For order-level refunds, check the <b>paymentSummary.refunds.refundId</b> field in the <b>getOrder</b>/<b>getOrders</b> response, and for line item level refunds, check the <b>lineItems.refunds.refundId</b> field(s) in the <b>getOrder</b>/<b>getOrders</b> response.  # noqa: E501

        :return: The refund_id of this Refund.  # noqa: E501
        :rtype: str
        """
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        """Sets the refund_id of this Refund.

        The unique identifier of the order refund. This value is returned unless the refund operation fails (<b>refundStatus</b> value shows <code>FAILED</code>). This identifier can be used to track the status of the refund through a <b>getOrder</b> or <b>getOrders</b> call. For order-level refunds, check the <b>paymentSummary.refunds.refundId</b> field in the <b>getOrder</b>/<b>getOrders</b> response, and for line item level refunds, check the <b>lineItems.refunds.refundId</b> field(s) in the <b>getOrder</b>/<b>getOrders</b> response.  # noqa: E501

        :param refund_id: The refund_id of this Refund.  # noqa: E501
        :type: str
        """

        self._refund_id = refund_id

    @property
    def refund_status(self):
        """Gets the refund_status of this Refund.  # noqa: E501

        The value returned in this field indicates the success or failure of the refund operation. A successful <b>issueRefund</b> operation should result in a value of <code>PENDING</code>. A failed <b>issueRefund</b> operation should result in a value of <code>FAILED</code>, and an HTTP status code and/or and API error code may also get returned to possibly indicate the issue.<br/><br/>The refunds issued through this method are processed asynchronously, so the refund will not show as 'Refunded' right away. A seller will have to make a subsequent <a href=\"https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrder\" target=\"_blank\">getOrder</a> call to check the status of the refund.  The status of an order refund can be found in the <a href=\"https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrder#response.paymentSummary.refunds.refundStatus\" target=\"_blank\">paymentSummary.refunds.refundStatus</a> field of the <a href=\"https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrder\" target=\"_blank\">getOrder</a> response. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:RefundStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The refund_status of this Refund.  # noqa: E501
        :rtype: str
        """
        return self._refund_status

    @refund_status.setter
    def refund_status(self, refund_status):
        """Sets the refund_status of this Refund.

        The value returned in this field indicates the success or failure of the refund operation. A successful <b>issueRefund</b> operation should result in a value of <code>PENDING</code>. A failed <b>issueRefund</b> operation should result in a value of <code>FAILED</code>, and an HTTP status code and/or and API error code may also get returned to possibly indicate the issue.<br/><br/>The refunds issued through this method are processed asynchronously, so the refund will not show as 'Refunded' right away. A seller will have to make a subsequent <a href=\"https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrder\" target=\"_blank\">getOrder</a> call to check the status of the refund.  The status of an order refund can be found in the <a href=\"https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrder#response.paymentSummary.refunds.refundStatus\" target=\"_blank\">paymentSummary.refunds.refundStatus</a> field of the <a href=\"https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrder\" target=\"_blank\">getOrder</a> response. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:RefundStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param refund_status: The refund_status of this Refund.  # noqa: E501
        :type: str
        """

        self._refund_status = refund_status

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
        if issubclass(Refund, dict):
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
        if not isinstance(other, Refund):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
