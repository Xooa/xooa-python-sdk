#!/usr/bin/env python
# coding: utf-8

import sys
sys.path.append('..')

# Import XooaClient Library
from xooa_api.api_client import XooaClient

# Create an instance of XooaClient
xooa_client = XooaClient()

# Set API Token
xooa_client.set_api_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlLZXkiOiIwOFpKNFhTLTQ2RDRQRVQtRzlSRkZZRy1YMlkySEYzIiwiQXBpU2VjcmV0IjoiMXB5RXdhUHg1SFhLT3hWIiwiUGFzc3BocmFzZSI6IjNiMGM0OGZjZjRjN2M4MDQ4Nzg2ZjkwNmU1ZjE4OTdjIiwiaWF0IjoxNTQ2NTE1ODg3fQ.WtdIW0wVgpb6qR9L7W8ElEu9VQWNg0YlF17ML_HNdbY")

# Validate Token
# xooa_client.validate()

print("----- Start -----")
print()

# To invoke chaincode asynchronously, call invoke_async method
# function name and arguments are required
print("----- Invoke Async -----")
fcn = 'set'
args = ["a","1"]
app_invoke_async = xooa_client.invoke_async(fcn, args)
print(app_invoke_async)
print()

# To invoke chaincode call invoke method
# function name and arguments are required
# timeout is an optional keyword argument
print("----- Invoke -----")
fcn = 'set'
args = ['b','2']
app_invoke = xooa_client.invoke(fcn, args)
print(app_invoke)
print()

# To check whether the transaction has been completed or not, call get_result method
# result_id is required argument
print("----- Result for Invoke Async -----")
result_id = app_invoke_async['resultId']
app_get_result = xooa_client.get_result(result_id)
print(app_get_result)
print()

# To query chaincode asynchronously call query method
# function name is required argument and args is a required keyword argument
print("----- Query Async -----")
fcn = 'get'
args = ["a","b"]
app_query_async = xooa_client.query_async(fcn, args)
print(app_query_async)
print()

# To query chaincode call query method
# function name is required argument and args is a required keyword argument
# timeout is an optional keyword argument
print("----- Query -----")
fcn = 'get'
args = ["a","b"]
app_query = xooa_client.query(fcn, args)
print(app_query['payload'])
print()

# To check whether the transaction has been completed or not, call get_result method
# result_id is required argument
print("----- Result for Query Async -----")
result_id = app_query_async['resultId']
app_get_result = xooa_client.get_result(result_id)
print(app_get_result)
print()

# To get blockchain data asynchronously call get_block_by_number_async method
# block_number is required argument
print("----- Get Block By Number Async -----")
block_number = 2
app_block_by_number_async = xooa_client.get_block_by_number_async(block_number)
print(app_block_by_number_async)
print()

# To get blockchain data call get_block_by_number method
# block_number is required argument
# timeout is an optional keyword argument
print("----- Get Block By Number -----")
block_number = 2
app_block_by_number = xooa_client.get_block_by_number(block_number)
print(app_block_by_number)
print()

# To check whether the transaction has been completed or not, call get_result method
# result_id is required argument
print("----- Result for Block By Number Async -----")
result_id = app_block_by_number_async['resultId']
app_get_result = xooa_client.get_result(result_id)
print(app_get_result)
print()

# To get blockchain height asynchronously call get_current_block_async method
print("----- Current Block Async -----")
app_current_block_async = xooa_client.get_current_block_async()
print(app_current_block_async)
print()

# To get blockchain height call get_current_block method
# timeout is an optional keyword argument
print("----- Current Block -----")
app_current_block = xooa_client.get_current_block(timeout=3000)
print(app_current_block)
print()

# To check whether the transaction has been completed or not, call get_result method
# result_id is required argument
print("----- Result for Current Block Async -----")
result_id = app_current_block_async['resultId']
app_get_result = xooa_client.get_result(result_id)
print(app_get_result)
print()

# To get blockchain height asynchronously call get_current_block_async method
print("----- Get Transaction Async -----")
app_transaction_async = xooa_client.get_transaction_by_transaction_id_async(app_invoke['txId'])
print(app_transaction_async)
print()

# To get blockchain height call get_current_block method
# timeout is an optional keyword argument
print("----- Get Transaction -----")
app_transaction = xooa_client.get_transaction_by_transaction_id(app_invoke['txId'])
print(app_transaction)
print()

# To check whether the transaction has been completed or not, call get_result method
# result_id is required argument
print("----- Result for Get Transaction Async -----")
result_id = app_transaction_async['resultId']
app_get_result = xooa_client.get_result(result_id)
print(app_get_result)
print()

# To get identity information call current_identity method
print("----- Current Identity -----")
app_current_identity = xooa_client.current_identity()
print(app_current_identity)
print()

# To get all the identities information call get_identities method
print("----- Get All Identities -----")
app_get_identities = xooa_client.get_identities()
print(app_get_identities)
print()

# To enroll an identity asynchronously call enroll_identity method
# data is required keyword argument
print("----- Enroll Identity Async -----")
enroll_identity_async_data = {
    "IdentityName": "Test",
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
app_enroll_identity_async = xooa_client.enroll_identity_async(enroll_identity_async_data)
print(app_enroll_identity_async)
print()

# To enroll an identity call enroll_identity method
# data is required keyword argument
print("----- Enroll Identity -----")
enroll_identity_data = {
    "IdentityName": "Test2",
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
app_enroll_identity = xooa_client.enroll_identity(enroll_identity_data)
print(app_enroll_identity)
print()

# To check whether the transaction has been completed or not, call get_result method
# result_id is required argument
print("----- Result for Enroll Identity Async -----")
result_id = app_enroll_identity_async['resultId']
app_get_result = xooa_client.get_result(result_id)
print(app_get_result)
print()

# To regenerate identity api token call regenerate_identity_api_token method
# identity is required argument
print("----- Regenerate Identity API Token -----")
identity = app_enroll_identity['Id']
app_regenerate_identity_api_token = xooa_client.regenerate_identity_api_token(identity)
print(app_regenerate_identity_api_token)
print()

# To get identity call get_identity method
# identity is required argument
print("----- Get Identity Details -----")
identity = app_regenerate_identity_api_token['Id']
app_get_identity = xooa_client.get_identity(identity)
print(app_get_identity)
print()

# To delete identity asynchronously delete_identity_async method
# identity is required argument
print("----- Delete Identity Async -----")
identity = app_enroll_identity['Id']
app_delete_identity_async = xooa_client.delete_identity_async(identity)
print(app_delete_identity_async)
print()

# To delete identity delete_identity method
# identity is required argument
print("----- Delete Identity -----")
identity = app_get_result['result']['Id']
app_delete_identity = xooa_client.delete_identity(identity)
print(app_delete_identity)
print()

# To check whether the transaction has been completed or not, call get_result method
# result_id is required argument
print("----- Result for Enroll Identity Async -----")
result_id = app_delete_identity_async['resultId']
app_get_result = xooa_client.get_result(result_id)
print(app_get_result)
print()

print("----- End -----")
# To subscribe to events call subscribe_all_events method
# callback_on_event is required argument. It is an event handler.

# callback_on_event = 'callback_on_event'
# app_subscribe_events = xooa_client.subscribe_all_events(callback_on_event)
# print(app_subscribe_events)
