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

    def __init__(self, api_token=None, url=None):
        self.api_token = api_token
        self.url = url
        self.is_valid = False
        self.error = {
            'error_msg': 'Unauthorized',
            'error_code': 401}
        self.socket_host = 'https://api.xooa.com/subscribe'
        self.token_prefix = 'Bearer '
        self.req_params = {
            'headers': {'Content-Type': 'application/json'},
            'base_url': 'https://api.xooa.com/api/v1/'}
        self.logs = Logger()
        self.xooa_logger = self.logs.get_logger('DEBUG')

    def set_api_token(self, api_token):
        if api_token:
            self.api_token = api_token
            return 'API Token has been set. Please validate.'
        else:
            raise InvalidParameterException()

    def set_url(self, url):
        if url:
            self.req_params['base_url'] = url
            return "URL has been set"
        else:
            raise InvalidParameterException()

    def validate(self):
        if self.api_token:
            logger = self.xooa_logger

            url_for_validation = self.req_params['base_url'] + 'identities/me/'

            self.req_params['headers']['Authorization'] = self.token_prefix + self.api_token
            logger.debug('Validating API Token...')
            try:
                request = requests.get(url_for_validation, headers=self.req_params['headers'])
                if request.status_code == 200:
                    logger.debug(request)

                    self.is_valid = True
                    return request
                elif request.status_code >= 400:
                    self.error['error_code'] = request.status_code
                    self.error['error_msg'] = request.text
                    raise XooaApiException(request.text, request.status_code)
            except Exception:
                raise
        else:
            raise InvalidParameterException()

    def invoke(self, fcn, **kwargs):
        if self.is_valid:
            invoke_api = InvokeApi()
            r = invoke_api.invoke(self, fcn, **kwargs)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def invoke_async(self, fcn, **kwargs):
        if self.is_valid:
            invoke_api = InvokeApi()
            r = invoke_api.invoke(self, fcn, asyncKey='true', **kwargs)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def query(self, fcn, **kwargs):
        if self.is_valid:
            query_api = QueryApi()
            r = query_api.query(self, fcn, **kwargs)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def query_async(self, fcn, **kwargs):
        if self.is_valid:
            query_api = QueryApi()
            r = query_api.query(self, fcn, asyncKey='true', **kwargs)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def get_block_by_number(self, block_number, **kwargs):
        if self.is_valid:
            blockchain_api = BlockchainApi()
            r = blockchain_api.block_data(self, block_number, **kwargs)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def get_block_by_number_async(self, block_number, **kwargs):
        if self.is_valid:
            blockchain_api = BlockchainApi()
            r = blockchain_api.block_data(self, block_number, asyncKey='true', **kwargs)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def get_current_block(self, **kwargs):
        if self.is_valid:
            blockchain_api = BlockchainApi()
            r = blockchain_api.block_height(self, **kwargs)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def get_current_block_async(self, **kwargs):
        if self.is_valid:
            blockchain_api = BlockchainApi()
            r = blockchain_api.block_height(self, asyncKey='true', **kwargs)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def current_identity(self):
        if self.is_valid:
            identities_api = IdentitiesApi()
            r = identities_api.authenticated_identity_information(self)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def get_identities(self):
        if self.is_valid:
            identities_api = IdentitiesApi()
            r = identities_api.identities_get_all_identities(self)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def enroll_identity(self, **kwargs):
        if self.is_valid:
            identities_api = IdentitiesApi()
            r = identities_api.enrollment(self, **kwargs)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def enroll_identity_async(self, **kwargs):
        if self.is_valid:
            identities_api = IdentitiesApi()
            r = identities_api.enrollment(self, asyncKey='true', **kwargs)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def regenerate_identity_api_token(self, identity):
        if self.is_valid:
            identities_api = IdentitiesApi()
            r = identities_api.regenerate_token(self, identity)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def delete_identity(self, identity, **kwargs):
        if self.is_valid:
            identities_api = IdentitiesApi()
            r = identities_api.delete_identity(self, identity, **kwargs)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def delete_identity_async(self, identity, **kwargs):
        if self.is_valid:
            identities_api = IdentitiesApi()
            r = identities_api.delete_identity(self, identity, asyncKey='true', **kwargs)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def get_identity(self, identity):
        if self.is_valid:
            identities_api = IdentitiesApi()
            r = identities_api.identity_information(self, identity)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

    def get_result(self, result_id):
        if self.is_valid:
            results_api = ResultApi()
            r = results_api.result(self, result_id)
            return r
        else:
            raise XooaApiException(self.error['error_msg'], self.error['error_code'])

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

    def set_logging_level(self, logging_level):
        if logging_level:
            self.xooa_logger = self.logs.get_logger(logging_level)
        else:
            raise InvalidParameterException()
