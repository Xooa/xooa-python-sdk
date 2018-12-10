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
# coding: utf-8
from __future__ import absolute_import

# python 2 and python 3 compatibility library
import six
import ast
import requests
import json
from .xooa_exceptions import XooaApiException, XooaRequestTimeoutException


class InvokeApi(object):

    def invoke(self, client_obj, fcn, **kwargs):
        """
        The Invoke API End Point is used for submitting transaction for processing by the blockchain Smart Contract app.
         The end point must call a function already defined in your Smart Contract app which will process the Invoke request.
         The function name is part of the endpoint URL, or can be entered as the fcn parameter when testing using the Sandbox.
         For example, if testing the sample get-set Smart Contract app, use ‘set’ (without quotes)  as the value for fcn.
         The function arguments (number of arguments and type) is determined by the Smart Contract.
         The Smart Contract is also responsible for arguments validation and exception management.
         The payload object of Invoke Transaction Response in case of Final Response is determined by the Smart Contract app.
         A success response may be either 200 or 202.

        :param client_obj: Includes Headers and URL to make request
        :param str fcn: function name
        :param kwargs:
        :param str async: Call this request asynchronously without waiting for response
        :param str timeout: Request timeout in millisecond
        :return:
        """
        logger = client_obj.xooa_logger
        try:
            req_params = client_obj.req_params


            logger.info('Invoke API has been called')

            all_params = ['fcn', 'asyncKey', 'timeout', 'data']

            params = locals()
            for key, val in six.iteritems(params['kwargs']):
                if key not in all_params:
                    logger.error("Got an unexpected keyword argument '%s'"
                        " to method invoke" % key)

                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method invoke" % key
                    )
                params[key] = val
            del params['kwargs']
            # verify the required parameter 'fcn' is set
            if 'fcn' not in params or params['fcn'] is None:

                logger.error("Missing the required parameter `fcn` when calling `invoke`")

                raise ValueError("Missing the required parameter `fcn` when calling `invoke`")

            query_params = {}
            if 'async' in params:
                query_params['async'] = params['asyncKey']
            else:
                query_params['async'] = 'false'
            if 'timeout' in params:
                query_params['timeout'] = params['timeout']

            body_params = params['data']

            url_suffix = 'invoke/' + fcn

            url = req_params['base_url'] + url_suffix
            headers = req_params['headers']

            data = json.dumps(body_params)

            logger.info("Sending request...")

            request = requests.post(url, params=query_params, headers=headers, data=data)

            if request.status_code >= 400:
                raise XooaApiException(request.text, request.status_code)

            response_object = json.loads(request.text)

            if query_params['async'] == 'true':
                if request.status_code == 200:
                    return response_object
                else:
                    request.raise_for_status()

            else:
                if request.status_code == 200:
                    return response_object

                elif request.status_code == 202:
                    result_id = response_object['resultId']
                    result_url = response_object['resultURL']
                    raise XooaRequestTimeoutException(result_id, result_url)
                else:
                    request.raise_for_status()
        except Exception:
            logger.exception('Got exception on main handler')
            raise
