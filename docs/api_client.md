# XooaClient
List of Xooa Blockchain Methods

The methods included in XooaClient are:

-set_api_token

-set_url

-validate

-invoke

-invoke_async

-query

-query_async

-get_block_by_number

-get_block_by_number_async

-get_current_block

-get_current_block_async

-current_identity

-get_identity

-get_identities

-enroll_identity

-enroll_identity_async

-regenerate_identity_api_token

-delete_identity

-delete_identity_async

-get_result

-subscribe_all_events

-unsubscribe

-callback_on_event

-set_logging_level


### Example
Create an instance of XooaClient
```import xooa_api.api_client import XooaClient
xooa_client = XooaClient()
```
Set API token
```
api_token = '<API_TOKEN>'
validate_app = xooa_client.set_api_token(api_token)
```
To invoke chaincode call invoke method
function name is required argument and data is a required keyword argument
timeout is an optional keyword argument

```
fcn = 'set'
args = {"args":["args1","args2"]}
```
## Documentation For Authorization

 All endpoints require authorization.
