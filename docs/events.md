# Subscribe Events

All URIs are relative to *https://api.ci.xooa.io/*

 **Event handler**

Event Listener

Subscribe to the events and receive the event data

### Example
Create an instance of XooaClient

```
import xooa_api.api_client import XooaClient
xooa_client = XooaClient()
```

Set API token
```
api_token = '<API_TOKEN>'
validate_app = xooa_client.set_api_token(api_token)
```

To subscribe to events call subscribe_all_events method
callback_on_event is required argument. It is an event handler.

```
callback_on_event = 'callback_on_event'
app_subscribe_events = xooa_client.subscribe_all_events(callback_on_event)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_on_event** | **str**| callback function to handle data | 

### Authorization

Authorization required
