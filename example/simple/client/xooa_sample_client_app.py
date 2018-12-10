#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.path.append('..')
# Import XooaClient Library
from xooa_api.api_client import XooaClient
# Create an instance of XooaClient
foo = XooaClient()
# Set API Token
foo.set_api_token('<YOUR_TOKEN_HERE>')
#Validate Token
foo.validate()


# In[ ]:


# To invoke chaincode call invoke method
# function name is required argument and data is a required keyword argument
# timeout is an optional keyword argument
fcn = 'set'
args = {"args":["args1","args2"]}
app_invoke = foo.invoke(fcn, data=args, timeout=5000)
print(app_invoke)


# In[ ]:


# To invoke chaincode asynchronously, call invoke_async method
# function name is required argument and data is a required keyword  that needs to be a key value pair
fcn = 'set'
args = {"args":["args1","args2"]}
app_invoke_async = foo.invoke_async(fcn, data=args)
print(app_invoke_async)


# In[ ]:


# To query chaincode call query method
# function name is required argument and args is a required keyword argument
# timeout is an optional keyword argument
fcn = 'set'
args = ["args1","args2"]
app_query = foo.query(fcn, args = args, timeout=5000)
print(app_query['payload'])


# In[ ]:


# To query chaincode asynchronously call query method
# function name is required argument and args is a required keyword argument
fcn = 'set'
args = ["args1","args2"]
app_query_async = foo.query_async(fcn, args = args)
print(app_query_async)


# In[ ]:


# To get blockchain data call get_block_by_number method
# block_number is required argument
# timeout is an optional keyword argument
block_number = 2
app_block_by_number = foo.get_block_by_number(block_number, timeout=3000)
print(app_block_by_number)


# In[ ]:


# To get blockchain data asynchronously call get_block_by_number_async method
# block_number is required argument
block_number = 2
app_block_by_number_async = foo.get_block_by_number_async(block_number)
print(app_block_by_number_async)


# In[ ]:


# To get blockchain height call get_current_block method
# timeout is an optional keyword argument
app_current_block = foo.get_current_block(timeout=3000)
print(app_current_block)


# In[ ]:


# To get blockchain height asynchronously call get_current_block_async method
app_current_block_async = foo.get_current_block_async()
print(app_current_block_async)


# In[ ]:


# To get identity information call current_identity method
app_current_identity = foo.current_identity()
print(app_current_identity)


# In[ ]:


# To get all the identities information call get_identities method
app_get_identities = foo.get_identities()
print(app_get_identities)


# In[ ]:


# To enroll an identity call enroll_identity method
# data is required keyword argument

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
app_enroll_identity = foo.enroll_identity(data=enroll_identity_data)
print(app_enroll_identity)


# In[ ]:


# To enroll an identity asynchronously call enroll_identity method
# data is required keyword argument

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
app_enroll_identity_async = foo.enroll_identity_async(data=enroll_identity_data)
print(app_enroll_identity_async)


# In[ ]:


# To regenerate identity api token call regenerate_identity_api_token method
# identity is required argument

identity = '<IDENTITY>'
app_regenerate_identity_api_token = foo.regenerate_identity_api_token(identity)
print(app_regenerate_identity_api_token)


# In[ ]:


# To delete identity delete_identity method
# identity is required argument

identity = '<IDENTITY>'
app_delete_identity = foo.delete_identity(identity)
print(app_delete_identity)


# In[ ]:


# To delete identity asynchronously delete_identity_async method
# identity is required argument

identity = '<IDENTITY>'
app_delete_identity_async = foo.delete_identity_async(identity)
print(app_delete_identity_async)


# In[ ]:


# To get identity call get_identity method
# identity is required argument

identity = '<IDENTITY>'
app_get_identity = foo.get_identity(identity)
print(app_get_identity)


# In[ ]:


# To check whether the transaction has been completed or not, call get_result method
# result_id is required argument

result_id = '<RESULT_ID>'
app_get_result = foo.get_result(result_id)
print(app_get_result)


# In[ ]:


# To subscribe to events call subscribe_all_events method
# callback_on_event is required argument. It is an event handler.

callback_on_event = 'callback_on_event'
app_subscribe_events = foo.subscribe_all_events(callback_on_event)
print(app_subscribe_events)


# In[ ]:



