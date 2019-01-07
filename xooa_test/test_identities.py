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


class TestIdentitiesApi(unittest.TestCase):
    """ Identities Api unit test stubs. """

    def setUp(self):
        self.api = XooaClient()
        api_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlLZXkiOiIwOFpKNFhTLTQ2RDRQRVQtRzlSRkZZRy1YMlkySEYzIiwiQXBpU2VjcmV0IjoiMXB5RXdhUHg1SFhLT3hWIiwiUGFzc3BocmFzZSI6IjNiMGM0OGZjZjRjN2M4MDQ4Nzg2ZjkwNmU1ZjE4OTdjIiwiaWF0IjoxNTQ2NTE1ODg3fQ.WtdIW0wVgpb6qR9L7W8ElEu9VQWNg0YlF17ML_HNdbY'
        self.api.set_api_token(api_token)
        pass

    def tearDown(self):
        pass

    def test_authenticated_identity(self):
        current_identity = self.api.current_identity()
        self.assertEqual(type(current_identity), dict)
        pass

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
        enroll_identity = self.api.enroll_identity(enroll_identity_data)
        self.assertEqual(type(enroll_identity), dict)
        pass

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
        enroll_identity_async = self.api.enroll_identity_async(enroll_identity_data)
        self.assertEqual(type(enroll_identity_async), dict)
        pass

    def test_get_all_identities(self):
        c = self.api.get_identities()
        self.assertEqual(type(c), list)

    def test_get_identity_information(self):
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
        enroll_identity = self.api.enroll_identity(enroll_identity_data)
        time.sleep(2)
        get_identity = self.api.get_identity(enroll_identity['Id'])
        self.assertEqual(type(get_identity), dict)
        pass

    def test_regenerate_token(self):
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
        enroll_identity = self.api.enroll_identity(enroll_identity_data)
        time.sleep(2)
        regenerate_identity_api_token = self.api.regenerate_identity_api_token(enroll_identity['Id'])
        self.assertEqual(type(regenerate_identity_api_token), dict)
        pass

    def test_delete_identity_sync(self):
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
        enroll_identity = self.api.enroll_identity(enroll_identity_data)
        time.sleep(2)
        delete_identity = self.api.delete_identity(enroll_identity['Id'])
        self.assertEqual(type(delete_identity), dict)
        pass

    def test_delete_identity_async(self):
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
        enroll_identity = self.api.enroll_identity(enroll_identity_data)
        time.sleep(2)
        delete_identity_async = self.api.delete_identity_async(enroll_identity['Id'])
        self.assertEqual(type(delete_identity_async), dict)
        pass


if __name__ == '__main__':
    unittest.main()
