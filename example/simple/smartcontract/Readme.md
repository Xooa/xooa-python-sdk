# Xooa Get-Set Smart Contract

This page provides an overview to Xooa Get-Set smart contract functionalities.



## Overview

This smart contract provides 2 functions:
  
  * Get
  * Set

#### Get

Get method is used to fetch values associated with the key passed in the arguments.

If get method is invoked with a single key it will return either a 200 response with the state of the key or a 404 response if the key does not exist in the blockchain.

If get method is invoked with multiple keys it will return a 400 Bad Request error response.


#### Set

Set method is used to store the key value pairs in the ledger.

If set method is called with two arguments they are taken up as key value pair and are stored in the ledger. A response with the key value pair in result is returned.

If set method is called with any number of arguments other than 2 it returns a 400 Bad Request error response.



## Deploy the Xooa-Python Get-Set smart contract 
 
1. Log in to the Xooa blockchain console at https://xooa.com/blockchain.

2. Go to **Apps** > **Deploy New**. If you didn't log in with your GitHub account, you will need to do it now.

3. Find the Github repository **xooa/xooa-python-sdk** with the smart contract. Tap **Select**, and then **Next**.
   > For accesing **Private Git Repos**, click or tap **Authorize Private Github Access**.

4. Select the Smart Contract **Xooa-Python** to deploy, and then click **Deploy**.

5. Relax:  Xooa is doing the blockchain heavy lifting. You will be redirected to app dashboard when the deployment completes.

6. Record the **API Token** when it is shown: you will need it to authorize API requests from Python SDK. API Token cannot be dispalyed after you closed the window, but it may get regenerated. 
   > **Tip:**  to regenerate the API token: 
   >
   > 1. Go to the **Identities** tab in the App. 
   > 2. Next to the ID, select **Actions**.
   > 3. Select **Regenerate API Token**, and then select **Generate**.


