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

    def test_authenticated_identity(self):

        current_identity = self.api.current_identity()
        self.assertEqual(type(current_identity), dict)

    def test_enrollment_sync(self):

        enroll_identity_data = {
          "IdentityName": "string",
          "Access": "r",
          "Attrs": [
            {
              "name": "string",
              "ecert": True,
              "value": "string"
            }
          ],
          "canManageIdentities": True
        }
        enroll_identity = self.api.enroll_identity(data=enroll_identity_data)
        self.assertEqual(type(enroll_identity), dict)

    def test_enrollment_async(self):

        enroll_identity_data = {
          "IdentityName": "string",
          "Access": "r",
          "Attrs": [
            {
              "name": "string",
              "ecert": True,
              "value": "string"
            }
          ],
          "canManageIdentities": True
        }
        enroll_identity_async = self.api.enroll_identity_async(data=enroll_identity_data)
        self.assertEqual(type(enroll_identity_async), dict)

    def test_get_all_identities(self):


        c = self.api.get_identities()
        self.assertEqual(type(c), dict)

    def test_get_identity_information(self):

        identity = '<IDENTITY>'
        get_identity = self.api.get_identity(identity)
        self.assertEqual(type(get_identity), dict)

    def test_regenerate_token(self):

        identity = '<IDENTITY>'
        regenerate_identity_api_token = self.api.regenerate_identity_api_token(identity)
        self.assertEqual(type(regenerate_identity_api_token), dict)

    def test_delete_identity_sync(self):

        identity = '<IDENTITY>'
        delete_identity = self.api.delete_identity(identity)
        self.assertEqual(type(delete_identity), dict)

    def test_delete_identity_async(self):

        identity = '<IDENTITY>'
        delete_identity_async = self.api.delete_identity_async(identity)
        self.assertEqual(type(delete_identity_async), dict)


if __name__ == '__main__':
    unittest.main()
