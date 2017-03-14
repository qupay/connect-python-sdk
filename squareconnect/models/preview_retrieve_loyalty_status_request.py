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


class PreviewRetrieveLoyaltyStatusRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, phone_number=None):
        """
        PreviewRetrieveLoyaltyStatusRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'phone_number': 'str'
        }

        self.attribute_map = {
            'phone_number': 'phone_number'
        }

        self._phone_number = phone_number

    @property
    def phone_number(self):
        """
        Gets the phone_number of this PreviewRetrieveLoyaltyStatusRequest.
        The customer phone number that identifies the loyalty account.

        :return: The phone_number of this PreviewRetrieveLoyaltyStatusRequest.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this PreviewRetrieveLoyaltyStatusRequest.
        The customer phone number that identifies the loyalty account.

        :param phone_number: The phone_number of this PreviewRetrieveLoyaltyStatusRequest.
        :type: str
        """

        if not phone_number:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")
        if len(phone_number) > 20:
            raise ValueError("Invalid value for `phone_number`, length must be less than `20`")
        if len(phone_number) < 1:
            raise ValueError("Invalid value for `phone_number`, length must be greater than or equal to `1`")

        self._phone_number = phone_number

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
