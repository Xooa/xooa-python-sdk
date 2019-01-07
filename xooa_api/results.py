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

import json
import requests
from .xooa_exceptions import XooaApiException, XooaRequestTimeoutException


class ResultApi(object):
    """ Result API class to make request to Result API. """

    def result(self, xooa_client, result_id):
        """ This endpoint returns the result of previously submitted api request.

        :param xooa_client: Includes Headers and URL to make request
        :param result_id: Result ID of the previously submitted transaction
        :return:
        """

        logger = xooa_client.xooa_logger

        try:
            req_params = xooa_client.req_params

            logger.info('Result API has been called')

            # verify the required parameter 'result_id' is set
            if result_id is None:
                logger.error("Missing the required parameter `result_id` when calling `result`")
                raise ValueError("Missing the required parameter `result_id` when calling `result`")

            url_suffix = '/results/' + result_id

            url = req_params['base_url'] + url_suffix

            headers = req_params['headers']

            logger.info("Fetching result...")

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
            raise XooaApiException('0', 'Exception in calling Result API')
