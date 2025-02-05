# Copyright 2022 The KServe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    KServe

    Python SDK for KServe  # noqa: E501

    The version of the OpenAPI document: v0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kserve.configuration import Configuration


class V1beta1FailureInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'exit_code': 'int',
        'location': 'str',
        'message': 'str',
        'model_revision_name': 'str',
        'reason': 'str',
        'time': 'V1Time'
    }

    attribute_map = {
        'exit_code': 'exitCode',
        'location': 'location',
        'message': 'message',
        'model_revision_name': 'modelRevisionName',
        'reason': 'reason',
        'time': 'time'
    }

    def __init__(self, exit_code=None, location=None, message=None, model_revision_name=None, reason=None, time=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1FailureInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exit_code = None
        self._location = None
        self._message = None
        self._model_revision_name = None
        self._reason = None
        self._time = None
        self.discriminator = None

        if exit_code is not None:
            self.exit_code = exit_code
        if location is not None:
            self.location = location
        if message is not None:
            self.message = message
        if model_revision_name is not None:
            self.model_revision_name = model_revision_name
        if reason is not None:
            self.reason = reason
        if time is not None:
            self.time = time

    @property
    def exit_code(self):
        """Gets the exit_code of this V1beta1FailureInfo.  # noqa: E501

        Exit status from the last termination of the container  # noqa: E501

        :return: The exit_code of this V1beta1FailureInfo.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this V1beta1FailureInfo.

        Exit status from the last termination of the container  # noqa: E501

        :param exit_code: The exit_code of this V1beta1FailureInfo.  # noqa: E501
        :type: int
        """

        self._exit_code = exit_code

    @property
    def location(self):
        """Gets the location of this V1beta1FailureInfo.  # noqa: E501

        Name of component to which the failure relates (usually Pod name)  # noqa: E501

        :return: The location of this V1beta1FailureInfo.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this V1beta1FailureInfo.

        Name of component to which the failure relates (usually Pod name)  # noqa: E501

        :param location: The location of this V1beta1FailureInfo.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def message(self):
        """Gets the message of this V1beta1FailureInfo.  # noqa: E501

        Detailed error message  # noqa: E501

        :return: The message of this V1beta1FailureInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1beta1FailureInfo.

        Detailed error message  # noqa: E501

        :param message: The message of this V1beta1FailureInfo.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def model_revision_name(self):
        """Gets the model_revision_name of this V1beta1FailureInfo.  # noqa: E501

        Internal Revision/ID of model, tied to specific Spec contents  # noqa: E501

        :return: The model_revision_name of this V1beta1FailureInfo.  # noqa: E501
        :rtype: str
        """
        return self._model_revision_name

    @model_revision_name.setter
    def model_revision_name(self, model_revision_name):
        """Sets the model_revision_name of this V1beta1FailureInfo.

        Internal Revision/ID of model, tied to specific Spec contents  # noqa: E501

        :param model_revision_name: The model_revision_name of this V1beta1FailureInfo.  # noqa: E501
        :type: str
        """

        self._model_revision_name = model_revision_name

    @property
    def reason(self):
        """Gets the reason of this V1beta1FailureInfo.  # noqa: E501

        High level class of failure  # noqa: E501

        :return: The reason of this V1beta1FailureInfo.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1beta1FailureInfo.

        High level class of failure  # noqa: E501

        :param reason: The reason of this V1beta1FailureInfo.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def time(self):
        """Gets the time of this V1beta1FailureInfo.  # noqa: E501


        :return: The time of this V1beta1FailureInfo.  # noqa: E501
        :rtype: V1Time
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this V1beta1FailureInfo.


        :param time: The time of this V1beta1FailureInfo.  # noqa: E501
        :type: V1Time
        """

        self._time = time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1FailureInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1FailureInfo):
            return True

        return self.to_dict() != other.to_dict()
