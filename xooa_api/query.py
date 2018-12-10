# coding: utf-8

# python 2 and python 3 compatibility library
import six

import requests
import json
from .xooa_exceptions import XooaApiException, XooaRequestTimeoutException, XooaPendingException


class QueryApi(object):

    def query(self, client_obj, fcn, **kwargs):
        """
        The query API End Point is used for querying blockchain state.
        The end point must call a function already defined in your Smart Contract app which will process the query request.
        The function name is part of the endpoint URL, or can be entered as the fcn parameter  when testing using the Sandbox.
        The function arguments (number of arguments and type) is determined by the Smart Contract.
        The Smart Contract is responsible for validation and exception management.
        For example, if testing the sample get-set Smart Contract app, enter ‘get’ (without quotes) as the value for fcn.
        The response body is also determined by the Smart Contract app, and that’s also the reason why a consistent response sample is unavailable for this end point.
        A success response may be either 200 or 202. For more details refer to Synchronous vs Asynchronous Calls.
        In contrast to Invoke, the Query end point will often return fast even when called in Synchronous mode

        :param client_obj: Includes Headers and URL to make request
        :param str fcn: function name
        :param kwargs:
        :param str async: Call this request asynchronously without waiting for response
        :param str timeout: Request timeout in millisecond
        :return:
        """
        logger = client_obj.xooa_logger
        try:
            req_params = client_obj.req_params

            logger.info('Query API has been called')

            all_params = ['fcn', 'args', 'async', 'timeout']

            params = locals()
            for key, val in six.iteritems(params['kwargs']):
                if key not in all_params:

                    logger.error("Got an unexpected keyword argument '%s'"
                                 " to method query" % key)

                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method query" % key
                    )
                params[key] = val
            del params['kwargs']
            # verify the required parameter 'fcn' is set
            if 'fcn' not in params or params['fcn'] is None:

                logger.error("Missing the required parameter `fcn` when calling `query`")

                raise ValueError("Missing the required parameter `fcn` when calling `query`")

            query_params = {}
            if 'args' in params:
                query_params['args'] =  json.dumps(params['args'])
            if 'async' in params:
                query_params['async'] = params['async']
            else:
                query_params['async'] = 'false'
            if 'timeout' in params:
                query_params['timeout'] = params['timeout']

            url_suffix = '/query/' + fcn

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
