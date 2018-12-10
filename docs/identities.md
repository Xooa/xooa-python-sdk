All URIs are relative to *https://api.ci.xooa.io/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticated_identity_information**](IdentitiesApi.md#authenticated_identity_information) | **GET** /identities/me/ | Authenticated Identity Information
[**delete_identity**](IdentitiesApi.md#delete_identity) | **DELETE** /identities/{Id} | Delete Identity
[**enrollment**](IdentitiesApi.md#enrollment) | **POST** /identities/ | Enroll Identity
[**identities_get_all_identities**](IdentitiesApi.md#identities_get_all_identities) | **GET** /identities/ | Get All Identities
[**identity_information**](IdentitiesApi.md#identity_information) | **GET** /identities/{Id} | Identity Information
[**regenerate_token**](IdentitiesApi.md#regenerate_token) | **POST** /identities/{Id}/regeneratetoken | Regenerate Identity API Token


# **authenticated_identity_information**
> authenticated_identity_information()

Authenticated Identity Information

This End Point Returns Information about the Authenticated Identity

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
To get identity information call current_identity method
```
app_current_identity = xooa_client.current_identity()
```

### Parameters
This endpoint does not need any parameter.

### Authorization

Authorization required


# **delete_identity**
> delete_identity(id, async=async, timeout=timeout)

Delete Identity

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
 To delete identity delete_identity method
 identity is required argument

```
identity = '<APP_ID>'
app_delete_identity = xooa_client.delete_identity(identity)
```

 To delete identity asynchronously delete_identity_async method
 identity is required argument

```
identity = '<APP_ID>'
app_delete_identity_async = xooa_client.delete_identity_async(identity)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identity Id | 
 **async** | **str**| Call this request asynchronously without waiting for response | [optional] 
 **timeout** | **str**| Request timeout in millisecond | [optional] 

### Authorization

Authorization required

# **enrollment**
> enrollment(async=async, timeout=timeout)

Enroll Identity

The Enroll Identity end point is used to  enroll new identities for the Smart Contract app.  A success response includes the API Key generated for the identity. This API Key can be used to call API End points on behalf of the enrolled identity. This End Point provides equivalent functionality to adding new identity manually using Xooa console, and identities added using this end point will appear, and can be managed, using Xooa console under the identities tab of the Smart Contract app Required permission: manage identities (canManageIdentities=true)

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
 To enroll an identity call enroll_identity method
 data is required keyword argument

```
identity_data = {
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
app_enroll_identity = xooa_client.enroll_identity(data=identity_data)
```
To enroll an identity asynchronously call enroll_identity method
data is required keyword argument

```
identity_data = {
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
app_enroll_identity_async = xooa_client.enroll_identity_async(data=identity_data)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async** | **str**| Call this request asynchronously without waiting for response | [optional] 
 **timeout** | **str**| Request timeout | [optional] 

### Authorization

Authorization required


# **identities_get_all_identities**
> identities_get_all_identities()

Get All Identities

Get all identities from the identity registry

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

To get all the identities information call get_identities method
```
app_get_identities = xooa_client.get_identities()
```

### Parameters
This endpoint does not need any parameter.

### Authorization

Authorization required


# **identity_information**
> identity_information(id)

Identity Information

Get the specified identity from the identity registry

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

To get all the identities information call get_identities method
```
app_get_identities = xooa_client.get_identities()
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identity Id | 

### Authorization

Authorization required

# **regenerate_token**
> regenerate_token(id)

Regenerate Identity API Token

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
 To regenerate identity api token call regenerate_identity_api_token method
 identity is required argument

```
identity = '<APP_ID>'
app_regenerate_identity_api_token = xooa_client.regenerate_identity_api_token(identity)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identity Id | 

### Authorization

Authorization required
