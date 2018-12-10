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
import json
from .xooa_exceptions import XooaApiException, XooaRequestTimeoutException
import requests


class BlockchainApi(object):

    def block_data(self, client_obj, block_number, **kwargs):
        """
        Get specific block information such as hash, # of transactions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param client_obj: Includes Headers and URL to make request
        :param int block_number:  Block number to fetch data (required)
        :param kwargs:
        :param str async: Call this request asynchronously without waiting for response
        :param str timeout: Request timeout in millisecond
        :return:
        """
        logger = client_obj.xooa_logger
        try:
            req_params = client_obj.req_params


            logger.info('Blockchain Data API has been called')

            all_params = ['block_number', 'asyncKey', 'timeout']

            params = locals()
            for key, val in six.iteritems(params['kwargs']):
                if key not in all_params:

                    logger.error("Got an unexpected keyword argument '%s'"
                                 " to method invoke" % key)
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method block_data" % key
                    )
                params[key] = val
            del params['kwargs']
            # verify the required parameter 'block_number' is set
            if ('block_number' not in params or
                    params['block_number'] is None):
                logger.error("Missing the required parameter `block_number` when calling `block_data`")

                raise ValueError("Missing the required parameter `block_number` when calling `block_data`")

            query_params = {}
            if 'async' in params:
                query_params['async'] = params['asyncKey']
            else:
                query_params['async'] = 'false'
            if 'timeout' in params:
                query_params['timeout'] = params['timeout']

            url_suffix = '/block/' + str(block_number)

            url = req_params['base_url'] + url_suffix
            headers = req_params['headers']

            logger.info("Sending request...")

            request = requests.get(url, params=query_params, headers=headers)
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

    def block_height(self, client_obj, **kwargs):
        """
        Get block height
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param client_obj: Includes Headers and URL to make request
        :param kwargs:
        :param str async: Call this request asynchronously without waiting for response
        :param str timeout: Request timeout in millisecond
        :return:
        """
        logger = client_obj.xooa_logger
        try:
            req_params = client_obj.req_params

            logger.debug('Block Height API has been called')

            all_params = ['asyncKey', 'timeout']

            params = locals()
            for key, val in six.iteritems(params['kwargs']):
                if key not in all_params:
                    logger.error("Got an unexpected keyword argument '%s'"
                                 " to method block_height" % key)
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method block_height" % key
                    )
                params[key] = val
            del params['kwargs']

            query_params = {}
            if 'async' in params:
                query_params['async'] = params['asyncKey']
            else:
                query_params['async'] = 'false'
            if 'timeout' in params:
                query_params['timeout'] = params['timeout']

            url_suffix = 'block/current'

            url = req_params['base_url'] + url_suffix
            headers = req_params['headers']

            logger.debug("Requesting blockchain height...")

            request = requests.get(url, params=query_params, headers=headers)
            if request.status_code >= 400:
                logger.error("Error: " + request.text)
                raise XooaApiException(request.text, request.status_code)

            response_object = json.loads(request.text)

            if query_params['async'] == 'true':
                if request.status_code == 200:
                    logger.debug("Response: " + response_object)
                    return response_object
                else:
                    request.raise_for_status()

            else:
                if request.status_code == 200:
                    logger.debug("Response: " + json.dumps(response_object))
                    return response_object
                elif request.status_code == 202:
                    logger.debug("Response: " + json.dumps(response_object))
                    result_id = response_object['resultId']
                    result_url = response_object['resultURL']
                    raise XooaRequestTimeoutException(result_id, result_url)
                else:
                    request.raise_for_status()

        except Exception:
            logger.exception('Got exception on main handler')
            raise
