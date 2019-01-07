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

from xooa_api.api_client import XooaClient
import unittest
import time
import sys
sys.path.append('..')


class TestInvokeApi(unittest.TestCase):
    """ InvokeApi unit test stubs. """

    def setUp(self):
        self.api = XooaClient()
        api_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlLZXkiOiIwOFpKNFhTLTQ2RDRQRVQtRzlSRkZZRy1YMlkySEYzIiwiQXBpU2VjcmV0IjoiMXB5RXdhUHg1SFhLT3hWIiwiUGFzc3BocmFzZSI6IjNiMGM0OGZjZjRjN2M4MDQ4Nzg2ZjkwNmU1ZjE4OTdjIiwiaWF0IjoxNTQ2NTE1ODg3fQ.WtdIW0wVgpb6qR9L7W8ElEu9VQWNg0YlF17ML_HNdbY'
        self.api.set_api_token(api_token)
        pass

    def tearDown(self):
        pass

    def test_invoke_async(self):
        fcn = 'set'
        args = ["args1", "args2"]
        invoke_async = self.api.invoke_async(fcn, args)
        time.sleep(2)
        self.assertEqual(type(invoke_async), dict)
        pass

    def test_invoke_sync(self):
        fcn = 'set'
        args = ["args1", "args2"]
        invoke = self.api.invoke(fcn, args, 4000)
        time.sleep(2)
        self.assertEqual(type(invoke), dict)
        pass


if __name__ == '__main__':
    unittest.main()
