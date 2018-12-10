import unittest
import sys
sys.path.append('..')
from xooa_api.api_client import XooaClient


class TestQueryApi(unittest.TestCase):

    """QueryApi unit xooa_test stubs"""

    def setUp(self):
        self.api = XooaClient()
        api_token = '<API_TOKEN>'
        set_token = self.api.set_api_token(api_token)
        validate = self.validate()

    def tearDown(self):
        pass

    def test_query_sync(self):

        fcn = 'set'
        args = ["args1", "args2"]
        query = self.api.query(fcn, timeout=8000, args=args)
        self.assertEqual(type(query), dict)

    def test_query_async(self):

        fcn = 'set'
        args = ["args1", "args2"]
        query_async = self.api.query_async(fcn, args=args)
        self.assertEqual(type(c), dict)


if __name__ == '__main__':
    unittest.main()
