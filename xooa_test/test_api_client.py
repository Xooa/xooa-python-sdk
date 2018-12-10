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
