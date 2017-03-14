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


class CatalogQueryItemsForTax(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, tax_ids=None):
        """
        CatalogQueryItemsForTax - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'tax_ids': 'list[str]'
        }

        self.attribute_map = {
            'tax_ids': 'tax_ids'
        }

        self._tax_ids = tax_ids

    @property
    def tax_ids(self):
        """
        Gets the tax_ids of this CatalogQueryItemsForTax.
        A set of [CatalogTax](#type-catalogtax) ids to be used to find associated [CatalogItem](#type-catalogitem)s.

        :return: The tax_ids of this CatalogQueryItemsForTax.
        :rtype: list[str]
        """
        return self._tax_ids

    @tax_ids.setter
    def tax_ids(self, tax_ids):
        """
        Sets the tax_ids of this CatalogQueryItemsForTax.
        A set of [CatalogTax](#type-catalogtax) ids to be used to find associated [CatalogItem](#type-catalogitem)s.

        :param tax_ids: The tax_ids of this CatalogQueryItemsForTax.
        :type: list[str]
        """

        self._tax_ids = tax_ids

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
