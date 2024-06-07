## About the connector
The IBM IAM Identity Service API is used to manage service IDs, API key identities, trusted profiles, account security settings and to create IAM access tokens for a user or service ID.
<p>This document provides information about the IBM IAM Connector, which facilitates automated interactions, with a IBM IAM server using FortiSOAR&trade; playbooks. Add the IBM IAM Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with IBM IAM.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Contributors: Jitesh Rathod

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-ibm-iam`

## Prerequisites to configuring the connector
- You must have the URL of IBM IAM server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the IBM IAM server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>IBM IAM</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the IBM IAM server to connect and perform automated operations.<br>
<tr><td>API key<br></td><td>Enter your IBM Cloud API key.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>
## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get API Keys</td><td>Retrieves the list of API key details for a given service or user IAM ID and account ID.</td><td>get_api_keys <br/>Investigation</td></tr>
<tr><td>Create An API Key</td><td>Creates an API key for a UserID or service ID. Users can manage user API keys for themself, or service ID API keys for service IDs they have access to</td><td>create_an_api_key <br/>Investigation</td></tr>
<tr><td>Get API Key Details By Value</td><td>Retrieves the details of an API key by its value.</td><td>get_api_key_details_by_value <br/>Investigation</td></tr>
<tr><td>Get API Key Details</td><td>Retrieves the details information of an API key</td><td>Get_api_key_details <br/>Investigation</td></tr>
<tr><td>Update API Key</td><td>Updates an API key using a UserID or service ID.</td><td>update_api_key <br/>Investigation</td></tr>
<tr><td>Delete API Key</td><td>Deletes an API key.</td><td>delete_api_key <br/>Investigation</td></tr>
<tr><td>Lock API Key</td><td>Lock an API key by ID.</td><td>lock_api_key <br/>Investigation</td></tr>
<tr><td>UnLock API Key</td><td>Un-Lock an API key by ID.</td><td>unlock_api_key <br/>Investigation</td></tr>
<tr><td>Disable the API key</td><td>Disable an API key.</td><td>disable_the_api_key <br/>Investigation</td></tr>
<tr><td>Enable the API key</td><td>Enable an API key.</td><td>enable_the_api_key <br/>Investigation</td></tr>
<tr><td>List Service IDs By Name</td><td>Returns a list of service IDs. Users can manage user API keys for themself, or service ID API keys for service IDs they have access.</td><td>list_service_id_by_name <br/>Investigation</td></tr>
<tr><td>List Service IDs</td><td>Retrieves a list of service IDs. Users can manage user API keys for themself, or service ID API keys for service IDs they have access.</td><td>list_service_id_by_account_id <br/>Investigation</td></tr>
<tr><td>Create A Service ID</td><td>Creates a service ID for an IBM Cloud account. Users can manage user API keys for themself, or service ID API keys for service IDs.</td><td>create_a_service_id <br/>Investigation</td></tr>
<tr><td>Update Service ID</td><td>Updates properties of a service ID.</td><td>update_service_id <br/>Investigation</td></tr>
<tr><td>Delete Service ID and Associated API keys</td><td>Deletes a service ID and all API keys associated to it. Before deleting the service ID, all associated API keys are deleted. </td><td>delete_service_id_and_associated_api_keys <br/>Investigation</td></tr>
<tr><td>Lock The Service ID</td><td>Locks a service ID by ID. Users can manage user API keys for themself, or service ID API keys for service IDs </td><td>lock_service_id <br/>Investigation</td></tr>
<tr><td>Unlock The Service ID</td><td>Unlocks a service ID by ID. Users can manage user API keys for themself, or service ID API keys for service IDs </td><td>unlock_service_id <br/>Investigation</td></tr>
<tr><td>Get Account Configurations</td><td>Retrieves the details of an account's configuration.</td><td>get_account_configurations <br/>Investigation</td></tr>
<tr><td>Update Account Configurations</td><td>Allows a user to configure settings on their account with regards to MFA, MFA exempted list, session lifetimes, access control for creating new identities, and enforcing IP restrictions on token creation.</td><td>update_account_configurations <br/>Investigation</td></tr>
<tr><td>Trigger Activity Report</td><td>Trigger activity report for the account by specifying the account ID. It can take a few minutes to generate the report for retrieval.</td><td>trigger_activity_report_for_the_account <br/>Investigation</td></tr>
<tr><td>Get Activity Report</td><td>Get activity report for the account by specifying the account ID and the reference that is generated by triggering the report. Reports older than a day are deleted when generating a new report.</td><td>get_activity_report_for_the_account <br/>Investigation</td></tr>
</tbody></table>

### operation: Get API Keys
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Account ID</td><td>Specify the Account ID of the API keys to query.
</td></tr><tr><td>IAM ID</td><td>Specify the IAM ID of the API keys to be queried.
</td></tr><tr><td>Page Size</td><td>Optional size of a single page. Default is 20 items per page. Valid range is 1 to 100.
</td></tr><tr><td>Page Token</td><td>Optional Prev or Next page token returned from a previous query execution. Default is start with first page.
</td></tr><tr><td>Scope</td><td>Select the scope of the queried API keys. Can be 'entity' (default) or 'account'.
</td></tr><tr><td>Type</td><td>Select the type of the queried API keys. Can be 'user' or 'serviceid'.
</td></tr><tr><td>Sort</td><td>Select the following input parameter to sort the API keys.
</td></tr><tr><td>Order</td><td>Select the sort order, valid values are asc and desc. Default: asc.
</td></tr><tr><td>Include History</td><td>If this parameter is checked, then the entity history is included in the response.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "limit": "",
    "first": "",
    "next": "",
    "apikeys": {
        "id": "",
        "entity_tag": "",
        "crn": "",
        "locked": "",
        "disabled": "",
        "created_at": "",
        "created_by": "",
        "modified_at": "",
        "support_sessions": "",
        "action_when_leaked": "",
        "name": "",
        "description": "",
        "iam_id": "",
        "account_id": ""
    }
}</pre>
### operation: Create An API Key
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Account ID</td><td>Specify the account ID of the API key.
</td></tr><tr><td>Name</td><td>Specify the name of the API key if it is not checked for uniqueness. Therefore, multiple names with the same value can exist. Access is done via the UUID of the API key.
</td></tr><tr><td>IAM ID</td><td>Specify the IAM ID that the API key authenticates
</td></tr><tr><td>Description</td><td>Specify the description of the API key. The 'description' property is only available if a description was provided during a create of an API key.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "id": "",
    "entity_tag": "",
    "crn": "",
    "locked": "",
    "disabled": "",
    "created_at": "",
    "created_by": "",
    "modified_at": "",
    "support_sessions": "",
    "action_when_leaked": "",
    "name": "",
    "description": "",
    "iam_id": "",
    "account_id": "",
    "apikey": ""
}</pre>
### operation: Get API Key Details By Value
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>IAM ApiKey</td><td>Provide value of the API key
</td></tr><tr><td>Include History</td><td>If this parameter is selected, the entity history will be included in the response. Default: false.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "id": "",
    "entity_tag": "",
    "crn": "",
    "locked": "",
    "disabled": "",
    "created_at": "",
    "created_by": "",
    "modified_at": "",
    "support_sessions": "",
    "action_when_leaked": "",
    "name": "",
    "description": "",
    "iam_id": "",
    "account_id": ""
}</pre>
### operation: Get API Key Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Api Key Unique ID</td><td>Specify the Unique ID of the API key.
</td></tr><tr><td>Include History</td><td>If this parameter is selected, the entity history will be included in the response. Default: false.
</td></tr><tr><td>Include Activity</td><td>If this parameter is selected, the entity's activity is included in the response. Retrieving activity data is an expensive operation, so only request this when needed Default: false.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "id": "",
    "entity_tag": "",
    "crn": "",
    "locked": "",
    "disabled": "",
    "created_at": "",
    "created_by": "",
    "modified_at": "",
    "support_sessions": "",
    "action_when_leaked": "",
    "name": "",
    "description": "",
    "iam_id": "",
    "account_id": ""
}</pre>
### operation: Update API Key
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Entity Tag</td><td>Specify the version that you retrieved when reading the API key.
</td></tr><tr><td>Api Key Unique ID</td><td>Specify the Unique ID of the API key.
</td></tr><tr><td>Name</td><td>Specify the name is not checked for uniqueness. Therefore multiple names with the same value can exist. Access is done via the UUID of the API key.
</td></tr><tr><td>Description</td><td>Optional description of the API key. The 'description' property is only available if a description was provided during a create of an API key.
</td></tr><tr><td>Support Sessions</td><td>Define if the API key supports sessions.
</td></tr><tr><td>Action When Leaked</td><td>Select the action to take when API key is leaked, valid values are 'none', 'disable' and 'delete'.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "id": "",
    "entity_tag": "",
    "crn": "",
    "locked": "",
    "disabled": "",
    "created_at": "",
    "created_by": "",
    "modified_at": "",
    "support_sessions": "",
    "action_when_leaked": "",
    "name": "",
    "description": "",
    "iam_id": "",
    "account_id": ""
}</pre>
### operation: Delete API Key
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Api Key Unique ID</td><td>Specify the Unique ID of the API key.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "Status": "",
    "API Key Status": "",
    "API Key ID": ""
}</pre>
### operation: Lock API Key
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Api Key Unique ID</td><td>Specify the Unique ID of the API key.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "Status": "",
    "API Key Status": "",
    "API Key ID": ""
}</pre>
### operation: UnLock API Key
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Api Key Unique ID</td><td>Specify the Unique ID of the API key.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "Status": "",
    "API Key Status": "",
    "API Key ID": ""
}</pre>
### operation: Disable the API key
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Api Key Unique ID</td><td>Specify the Unique ID of the API key.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "Status": "",
    "API Key Status": "",
    "API Key ID": ""
}</pre>
### operation: Enable the API key
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Api Key Unique ID</td><td>Specify the Unique ID of the API key.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "Status": "",
    "API Key Status": "",
    "API Key ID": ""
}</pre>
### operation: List Service IDs By Name
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Account ID</td><td>Specify Account ID of the service ID(s) to query.
</td></tr><tr><td>Name</td><td>Specify name of the service ID(s) to query. Optional.20 items per page.
</td></tr><tr><td>Page Size</td><td>Optional size of a single page. Default is 20 items per page. Valid range is 1 to 100.
</td></tr><tr><td>Page Token</td><td>Optional Prev or Next page token returned from a previous query execution. Default is start with first page.
</td></tr><tr><td>Sort</td><td>Optional parameter to filter the type of the queried API keys. Can be 'user' or 'serviceid'.
</td></tr><tr><td>Order</td><td>Optional sort order, valid values are asc and desc. Default: asc.
</td></tr><tr><td>Include History</td><td>If this parameter is checked, then the entity history is included in the response.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "offset": "",
    "limit": "",
    "first": "",
    "next": "",
    "serviceids": {
        "id": "",
        "iam_id": "",
        "entity_tag": "",
        "crn": "",
        "locked": "",
        "created_at": "",
        "modified_at": "",
        "account_id": "",
        "name": "",
        "description": "",
        "unique_instance_crns": []
    }
}</pre>
### operation: List Service IDs
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Account ID</td><td>Specify Account ID of the service ID(s) to query.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "offset": "",
    "limit": "",
    "first": "",
    "next": "",
    "serviceids": {
        "id": "",
        "iam_id": "",
        "entity_tag": "",
        "crn": "",
        "locked": "",
        "created_at": "",
        "modified_at": "",
        "account_id": "",
        "name": "",
        "description": "",
        "unique_instance_crns": []
    }
}</pre>
### operation: Create A Service ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Account ID</td><td>Specify Account ID of the service ID(s) to query.
</td></tr><tr><td>Name</td><td>Specify the name is not checked for uniqueness. Therefore multiple names with the same value can exist. Access is done via the UUID of the API key.
</td></tr><tr><td>Description</td><td>Specify the description of the service ID to create.
</td></tr><tr><td>Unique Instance CRNs</td><td>Provides CSV list of the CRNs which point to the services connected to this service ID.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "id": "",
    "entity_tag": "",
    "crn": "",
    "locked": "",
    "disabled": "",
    "created_at": "",
    "created_by": "",
    "modified_at": "",
    "support_sessions": "",
    "action_when_leaked": "",
    "name": "",
    "description": "",
    "iam_id": "",
    "account_id": "",
    "apikey": ""
}</pre>
### operation: Update Service ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Service ID</td><td>Unique ID of the service ID to be updated.
</td></tr><tr><td>Name</td><td>Specify the name is not checked for uniqueness. Therefore multiple names with the same value can exist. Access is done via the UUID of the API key.
</td></tr><tr><td>Description</td><td>Specify the description of the service ID to update. If specified an empty description will clear the description of the service ID. If an non empty value is provided the service ID will be updated.
</td></tr><tr><td>Unique Instance CRNs</td><td>Provides CSV list of CRNs which point to the services connected to this service ID.
</td></tr><tr><td>Entity Tag</td><td>Specify the version that you retrieved when reading the service ID.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "iam_id": "",
    "entity_tag": "",
    "crn": "",
    "locked": "",
    "created_at": "",
    "modified_at": "",
    "account_id": "",
    "name": "",
    "description": "",
    "unique_instance_crns": []
}</pre>
### operation: Delete Service ID and Associated API keys
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Service ID</td><td>Unique ID of the service ID to be updated.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "id": "",
    "iam_id": "",
    "entity_tag": "",
    "crn": "",
    "locked": "",
    "created_at": "",
    "modified_at": "",
    "account_id": "",
    "name": "",
    "description": "",
    "unique_instance_crns": []
}</pre>
### operation: Lock The Service ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Service ID</td><td>specify the Unique ID of the service ID to be locked.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "Status": "",
    "API Key Status": "",
    "API Key ID": ""
}</pre>
### operation: Unlock The Service ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Service ID</td><td>Specify the Unique ID of the service ID to be Unlock.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "Status": "",
    "API Key Status": "",
    "API Key ID": ""
}</pre>
### operation: Get Account Configurations
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Account ID</td><td>specify the Account ID of the service ID(s) to obtain account configuration-related information
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "account_id": "",
    "restrict_create_service_id": "",
    "restrict_create_platform_apikey": "",
    "entity_tag": "",
    "mfa": "",
    "user_mfa": {
        "iam_id": "",
        "mfa": ""
    },
    "session_expiration_in_seconds": "",
    "session_invalidation_in_seconds": "",
    "max_sessions_per_identity": "",
    "system_access_token_expiration_in_seconds": "",
    "system_refresh_token_expiration_in_seconds": ""
}</pre>
### operation: Update Account Configurations
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Entity Tag</td><td>Specify the version that you want to update.
</td></tr><tr><td>Account ID</td><td>Specify Account ID of the service ID(s) to update the account configurations.
</td></tr><tr><td>Restrict Create Service ID</td><td>Select the action to take when service id is leaked, valid values are 'RESTRICTED', 'NOT_RESTRICTED' and 'NOT_SET'.
</td></tr><tr><td>Restrict Create Platform Api key</td><td>Select the action to take when  API keys is leaked, valid values are 'RESTRICTED', 'NOT_RESTRICTED' and 'NOT_SET'.
</td></tr><tr><td>Allowed IP Addresses</td><td>Defines the IP addresses and subnets from which IAM tokens can be created for the account.
</td></tr><tr><td>MFA</td><td>Select the action to mfa trait for the account valid values are 'NONE', 'NONE_NO_ROPC', 'TOTP, 'TOTP4ALL','LEVEL1', 'LEVEL2', 'LEVEL3
</td></tr><tr><td>User MFA</td><td>Provides a users that are exempted from the MFA requirement of the account.
</td></tr><tr><td>Session Expiration In Seconds</td><td>Provides the session expiration in seconds for the account.
</td></tr><tr><td>Session Invalidation In Seconds</td><td>Provides the period of time in seconds in which a session will be invalidated due to inactivity.
</td></tr><tr><td>Max Sessions Per Identity</td><td>Provides the max allowed sessions per identity required by the account.
</td></tr><tr><td>System Access Token Expiration In Seconds</td><td>Provides the access token expiration in seconds.
</td></tr><tr><td>System Refresh Token Expiration In Seconds</td><td>Provides the refresh token expiration in seconds.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "account_id": "",
    "restrict_create_service_id": "",
    "restrict_create_platform_apikey": "",
    "entity_tag": "",
    "mfa": "",
    "user_mfa": {
        "iam_id": "",
        "mfa": ""
    },
    "session_expiration_in_seconds": "",
    "session_invalidation_in_seconds": "",
    "max_sessions_per_identity": "",
    "system_access_token_expiration_in_seconds": "",
    "system_refresh_token_expiration_in_seconds": ""
}</pre>
### operation: Trigger Activity Report
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Account ID</td><td>Specify Account ID of the service ID(s) to query.
</td></tr><tr><td>Type</td><td>Optional the supported value is 'inactive'. List all identities that have not authenticated within the time indicated by duration.
</td></tr><tr><td>Duration</td><td>Optional duration of the report. The supported unit of duration is hours.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "reference": ""
}</pre>
### operation: Get Activity Report
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Account ID</td><td>Specify Account ID of the service ID(s) to query.
</td></tr><tr><td>Reference</td><td>Specify reference for the report to be generated, You can use 'latest' to get the latest report for the given account.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<pre>{
    "created_by": "",
    "reference": "",
    "report_duration": "",
    "report_start_time": "",
    "report_end_time": "",
    "users": {
        "iam_id": "",
        "name": "",
        "username": "",
        "email": "",
        "last_authn": ""
    },
    "serviceids": {
        "id": "",
        "name": "",
        "last_authn": ""
    },
    "profiles": {
        "id": "",
        "name": "",
        "last_authn": ""
    },
    "apikeys": [
        {
            "id": "",
            "name": "",
            "type": "",
            "serviceid": {
                "id": "",
                "name": ""
            },
            "last_authn": ""
        },
        {
            "id": "",
            "name": "",
            "type": "",
            "user": {
                "iam_id": "",
                "name": "",
                "username": "",
                "email": ""
            },
            "last_authn": ""
        }
    ]
}</pre>
