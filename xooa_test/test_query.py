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


class TestQueryApi(unittest.TestCase):
    """ QueryApi unit test stubs. """

    def setUp(self):
        self.api = XooaClient()
        api_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlLZXkiOiIwOFpKNFhTLTQ2RDRQRVQtRzlSRkZZRy1YMlkySEYzIiwiQXBpU2VjcmV0IjoiMXB5RXdhUHg1SFhLT3hWIiwiUGFzc3BocmFzZSI6IjNiMGM0OGZjZjRjN2M4MDQ4Nzg2ZjkwNmU1ZjE4OTdjIiwiaWF0IjoxNTQ2NTE1ODg3fQ.WtdIW0wVgpb6qR9L7W8ElEu9VQWNg0YlF17ML_HNdbY'
        self.api.set_api_token(api_token)
        pass

    def tearDown(self):
        pass

    def test_query_sync(self):
        fcn = 'get'
        args = ["args1"]
        query = self.api.query(fcn, args)
        time.sleep(2)
        self.assertEqual(type(query), dict)
        pass

    def test_query_async(self):
        fcn = 'get'
        args = ["args1"]
        query_async = self.api.query_async(fcn, args)
        time.sleep(2)
        self.assertEqual(type(query_async), dict)
        pass


if __name__ == '__main__':
    unittest.main()
