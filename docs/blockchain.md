# BlockchainApi

All URIs are relative to *https://api.ci.xooa.io/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**block_data**](BlockchainApi.md#block_data) | **GET** /block/{BlockNumber} | Get block data (block #)
[**block_height**](BlockchainApi.md#block_height) | **GET** /block/current | Get current blocks


# **block_data**
```
block_data(block_number, async=async, timeout=timeout)
```
Get block data (block #)

Get specific block information such as hash, # of transactions

### Example
Create an instance of XooaClient
```
import xooa_api.api_client import XooaClient
xooa_client = XooaClient()
```
Set API token and Validate
```
api_token = '<API_TOKEN>' #check for your api token
set_api_token = xooa_client.set_api_token(api_token)
validate = self.validate()
```

To get blockchain data call get_block_by_number method
block_number is required argument
timeout is an optional keyword argument
```
block_number = 2
app_block_by_number = xooa_client.get_block_by_number(block_number, timeout=3000)
```
block_number is required argument
```
block_number = 2
app_block_by_number_async = xooa_client.get_block_by_number_async(block_number)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_number** | **str**| Block number to fetch data | 
 **async** | **str**| Call this request asynchronously without waiting for response | [optional] 
 **timeout** | **str**| Request timeout in millisecond | [optional] 

### Authorization

Authorization required

# **block_height**
Get current blocks

Get current blocks in the network

Get specific block information such as hash, # of transactions

### Example
Create an instance of XooaClient
```
import xooa_api.api_client import XooaClient
xooa_client = XooaClient()
```
Set API token and Validate
```
api_token = '<API_TOKEN>' #check for your api token
set_api_token = xooa_client.set_api_token(api_token)
validate = self.validate()
```
To get blockchain height call get_current_block method
timeout is an optional keyword argument
```
app_current_block = xooa_client.get_current_block(timeout=3000)
```
To get blockchain height asynchronously call get_current_block_async method
```
app_current_block_async = xooa_client.get_current_block_async()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async** | **str**| Call this request asynchronously without waiting for response | [optional] 
 **timeout** | **str**| Request timeout in millisecond | [optional] 

### Authorization

Authorization required