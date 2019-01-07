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


class IdentitiesApi(object):
    """ Identities API class to create requests to Identities API. """

    def authenticated_identity_information(self, xooa_client):
        """ Returns the current Identity the API Token points to in the app.

        :param xooa_client: Includes Headers and URL to make request
        :return:
        """

        logger = xooa_client.xooa_logger

        try:
            req_params = xooa_client.req_params

            logger.info("Calling Identity API for Current Identity info.")

            url_suffix = '/identities/me'

            url = req_params['base_url'] + url_suffix

            headers = req_params['headers']

            logger.info("Sending request to get current identity...")

            response = requests.get(url, headers=headers)

            response_object = json.loads(response.text)

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
            raise XooaApiException("0", "Exception in fetching Authenticating Identity.")

    def delete_identity(self, xooa_client, identity, timeout, **kwargs):
        """ Deletes an identity.

        :param xooa_client: Includes Headers and URL to make request
        :param identity: APP ID
        :param timeout:
        :param kwargs:
        :return:
        """

        logger = xooa_client.xooa_logger

        try:
            req_params = xooa_client.req_params

            logger.info('Calling Identity API to delete identity')

            params = locals()

            for key, val in six.iteritems(params['kwargs']):

                if key == 'asyncKey':
                    params[key] = val

            del params['kwargs']

            # verify the required parameter 'id' is set
            if identity is None:

                logger.error("Missing the required parameter `identity` when calling `delete_identity`")
                raise ValueError("Missing the required parameter `identity` when calling `delete_identity`")

            query_params = {}

            if 'asyncKey' in params:
                query_params['async'] = params['asyncKey']
            else:
                query_params['async'] = 'false'

            if timeout is not None:
                query_params['timeout'] = timeout

            url_suffix = '/identities/' + identity

            url = req_params['base_url'] + url_suffix

            headers = req_params['headers']

            logger.info("Sending request to delete identity...")

            response = requests.delete(url, params=query_params, headers=headers)

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
            raise XooaApiException("0", 'Exception in deleting Identity')

    def enrollment(self, xooa_client, identity, timeout, **kwargs):
        """ The Enroll identity endpoint is used to enroll new identities for the smart contract app.

         A success response includes the API Token generated for the identity.
         This API Token can be used to call API End points on behalf of the enrolled identity.
         This endpoint provides equivalent functionality to adding new identity manually using Xooa console,
         and identities added using this endpoint will appear, and can be managed,
         using Xooa console under the identities tab of the smart contract app.

         Required permission: manage identities (canManageIdentities=true)

        :param xooa_client: Includes Headers and URL to make request
        :param kwargs: Query arguments for the api including Async and timeout
        :param identity: Identity request object to enroll
        :param timeout:
        :return:
        """

        logger = xooa_client.xooa_logger

        try:
            req_params = xooa_client.req_params

            logger.info('Calling Identity API to Enroll new Identity')

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

            data = json.dumps(identity)

            url_suffix = '/identities/'

            url = req_params['base_url'] + url_suffix

            headers = req_params['headers']

            logger.info("Sending request to enroll new identity...")

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
            raise XooaApiException("0", 'Exception in Enrolling a new Identity')

    def identities_get_all_identities(self, xooa_client):
        """ Get all identities from the identity registry

         Required permission: manage identities (canManageIdentities=true)

        :param xooa_client: Includes Headers and URL to make request
        :return:
        """

        logger = xooa_client.xooa_logger

        try:
            req_params = xooa_client.req_params

            logger.info('Calling Identities API to get all identities')

            url_suffix = '/identities/'

            url = req_params['base_url'] + url_suffix

            headers = req_params['headers']

            logger.info("Sending request to get all identities...")

            response = requests.get(url, headers=headers)

            response_object = json.loads(response.text)

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
            raise XooaApiException("0", 'Exception in fetching all identities enrolled')

    def identity_information(self, xooa_client, identity_id):
        """ Get the specified identity from the identity registry.

         Required permission: manage identities (canManageIdentities=true)

        :param xooa_client: Includes Headers and URL to make request
        :param identity_id: Identity id to get the details
        :return:
        """

        logger = xooa_client.xooa_logger

        try:
            req_params = xooa_client.req_params

            logger.info('Calling Identity API to get Identity Info')

            # verify the required parameter 'id' is set
            if identity_id is None:
                logger.error("Missing the required parameter `id` when calling `identity_information`")
                raise ValueError("Missing the required parameter `id` when calling `identity_information`")

            url_suffix = '/identities/' + identity_id

            url = req_params['base_url'] + url_suffix

            headers = req_params['headers']

            logger.info("Sending request to get Identity info...")

            response = requests.get(url, headers=headers)

            response_object = json.loads(response.text)

            if response.status_code == 200:
                return response_object

            else:
                raise XooaApiException(response.status_code, response_object)

        except XooaApiException:
            raise

        except Exception:
            logger.exception('Got exception on main handler')
            raise XooaApiException('0', 'Exception while fetching Identity details')

    def regenerate_token(self, xooa_client, identity_id):
        """ Generates new identity API Token.

         Required permission: manage identities (canManageIdentities=true)

        :param xooa_client: Includes Headers and URL to make request
        :param identity_id: Identity Id to regenerate token for
        :return:
        """

        logger = xooa_client.xooa_logger

        try:
            req_params = xooa_client.req_params

            logger.info('Calling Identity API to Regenerate Token')

            # verify the required parameter 'id' is set
            if identity_id is None:
                logger.error("Missing the required parameter `id` when calling `regenerate_token`")
                raise ValueError("Missing the required parameter `id` when calling `regenerate_token`")

            url_suffix = '/identities/' + identity_id + '/regeneratetoken'

            url = req_params['base_url'] + url_suffix

            headers = req_params['headers']

            logger.info("Sending request to regenerate API token...")

            response = requests.post(url, headers=headers)

            response_object = json.loads(response.text)

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
            raise XooaApiException('0', 'Exception in regenerate token')
