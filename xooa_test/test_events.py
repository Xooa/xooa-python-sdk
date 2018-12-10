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
from xooa_api.api_client import XooaClient


class TestEventListener(unittest.TestCase):

    """BlockchainApi unit xooa_test stubs"""

    # def setUp(self):
    #     self.api = XooaClient()

    def tearDown(self):
        pass

    def test_api_client(self):
        self.api = XooaClient()
        self.api_token = '<API_TOKEN>'
        callback_on_event = 'callback_on_event'
        self.socket_host = 'https://api.xooa.io/subscribe'
        subscribe = self.api.subscribe_all_events(self, callback_on_event)
        # print (c)

if __name__ == '__main__':
    unittest.main()
