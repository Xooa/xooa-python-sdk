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
import requests
import json
from .xooa_exceptions import XooaApiException, XooaRequestTimeoutException


class InvokeApi(object):
    """ Invoke API Class to create requests to Invoke API. """

    def invoke(self, xooa_client, fcn, args, timeout, **kwargs):
        """ Invoke Submit block chain transactions in async mode.

         The Invoke API End Point is used for submitting transaction for processing
         by the block chain Smart Contract app. The end point must call a function
         already defined in your Smart Contract app which will process the Invoke request.
         The function name is part of the endpoint URL, or can be entered as the fcn parameter
         when testing using the Sandbox.
         For example, if testing the sample get-set Smart Contract app, use 'set'(without quotes)
         as the value for fcn. The function arguments (number of arguments and type)
         is determined by the Smart Contract. The Smart Contract is also responsible for
         arguments validation and exception management.
         The payload object of Invoke Transaction Response in case of Final Response
         is determined by the Smart Contract app. A success response may be either 200 or 202.

        :param xooa_client: Includes Headers and URL to make request
        :param str fcn: function name to be invoked
        :param args: Arguments to pass to the smart contract
        :param timeout:
        :param kwargs:
        :return:
        """

        logger = xooa_client.xooa_logger

        try:
            req_params = xooa_client.req_params

            logger.info('Invoke API has been called')

            params = locals()

            for key, val in six.iteritems(params['kwargs']):

                if key == 'asyncKey':
                    params[key] = val

            del params['kwargs']

            # verify the required parameter 'fcn' is set
            if fcn is None:
                logger.error("Missing the required parameter `fcn` when calling `invoke`")
                raise ValueError("Missing the required parameter `fcn` when calling `invoke`")

            query_params = {}

            if 'asyncKey' in params:
                query_params['async'] = params['asyncKey']
            else:
                query_params['async'] = 'false'

            if timeout is not None:
                query_params['timeout'] = timeout

            url_suffix = '/invoke/' + fcn

            url = req_params['base_url'] + url_suffix

            headers = req_params['headers']

            data = json.dumps(args)

            logger.info("Sending request to invoke...")

            response = requests.post(url, params=query_params, headers=headers, data=data)

            response_object = json.loads(response.text)

            if query_params['async'] == 'true':

                if response.status_code == 202:
                    return response_object

                else:
                    raise XooaApiException(response.status_code, response_object)

            else:
                if response.status_code == 200:
                    return response_object

                elif response.status_code == 202:
                    raise XooaRequestTimeoutException(response_object['resultId'], response_object['resultURL'])

                else:
                    raise XooaApiException(response.status_code, response_object)

        except XooaApiException:
            raise

        except XooaRequestTimeoutException:
            raise

        except Exception:
            logger.exception('Got exception on main handler')
            raise XooaApiException('0', 'Exception while Invoking Xooa.')
