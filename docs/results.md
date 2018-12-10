All URIs are relative to *https://api.ci.xooa.io/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**result**](ResultApi.md#result) | **GET** /results/{ResultId} | Fetch result of previously submitted transaction


Fetch result of previously submitted transaction

API Returns result of previously submitted transaction

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

 To check whether the transaction has been completed or not, call get_result method
 result_id is required argument

```
result_id = '<RESULT_ID>'
app_get_result = xooa_client.get_result(result_id)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| Returned in previous Query/Invoke/Participant Operation | 

### Authorization

Authorization required
