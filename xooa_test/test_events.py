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
