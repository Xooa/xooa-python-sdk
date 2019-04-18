# XooaClient

The official Xooa SDK for Python to connect with the Xooa PaaS.

- API version: v1
- Package version: 1.0.0

This SDK refers to smart contract APIs available for Xooa platform. For more details, refer: <https://api.xooa.com/explorer>

Note: XLDB and asset management APIs are not included in the SDK.

The platform documentation is available at <https://docs.xooa.com>

## Requirements.

Python 3.4+

## Installation & Usage
### pip install

You can download directly from Github repo or you can use pip to install 

```sh
pip install git+https://github.com/Xooa/xooa-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import xooa_api.api_client
```


## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

### Example
Create an instance of XooaClient
```
import xooa_api.api_client import XooaClient
xooa_client = XooaClient()
```

Set API token and Validate
```api_token = '<API_TOKEN>' 
set_api_token = xooa_client.set_api_token(api_token)
validate = xooa_client.validate()
```
 To invoke chaincode call invoke method
 function name is required argument and data is a required keyword argument which needs to be key value pair.
 timeout is an optional keyword argument
```fcn = 'set'
args = {"args":["args1","args2"]}
app_invoke = xooa_client.invoke(fcn, data=args, timeout=5000)
```
## Documentation For Authorization

 All endpoints require authorization.


## Author

support@xooa.com
