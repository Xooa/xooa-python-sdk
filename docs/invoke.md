# InvokeApi

All URIs are relative to *https://api.ci.xooa.io/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoke**](InvokeApi.md#invoke) | **POST** /invoke/{fcn} | Submit blockchain transaction


# **invoke**
> invoke(fcn, async=async, timeout=timeout)

Submit blockchain transaction

The Invoke API End Point is used for submitting transaction for processing by the blockchain Smart Contract app. The end point must call a function already defined in your Smart Contract app which will process the Invoke request. The function name is part of the endpoint URL, or can be entered as the fcn parameter when testing using the Sandbox. For example, if testing the sample get-set Smart Contract app, use ‘set’ (without quotes)  as the value for fcn.   The function arguments (number of arguments and type) is determined by the Smart Contract. The Smart Contract is also responsible for arguments validation and exception management. The payload object of Invoke Transaction Response in case of Final Response is determined by the Smart Contract app.   A success response may be either 200 or 202.

### Example
Create an instance of XooaClient
```
import xooa_api.api_client import XooaClient
xooa_client = XooaClient()
```
Set API token and Validate
```
api_token = '<API_TOKEN>' 
set_api_token = xooa_client.set_api_token(api_token)
validate = self.validate()
```
 To invoke chaincode call invoke method
 function name is required argument and data is a required keyword argument
 timeout is an optional keyword argument
```
fcn = 'set'
args = {"args":["args1","args2"]}
app_invoke = xooa_client.invoke(fcn, data=args, timeout=5000)
```

To invoke chaincode asynchronously, call invoke_async method
 function name is required argument and data is a required keyword argument
```
fcn = 'set'
args = {"args":["args1","args2"]}
app_invoke_async = foo.invoke_async(fcn, data=args)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fcn** | **str**| The blockchain Smart Contract app function name to invoke | 
 **async** | **str**| Call this request asynchronously without waiting for response | [optional] 
 **timeout** | **str**| Request timeout in millisecond | [optional] 