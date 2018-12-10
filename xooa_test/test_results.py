import unittest
import sys
sys.path.append('..')
from xooa_api.api_client import XooaClient


class TestResultsApi(unittest.TestCase):

    """ResultsApi unit xooa_test stubs"""

    def setUp(self):
        self.api = XooaClient()
        api_token = '<API_TOKEN>'
        set_token = self.api.set_api_token(api_token)
        validate = self.validate()

    def tearDown(self):
        pass

    def test_results(self):

        result_id = '<RESULT_ID>'
        result = self.api.result(result_id)
        self.assertEqual(type(result), dict)


if __name__ == '__main__':
    unittest.main()
