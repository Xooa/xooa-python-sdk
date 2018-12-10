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
from xooa_api.api_client import XooaClient


class TestInvokeApi(unittest.TestCase):

    """InvokeApi unit xooa_test stubs"""

    def setUp(self):
        self.api = XooaClient()
        api_token = '<API_TOKEN>'
        set_token = self.api.set_api_token(api_token)
        validate = self.validate()

    def tearDown(self):
        pass

    def test_invoke_async(self):

        fcn = 'set'
        args = {"args": ["args1", "args2"]}
        invoke_async = self.api.invoke_async(fcn, data=args)
        self.assertEqual(type(invoke_async), dict)

    def test_invoke_sync(self):

        fcn = 'set'
        args = {"args": ["args1", "args2"]}
        invoke = self.api.invoke(fcn, data=args, timeout=3000)
        self.assertEqual(type(invoke), dict)


if __name__ == '__main__':
    unittest.main()
