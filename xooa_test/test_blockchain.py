import unittest
import sys
sys.path.append('..')
from xooa_api.api_client import XooaClient


class TestBlockchainApi(unittest.TestCase):

    """BlockchainApi unit xooa_test stubs"""

    def setUp(self):
        self.api = XooaClient()
        api_token = '<API_TOKEN>'
        set_token = self.api.set_api_token(api_token)
        validate = self.api.validate()

    def tearDown(self):
        pass

    def test_blockchain_data_sync(self):
        block_number = 12
        get_block_by_number = self.api.get_block_by_number(block_number)
        self.assertEqual(type(get_block_by_number), dict)

    def test_blockchain_data_async(self):
        block_number = 12
        get_block_by_number_async = self.api.get_block_by_number_async(block_number)
        self.assertEqual(type(get_block_by_number_async), dict)

    def test_blockchain_height_sync(self):

        get_current_block = self.api.get_current_block(timeout=3000)
        self.assertEqual(type(get_current_block), dict)

    def test_blockchain_height_async(self):

        get_current_block_async = self.api.get_current_block_async(timeout=3000)
        self.assertEqual(type(get_current_block_async), dict)


if __name__ == '__main__':
    unittest.main()
