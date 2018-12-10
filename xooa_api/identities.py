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


class IdentitiesApi(object):

    def authenticated_identity_information(self, client_obj):
        """
        This End Point Returns Information about the Authenticated Identity

        :param client_obj: Includes Headers and URL to make request
        :return:
        """
        logger = client_obj.xooa_logger
        try:
            req_params = client_obj.req_params

            logger.info("Identity Info Api has been called")

            url_suffix = 'identities/me'

            url = req_params['base_url'] + url_suffix
            headers = req_params['headers']

            logger.info("Sending request...")

            request = requests.get(url, headers=headers)
            if request.status_code >= 400:
                raise XooaApiException(request.text, request.status_code)
            response_object = json.loads(request.text)

            if request.status_code == 200:
                return response_object
            else:
                request.raise_for_status()
        except Exception:
            logger.exception('Got exception on main handler')
            raise

    def delete_identity(self, client_obj,  identity, **kwargs):
        """
        This Endpoint deletes Identity

        :param client_obj: Includes Headers and URL to make request
        :param identity: APP ID
        :param kwargs:
        :param str async: Call this request asynchronously without waiting for response
        :param str timeout: Request timeout in millisecond
        :return:
        """
        logger = client_obj.xooa_logger
        try:
            req_params = client_obj.req_params


            logger.info('Delete Identity API has been called')

            all_params = ['identity', 'asyncKey', 'timeout']

            params = locals()
            for key, val in six.iteritems(params['kwargs']):
                if key not in all_params:

                    logger.error("Got an unexpected keyword argument '%s'"
                                 " to method delete_identity" % key)

                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method delete_identity" % key
                    )
                params[key] = val
            del params['kwargs']
            # verify the required parameter 'id' is set
            if 'identity' not in params or params['identity'] is None:

                logger.error("Missing the required parameter `identity` when calling `delete_identity`")

                raise ValueError("Missing the required parameter `identity` when calling `delete_identity`")

            query_params = {}
            if 'async' in params:
                query_params['async'] = params['asyncKey']
            else:
                query_params['async'] = 'false'
            if 'timeout' in params:
                query_params['timeout'] = params['timeout']

            url_suffix = '/identities/' + identity

            url = req_params['base_url'] + url_suffix
            headers = req_params['headers']

            logger.info("Sending request...")

            request = requests.delete(url, headers=headers)

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

    def enrollment(self, client_obj, **kwargs):
        """
        The Enroll Identity end point is used to  enroll new identities for the Smart Contract app.
        A success response includes the API Key generated for the identity. This API Key can be used to call API End points
        on behalf of the enrolled identity. This End Point provides equivalent functionality to adding new identity manually
        using Xooa console, and identities added using this end point will appear, and can be managed, using Xooa console
        under the identities tab of the Smart Contract app Required permission: manage identities (canManageIdentities=true)

        :param client_obj: Includes Headers and URL to make request
        :param kwargs:
        :param str async: Call this request asynchronously without waiting for response
        :param str timeout: Request timeout in millisecond
        :return:
        """
        logger = client_obj.xooa_logger
        try:
            req_params = client_obj.req_params

            logger.info('Identity Enrollment API has been called')

            all_params = ['asyncKey', 'timeout', 'data']

            params = locals()
            for key, val in six.iteritems(params['kwargs']):
                if key not in all_params:
                    logger.error("Got an unexpected keyword argument '%s'"
                                 " to method enrollment" % key)

                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method enrollment" % key
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

            body_params = params['data']

            data = json.dumps(body_params)

            url_suffix = 'identities/'

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

    def identities_get_all_identities(self, client_obj):
        """
        Get all identities from the identity registry

        :param client_obj: Includes Headers and URL to make request
        :return:
        """
        logger = client_obj.xooa_logger
        try:
            req_params = client_obj.req_params

            logger.info('Get All Identities API has been called')

            url_suffix = 'identities/'

            url = req_params['base_url'] + url_suffix
            headers = req_params['headers']

            logger.info("Sending request...")

            request = requests.get(url, headers=headers)
            if request.status_code >= 400:
                raise XooaApiException(request.text, request.status_code)
            response_object = json.loads(request.text)

            if request.status_code == 200:
                return response_object
            else:
                request.raise_for_status()

        except Exception:
            logger.exception('Got exception on main handler')
            raise

    def identity_information(self, client_obj, identity):
        """
        Get the specified identity from the identity registry

        :param client_obj: Includes Headers and URL to make request
        :param identity: APP ID
        :return:
        """
        logger = client_obj.xooa_logger
        try:
            req_params = client_obj.req_params

            logger.info('Get Identity API has been called')
            # verify the required parameter 'id' is set
            if identity is None:
                logger.error("Missing the required parameter `id` when calling `identity_information`")
                raise ValueError("Missing the required parameter `id` when calling `identity_information`")

            url_suffix = 'identities/'+identity

            url = req_params['base_url'] + url_suffix
            headers = req_params['headers']

            logger.info("Sending request...")

            request = requests.get(url, headers=headers)

            if request.status_code >= 400:
                raise XooaApiException(request.text, request.status_code)

            response_object = json.loads(request.text)

            if request.status_code == 200:
                return response_object
            else:
                request.raise_for_status()
        except Exception:
            logger.exception('Got exception on main handler')
            raise

    def regenerate_token(self, client_obj, identity):
        """
        Regenerate Identity API Token

        :param client_obj: Includes Headers and URL to make request
        :param identity: APP ID
        :return:
        """
        logger = client_obj.xooa_logger
        try:
            req_params = client_obj.req_params

            logger.info('Regenerate Token API has been called')
            # verify the required parameter 'id' is set
            if identity is None:

                logger.error("Missing the required parameter `id` when calling `regenerate_token`")

                raise ValueError("Missing the required parameter `id` when calling `regenerate_token`")

            url_suffix = '/identities/' + identity + '/regeneratetoken'

            url = req_params['base_url'] + url_suffix
            headers = req_params['headers']

            logger.info("Sending request...")

            request = requests.post(url, headers=headers)
            if request.status_code >= 400:
                raise XooaApiException(request.text, request.status_code)
            response_object = json.loads(request.text)

            if request.status_code == 200:
                return response_object
            else:
                request.raise_for_status()
        except Exception:
            logger.exception('Got exception on main handler')
            raise
