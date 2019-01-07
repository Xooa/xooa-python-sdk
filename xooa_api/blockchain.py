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
    """ Block chain API class to create requests to block chain API."""

    def block_data(self, xooa_client, block_number, timeout, **kwargs):
        """ Call the BlockByNumber api

        :param xooa_client: Includes Headers and URL to make request
        :param int block_number:  Block number to fetch data (required)
        :param timeout:
        :param kwargs: Query Arguments for the api including async and timeout
        :return:
        """

        logger = xooa_client.xooa_logger

        try:
            req_params = xooa_client.req_params

            logger.info('Calling Block Chain API for Block By Number')

            params = locals()

            for key, val in six.iteritems(params['kwargs']):

                if key == 'asyncKey':
                    params[key] = val

            del params['kwargs']

            # verify the required parameter 'block_number' is set
            if block_number is None:
                logger.error("Missing the required parameter `block_number` when calling `block_data`")
                raise ValueError("Missing the required parameter `block_number` when calling `block_data`")

            query_params = {}
            if 'asyncKey' in params:
                query_params['async'] = params['asyncKey']
            else:
                query_params['async'] = 'false'

            if timeout is not None:
                query_params['timeout'] = timeout

            url_suffix = '/block/' + str(block_number)

            url = req_params['base_url'] + url_suffix

            headers = req_params['headers']

            logger.info("Sending request to get Block By Number...")

            response = requests.get(url, params=query_params, headers=headers)

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
            raise XooaApiException("0", "Exception in GetBlockByNumber")

    def block_height(self, xooa_client, timeout, **kwargs):
        """ Call the CurrentBlock api

        :param xooa_client: Includes Headers and URL to make request
        :param timeout:
        :param kwargs: Query Arguments for the api including async and timeout
        :return:
        """

        logger = xooa_client.xooa_logger

        try:
            req_params = xooa_client.req_params

            logger.info('Calling Block Chain API for Block Height.')

            params = locals()

            for key, val in six.iteritems(params['kwargs']):

                if key == "asyncKey":
                    params[key] = val

            del params['kwargs']

            query_params = {}

            if 'asyncKey' in params:
                query_params['async'] = params['asyncKey']
            else:
                query_params['async'] = 'false'

            if timeout is not None:
                query_params['timeout'] = timeout

            url_suffix = '/block/current'

            url = req_params['base_url'] + url_suffix

            headers = req_params['headers']

            logger.info("Requesting blockchain height...")

            response = requests.get(url, params=query_params, headers=headers)

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
            raise XooaApiException("0", "Exception in GetBlockHeight")

    def get_transaction_by_transaction_id(self, xooa_client, transaction_id, timeout, **kwargs):
        """ Call the Transaction api

        :param xooa_client: Includes Headers and URL to make request
        :param transaction_id: Transaction Id to get transaction details
        :param timeout:
        :param kwargs: Query Arguments for the api including async and timeout
        :return:
        """

        logger = xooa_client.xooa_logger

        try:
            req_params = xooa_client.req_params

            logger.info('Calling Block Chain API for Transaction.')

            params = locals()

            for key, val in six.iteritems(params['kwargs']):

                if key == 'asyncKey':
                    params[key] = val

            del params['kwargs']

            query_params = {}

            if 'asyncKey' in params:
                query_params['async'] = params['asyncKey']
            else:
                query_params['async'] = 'false'

            if timeout is not None:
                query_params['timeout'] = timeout

            url_suffix = '/transactions/' + str(transaction_id)

            url = req_params['base_url'] + url_suffix

            headers = req_params['headers']

            logger.info("Requesting Transaction details...")

            response = requests.get(url, params=query_params, headers=headers)

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
            raise XooaApiException("0", "Exception in GetBlockHeight")
