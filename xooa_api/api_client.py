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

from .xooa_exceptions import XooaRequestTimeoutException
from .xooa_exceptions import XooaApiException, InvalidParameterException
from .invoke import InvokeApi
from .query import QueryApi
from .blockchain import BlockchainApi
from .results import ResultApi
from .identities import IdentitiesApi
from .event_listener import EventListener
import requests
from .logger import Logger


class XooaClient(object):
    """ Base class to connect with the Xooa Blockchain PaaS.

    This class provides all the methods exposed by the SDK.
    """

    def __init__(self, api_token=None, url='https://api.xooa.com/api/v1'):
        """ Constructor to get an instance of XooaClient

        :param api_token: API Token for the app to connect to.
        :param url: Url where the app is deployed. Default to https://api.xooa.com/api/v1
        """

        self.api_token = api_token
        self.url = url
        self.is_valid = False
        self.socket_host = 'https://api.xooa.com/subscribe'
        self.token_prefix = 'Bearer '
        self.req_params = {
            'headers': {'Content-Type': 'application/json'},
            'base_url': url}
        self.logs = Logger()
        self.xooa_logger = self.logs.get_logger('DEBUG')
        self.req_params['headers']['Authorization'] = self.api_token

    def validate(self):
        """ To validate if the API Token and App Url are valid and point to an existing App in xooa. """

        logger = self.xooa_logger

        url_for_validation = self.req_params['base_url'] + '/identities/me/'

        # self.req_params['headers']['Authorization'] = self.api_token

        logger.debug('Validating API Token...')
        logger.info('Validating API Token...')

        try:
            response = requests.get(url_for_validation, headers=self.req_params['headers'])

            if response.status_code == 200:

                logger.debug(response)

                self.is_valid = True

                return response

            elif response.status_code == 202:

                logger.debug(response)

                raise XooaRequestTimeoutException(response.text['resultId'], response.text['resultURL'])

            else:

                raise XooaApiException(response.status_code, response.text)

        except XooaApiException:
            raise

        except XooaRequestTimeoutException:
            raise

        except Exception:
            raise XooaApiException("0", "Exception trying to validate API Token")

    def set_api_token(self, api_token):
        """ Method to set API Token for the app.

        :param api_token: API Token for the app to connect to.
        :return:
        """

        try:
            self.api_token = api_token
            self.req_params['headers']['Authorization'] = self.api_token
            self.validate()
            return 'API Token has been set.'

        except InvalidParameterException:
            raise

        except XooaApiException:
            raise

        except Exception:
            raise XooaApiException("0", "Exception trying to set API Token")

    def set_url(self, url):
        """ Method to set App URL for the app.

        This URL is default to https://api.xooa.com/api/v1.
        This can be changed to some other if you are deploying the app in local setup.

        :param url: App Url where the app is deployed.
        :return:
        """

        if url:
            self.req_params['base_url'] = url
            return "URL has been set"

        else:
            raise InvalidParameterException()

    # Invoke Methods

    def invoke(self, fcn, args, timeout=4000):
        """ Invoke Submit block chain transactions.

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

        :param fcn: Function name in the smart contract to be invoked
        :param args: Arguments to pass to the smart contract
        :param timeout: Query timeout argument for the api
        :return:
        """

        return InvokeApi().invoke(self, fcn, args, timeout)

    def invoke_async(self, fcn, args):
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

        :param fcn: Function name in the smart contract to invoke
        :param args: Arguments to pass to the smart contract
        :param timeout: Query timeout arguments for the api
        :return:
        """

        return InvokeApi().invoke(self, fcn, args, 4000, asyncKey='true')

    # Query Methods

    def query(self, fcn, args, timeout=4000):
        """ Query - Query block chain data.

         The query API End Point is used for querying block chain state.
         The end point must call a function already defined in your Smart Contract app
         which will process the query request. The function name is part of the endpoint URL,
         or can be entered as the fcn parameter when testing using the Sandbox.
         The function arguments (number of arguments and type) is determined by the Smart Contract.
         The Smart Contract is responsible for validation and exception management.
         For example, if testing the sample get-set Smart Contract app, enter ‘get’ (without quotes)
         as the value for fcn. The response body is also determined by the Smart Contract app,
         and that’s also the reason why a consistent response sample is unavailable for
         this end point. A success response may be either 200 or 202.

        :param fcn: Function name in the smart contract to invoke
        :param args: Arguments to pass to the smart contract
        :param timeout: Query timeout arguments for the api
        :return:
        """

        return QueryApi().query(self, fcn, args, timeout)

    def query_async(self, fcn, args):
        """ Query - Query block chain data in async mode.

         The query API End Point is used for querying block chain state.
         The end point must call a function already defined in your Smart Contract app
         which will process the query request. The function name is part of the endpoint URL,
         or can be entered as the fcn parameter when testing using the Sandbox.
         The function arguments (number of arguments and type) is determined by the Smart Contract.
         The Smart Contract is responsible for validation and exception management.
         For example, if testing the sample get-set Smart Contract app, enter ‘get’ (without quotes)
         as the value for fcn. The response body is also determined by the Smart Contract app,
         and that’s also the reason why a consistent response sample is unavailable for
         this end point. A success response may be either 200 or 202.

        :param fcn: Function name in the smart contract to invoke
        :param args: Arguments to pass to the smart contract
        :param timeout: Query timeout arguments for the api
        :return:
        """

        return QueryApi().query(self, fcn, args, 4000, asyncKey='true')

    # Block Chain API Methods

    def get_block_by_number(self, block_number, timeout=4000):
        """ Use this endpoint to Get the number of transactions and
         hashes of a specific block in the network parameters.

        :param block_number: block number to get the details.
        :param timeout: Query timeout arguments for the api
        :return:
        """

        return BlockchainApi().block_data(self, block_number, timeout)

    def get_block_by_number_async(self, block_number):
        """ Use this endpoint to Get the number of transactions and
         hashes of a specific block in the network parameters in async mode.

        :param block_number: block number to get the details.
        :param kwargs: Query arguments for the api including Async and timeout
        :return:
        """

        return BlockchainApi().block_data(self, block_number, 4000, asyncKey='true')

    def get_current_block(self, timeout=4000):
        """ Use this endpoint to Get the block number and hashes of current (highest)
         block in the network.

        :param timeout: Query timeout arguments for the api
        :return:
        """

        return BlockchainApi().block_height(self, timeout)

    def get_current_block_async(self, timeout=4000):
        """ Use this endpoint to Get the block number and hashes of current (highest)
        block in the network in async mode.

        :param timeout: Query timeout arguments for the api
        :return:
        """

        return BlockchainApi().block_height(self, timeout, asyncKey='true')

    def get_transaction_by_transaction_id(self, transaction_id, timeout=4000):
        """ Use this endpoint to Get transaction by transaction id

        :param transaction_id: Transaction Id for the transaction
        :param timeout: Query timeout arguments for the api
        :return:
        """

        return BlockchainApi().get_transaction_by_transaction_id(self, transaction_id, timeout)

    def get_transaction_by_transaction_id_async(self, transaction_id):
        """ Use this endpoint to Get transaction by transaction id

        :param transaction_id: Transaction Id for the transaction
        :param kwargs: Query arguments for the api including Async and timeout
        :return:
        """

        return BlockchainApi().get_transaction_by_transaction_id(self, transaction_id, 4000, asyncKey='true')

    # Identity Methods

    def current_identity(self):
        """ Returns the current Identity the API Token points to in the app.

        :return:
        """

        return IdentitiesApi().authenticated_identity_information(self)

    def get_identities(self):
        """ Get all identities from the identity registry

        Required permission: manage identities (canManageIdentities=true)

        :return:
        """

        return IdentitiesApi().identities_get_all_identities(self)

    def enroll_identity(self, identity, timeout=4000):
        """ The Enroll identity endpoint is used to enroll new identities for the smart contract app.

        A success response includes the API Token generated for the identity.
        This API Token can be used to call API End points on behalf of the enrolled identity.
        This endpoint provides equivalent functionality to adding new identity manually using Xooa console,
        and identities added using this endpoint will appear, and can be managed,
        using Xooa console under the identities tab of the smart contract app.

        Required permission: manage identities (canManageIdentities=true)

        :param timeout: Query timeout arguments for the api
        :param identity: Identity request object to enroll
        :return:
        """

        return IdentitiesApi().enrollment(self, identity, timeout)

    def enroll_identity_async(self, identity):
        """ The Enroll identity endpoint is used to enroll new identities for the smart contract app.

        A success response includes the API Token generated for the identity.
        This API Token can be used to call API End points on behalf of the enrolled identity.
        This endpoint provides equivalent functionality to adding new identity manually using Xooa console,
        and identities added using this endpoint will appear, and can be managed,
        using Xooa console under the identities tab of the smart contract app.

        Required permission: manage identities (canManageIdentities=true)

        :param identity: Identity request object to enroll
        :return:
        """

        return IdentitiesApi().enrollment(self, identity, 4000, asyncKey='true')

    def regenerate_identity_api_token(self, identity):
        """ Generates new identity API Token.

        Required permission: manage identities (canManageIdentities=true)

        :param identity: Identity Id to regenerate the token
        :return:
        """

        return IdentitiesApi().regenerate_token(self, identity)

    def delete_identity(self, identity, timeout=4000):
        """ Deletes an identity.

        Required permission: manage identities (canManageIdentities=true)

        :param identity: Identity Id to delete the Identity
        :param kwargs: Query arguments for the api including Async and timeout
        :return:
        """

        return IdentitiesApi().delete_identity(self, identity, timeout)

    def delete_identity_async(self, identity):
        """ Deletes an identity in async mode.

        Required permission: manage identities (canManageIdentities=true)

        :param identity: Identity Id to delete the Identity
        :param kwargs: Query arguments for the api including Async and timeout
        :return:
        """

        return IdentitiesApi().delete_identity(self, identity, 4000, asyncKey='true')

    def get_identity(self, identity):
        """ Get the specified identity from the identity registry.

        Required permission: manage identities (canManageIdentities=true)

        :param identity: Identity Id to get the Identity data
        :return:
        """

        return IdentitiesApi().identity_information(self, identity)

    # Result Method

    def get_result(self, result_id):
        """ This endpoint returns the result of previously submitted api request.

        :param result_id: The Result Id to find the result details.
        :return:
        """

        return ResultApi().result(self, result_id)

    # Subscribe Methods

    def subscribe_all_events(self, callback_on_event):
        if callback_on_event == 'callback_on_event':
            try:
                event_listener = EventListener()
                event_listener.subscribe_events(self, self.callback_on_event)
            except Exception:
                error_message = 'Connection could not be established'
                error_code = 503
                raise XooaApiException(error_message, error_code)
        else:
            raise InvalidParameterException()

    def unsubscribe(self):
        event_listener = EventListener()
        r = event_listener.unsubscribe(self, self.event_handler())

    def callback_on_event(self, data):
        return data

    # Logging Method

    def set_logging_level(self, logging_level):
        """

        :param logging_level:
        :return:
        """

        if logging_level:
            self.xooa_logger = self.logs.get_logger(logging_level)
        else:
            raise InvalidParameterException()
