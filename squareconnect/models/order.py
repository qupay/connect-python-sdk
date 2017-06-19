# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class Order(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, location_id=None, reference_id=None, line_items=None, total_money=None, total_tax_money=None, total_discount_money=None):
        """
        Order - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'location_id': 'str',
            'reference_id': 'str',
            'line_items': 'list[OrderLineItem]',
            'total_money': 'Money',
            'total_tax_money': 'Money',
            'total_discount_money': 'Money'
        }

        self.attribute_map = {
            'id': 'id',
            'location_id': 'location_id',
            'reference_id': 'reference_id',
            'line_items': 'line_items',
            'total_money': 'total_money',
            'total_tax_money': 'total_tax_money',
            'total_discount_money': 'total_discount_money'
        }

        self._id = id
        self._location_id = location_id
        self._reference_id = reference_id
        self._line_items = line_items
        self._total_money = total_money
        self._total_tax_money = total_tax_money
        self._total_discount_money = total_discount_money

    @property
    def id(self):
        """
        Gets the id of this Order.
        The order's unique ID.  This value is not present if the order was not created with the [CreateOrder](#endpoint-createorder) endpoint.

        :return: The id of this Order.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Order.
        The order's unique ID.  This value is not present if the order was not created with the [CreateOrder](#endpoint-createorder) endpoint.

        :param id: The id of this Order.
        :type: str
        """

        self._id = id

    @property
    def location_id(self):
        """
        Gets the location_id of this Order.
        The ID of the merchant location this order is associated with.

        :return: The location_id of this Order.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this Order.
        The ID of the merchant location this order is associated with.

        :param location_id: The location_id of this Order.
        :type: str
        """

        self._location_id = location_id

    @property
    def reference_id(self):
        """
        Gets the reference_id of this Order.
        A client specified identifier to associate an entity in another system with this order.

        :return: The reference_id of this Order.
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """
        Sets the reference_id of this Order.
        A client specified identifier to associate an entity in another system with this order.

        :param reference_id: The reference_id of this Order.
        :type: str
        """

        self._reference_id = reference_id

    @property
    def line_items(self):
        """
        Gets the line_items of this Order.
        The line items included in the order. Every order has at least one line item.

        :return: The line_items of this Order.
        :rtype: list[OrderLineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """
        Sets the line_items of this Order.
        The line items included in the order. Every order has at least one line item.

        :param line_items: The line_items of this Order.
        :type: list[OrderLineItem]
        """

        self._line_items = line_items

    @property
    def total_money(self):
        """
        Gets the total_money of this Order.
        The total amount of money to collect for the order.

        :return: The total_money of this Order.
        :rtype: Money
        """
        return self._total_money

    @total_money.setter
    def total_money(self, total_money):
        """
        Sets the total_money of this Order.
        The total amount of money to collect for the order.

        :param total_money: The total_money of this Order.
        :type: Money
        """

        self._total_money = total_money

    @property
    def total_tax_money(self):
        """
        Gets the total_tax_money of this Order.
        The total tax amount of money to collect for the order.

        :return: The total_tax_money of this Order.
        :rtype: Money
        """
        return self._total_tax_money

    @total_tax_money.setter
    def total_tax_money(self, total_tax_money):
        """
        Sets the total_tax_money of this Order.
        The total tax amount of money to collect for the order.

        :param total_tax_money: The total_tax_money of this Order.
        :type: Money
        """

        self._total_tax_money = total_tax_money

    @property
    def total_discount_money(self):
        """
        Gets the total_discount_money of this Order.
        The total discount amount of money to collect for the order.

        :return: The total_discount_money of this Order.
        :rtype: Money
        """
        return self._total_discount_money

    @total_discount_money.setter
    def total_discount_money(self, total_discount_money):
        """
        Sets the total_discount_money of this Order.
        The total discount amount of money to collect for the order.

        :param total_discount_money: The total_discount_money of this Order.
        :type: Money
        """

        self._total_discount_money = total_discount_money

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
