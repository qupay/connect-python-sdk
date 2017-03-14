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


class CatalogItemModifierListInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, modifier_list_id=None, visibility=None, modifier_overrides=None, min_selected_modifiers=None, max_selected_modifiers=None, enabled=None):
        """
        CatalogItemModifierListInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'modifier_list_id': 'str',
            'visibility': 'str',
            'modifier_overrides': 'list[CatalogModifierOverride]',
            'min_selected_modifiers': 'int',
            'max_selected_modifiers': 'int',
            'enabled': 'bool'
        }

        self.attribute_map = {
            'modifier_list_id': 'modifier_list_id',
            'visibility': 'visibility',
            'modifier_overrides': 'modifier_overrides',
            'min_selected_modifiers': 'min_selected_modifiers',
            'max_selected_modifiers': 'max_selected_modifiers',
            'enabled': 'enabled'
        }

        self._modifier_list_id = modifier_list_id
        self._visibility = visibility
        self._modifier_overrides = modifier_overrides
        self._min_selected_modifiers = min_selected_modifiers
        self._max_selected_modifiers = max_selected_modifiers
        self._enabled = enabled

    @property
    def modifier_list_id(self):
        """
        Gets the modifier_list_id of this CatalogItemModifierListInfo.
        The [CatalogModifierList](#type-catalogmodifierlist) controlled by this CatalogItemModifierListInfo.

        :return: The modifier_list_id of this CatalogItemModifierListInfo.
        :rtype: str
        """
        return self._modifier_list_id

    @modifier_list_id.setter
    def modifier_list_id(self, modifier_list_id):
        """
        Sets the modifier_list_id of this CatalogItemModifierListInfo.
        The [CatalogModifierList](#type-catalogmodifierlist) controlled by this CatalogItemModifierListInfo.

        :param modifier_list_id: The modifier_list_id of this CatalogItemModifierListInfo.
        :type: str
        """

        if not modifier_list_id:
            raise ValueError("Invalid value for `modifier_list_id`, must not be `None`")
        if len(modifier_list_id) < 1:
            raise ValueError("Invalid value for `modifier_list_id`, length must be greater than or equal to `1`")

        self._modifier_list_id = modifier_list_id

    @property
    def visibility(self):
        """
        Gets the visibility of this CatalogItemModifierListInfo.
        

        :return: The visibility of this CatalogItemModifierListInfo.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """
        Sets the visibility of this CatalogItemModifierListInfo.
        

        :param visibility: The visibility of this CatalogItemModifierListInfo.
        :type: str
        """

        self._visibility = visibility

    @property
    def modifier_overrides(self):
        """
        Gets the modifier_overrides of this CatalogItemModifierListInfo.
        A set of [CatalogModifierOverride](#type-catalogmodifieroverride) objects that override whether a given modifier is enabled by default.

        :return: The modifier_overrides of this CatalogItemModifierListInfo.
        :rtype: list[CatalogModifierOverride]
        """
        return self._modifier_overrides

    @modifier_overrides.setter
    def modifier_overrides(self, modifier_overrides):
        """
        Sets the modifier_overrides of this CatalogItemModifierListInfo.
        A set of [CatalogModifierOverride](#type-catalogmodifieroverride) objects that override whether a given modifier is enabled by default.

        :param modifier_overrides: The modifier_overrides of this CatalogItemModifierListInfo.
        :type: list[CatalogModifierOverride]
        """

        self._modifier_overrides = modifier_overrides

    @property
    def min_selected_modifiers(self):
        """
        Gets the min_selected_modifiers of this CatalogItemModifierListInfo.
        If >= 0, the smallest number of modifiers that must be selected from this [CatalogModifierList](#type-catalogmodifierlist).

        :return: The min_selected_modifiers of this CatalogItemModifierListInfo.
        :rtype: int
        """
        return self._min_selected_modifiers

    @min_selected_modifiers.setter
    def min_selected_modifiers(self, min_selected_modifiers):
        """
        Sets the min_selected_modifiers of this CatalogItemModifierListInfo.
        If >= 0, the smallest number of modifiers that must be selected from this [CatalogModifierList](#type-catalogmodifierlist).

        :param min_selected_modifiers: The min_selected_modifiers of this CatalogItemModifierListInfo.
        :type: int
        """

        self._min_selected_modifiers = min_selected_modifiers

    @property
    def max_selected_modifiers(self):
        """
        Gets the max_selected_modifiers of this CatalogItemModifierListInfo.
        If >= 0, the largest number of modifiers that can be selected from this [CatalogModifierList](#type-catalogmodifierlist).

        :return: The max_selected_modifiers of this CatalogItemModifierListInfo.
        :rtype: int
        """
        return self._max_selected_modifiers

    @max_selected_modifiers.setter
    def max_selected_modifiers(self, max_selected_modifiers):
        """
        Sets the max_selected_modifiers of this CatalogItemModifierListInfo.
        If >= 0, the largest number of modifiers that can be selected from this [CatalogModifierList](#type-catalogmodifierlist).

        :param max_selected_modifiers: The max_selected_modifiers of this CatalogItemModifierListInfo.
        :type: int
        """

        self._max_selected_modifiers = max_selected_modifiers

    @property
    def enabled(self):
        """
        Gets the enabled of this CatalogItemModifierListInfo.
        

        :return: The enabled of this CatalogItemModifierListInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this CatalogItemModifierListInfo.
        

        :param enabled: The enabled of this CatalogItemModifierListInfo.
        :type: bool
        """

        self._enabled = enabled

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
