#
# Python SDK for Xooa
#
# Copyright 2018 Xooa
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License
# for the specific language governing permissions and limitations under the License.
#
# Author: Rahul Kamboj
#

class XooaPendingException(Exception):
    def __init__(self, result_id, result_url):

        # Call the base class constructor with the parameters it needs
        super(XooaPendingException, self).__init__({'result_url': result_url, 'result_id': result_id})

        # self.errors = errors


class XooaRequestTimeoutException(Exception):
    def __init__(self, result_id, result_url):

            super(XooaRequestTimeoutException, self).__init__({'result_url': result_url, 'result_id': result_id})

        # self.errors = errors


class XooaApiException(Exception):
    def __init__(self, message, errors):

        super(XooaApiException, self).__init__({'error_code': errors, 'error_message': message})

        # self.errors = errors


class InvalidParameterException(Exception):
    def __init__(self):

        super(InvalidParameterException, self).__init__({'error_message': 'Invalid Parameter'})

        # self.errors = errors
