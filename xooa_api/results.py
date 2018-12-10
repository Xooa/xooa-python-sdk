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

import json
from .xooa_exceptions import XooaApiException, XooaPendingException
import requests


class ResultApi(object):

    def result(self, client_obj, result_id):
        """
        API Returns result of previously submitted transaction

        :param client_obj: Includes Headers and URL to make request
        :param result_id: Result ID of the previously submitted transaction
        :return:
        """
        logger = client_obj.xooa_logger
        try:
            req_params = client_obj.req_params

            logger.info('Result API has been called')
            # verify the required parameter 'result_id' is set
            if result_id is None:

                logger.error("Missing the required parameter `result_id` when calling `result`")

                raise ValueError("Missing the required parameter `result_id` when calling `result`")

            url_suffix = 'results/' + result_id

            url = req_params['base_url'] + url_suffix
            headers = req_params['headers']

            logger.info("Fetching result...")

            request = requests.get(url, headers=headers)
            if request.status_code >= 400:
                raise XooaApiException(request.text, request.status_code)

            response_object = json.loads(request.text)

            if request.status_code == 200:
                return response_object

            elif request.status_code == 202:
                result_id = response_object['resultId']
                result_url = response_object['resultURL']
                raise XooaPendingException(result_id, result_url)
        except Exception:
            logger.exception('Got exception on main handler')
            raise
