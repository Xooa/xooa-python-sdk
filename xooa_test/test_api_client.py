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

import unittest
import sys
sys.path.append('..')
from api_client import XooaClient
import logging


class TestApiClient(unittest.TestCase):

    """BlockchainApi unit xooa_test stubs"""

    # def setUp(self):
    #     self.api = XooaClient()

    def tearDown(self):
        pass

    def test_api_client(self):
        self.api = XooaClient()
        api_token = '<API_TOKEN>'
        set_token = self.api.set_api_token(api_token)
        validate = self.validate()

        set_logging_level = self.api.set_logging_level(logging.debug)
        # print(c)
        pass


        fcn = 'set'
        args = {"args": ["args1", "args2"]}
        invoke = self.api.invoke(fcn, data=args, timeout=3000)
        # print(invoke)
        pass

        fcn = 'set'
        args = {"args": ["args1", "args2"]}
        invoke_async = self.api.invoke_async(fcn, data=args)
        # print(invoke_async)
        pass

        # c = self.api.subscribe_all_events(callback_on_event='callback_on_event')
        # print(c)
        # pass


if __name__ == '__main__':
    unittest.main()
