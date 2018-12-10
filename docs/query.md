All URIs are relative to *https://api.ci.xooa.io/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query**](QueryApi.md#query) | **GET** /query/{fcn} | Query Blockchain data


Query Blockchain data

The query API End Point is used for querying blockchain state. The end point must call a function already defined in your Smart Contract app which will process the query request. The function name is part of the endpoint URL, or can be entered as the fcn parameter  when testing using the Sandbox. The function arguments (number of arguments and type) is determined by the Smart Contract. The Smart Contract is responsible for validation and exception management. For example, if testing the sample get-set Smart Contract app, enter ‘get’ (without quotes) as the value for fcn.   The response body is also determined by the Smart Contract app, and that’s also the reason why a consistent response sample is unavailable for this end point. A success response may be either 200 or 202. For more details refer to Synchronous vs Asynchronous Calls. In contrast to Invoke, the Query end point will often return fast even when called in Synchronous mode  Required permission: read (\"Access\":\"rw\" or \"Access\":\"r\")

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
 To query chaincode call query method
 function name is required argument and args is a required keyword argument
 timeout is an optional keyword argument
```
fcn = 'set'
args = ["args1","args2"]
app_query = xooa_client.query(fcn, args = args, timeout=5000)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fcn** | **str**| The blockchain Smart Contract app function name to call | 
 **args** | **str**| Argument(s) to pass to the blockchain Smart Contract app function. example - [\&quot;arg1\&quot;,\&quot;arg2\&quot;] | [optional] 
 **async** | **str**| Call this request asynchronously without waiting for response | [optional] 
 **timeout** | **str**| Request timeout in millisecond | [optional] 


### Authorization

Authorization required

### HTTP request headers