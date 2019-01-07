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

from __future__ import absolute_import
from xooa_api.api_client import XooaClient
import unittest
import time
import sys
sys.path.append('..')


class TestBlockchainApi(unittest.TestCase):
    """ Block Chain Api unit xooa_test stubs. """

    def setUp(self):
        self.api = XooaClient()
        api_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlLZXkiOiIwOFpKNFhTLTQ2RDRQRVQtRzlSRkZZRy1YMlkySEYzIiwiQXBpU2VjcmV0IjoiMXB5RXdhUHg1SFhLT3hWIiwiUGFzc3BocmFzZSI6IjNiMGM0OGZjZjRjN2M4MDQ4Nzg2ZjkwNmU1ZjE4OTdjIiwiaWF0IjoxNTQ2NTE1ODg3fQ.WtdIW0wVgpb6qR9L7W8ElEu9VQWNg0YlF17ML_HNdbY'
        self.api.set_api_token(api_token)
        pass

    def tearDown(self):
        pass

    def test_blockchain_data_sync(self):
        block_number = 12
        get_block_by_number = self.api.get_block_by_number(block_number)
        self.assertEqual(type(get_block_by_number), dict)
        pass

    def test_blockchain_data_async(self):
        block_number = 12
        get_block_by_number_async = self.api.get_block_by_number_async(block_number)
        self.assertEqual(type(get_block_by_number_async), dict)
        pass

    def test_blockchain_height_sync(self):
        get_current_block = self.api.get_current_block(timeout=3000)
        self.assertEqual(type(get_current_block), dict)
        pass

    def test_blockchain_height_async(self):
        get_current_block_async = self.api.get_current_block_async(timeout=3000)
        self.assertEqual(type(get_current_block_async), dict)
        pass

    def test_transaction_sync(self):
        fcn = 'set'
        args = ["args1", "args2"]
        invoke = self.api.invoke(fcn, args)
        time.sleep(2)
        transaction_data = self.api.get_transaction_by_transaction_id(invoke['txId'])
        self.assertEqual(type(transaction_data), dict)
        pass

    def test_transaction_async(self):
        fcn = 'set'
        args = ["args1", "args2"]
        invoke = self.api.invoke(fcn, args)
        time.sleep(2)
        transaction_async = self.api.get_transaction_by_transaction_id_async(invoke['txId'])
        self.assertEqual(type(transaction_async), dict)
        pass


if __name__ == '__main__':
    print("path")
    print(sys.path)
    unittest.main()
