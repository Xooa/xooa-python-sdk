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
