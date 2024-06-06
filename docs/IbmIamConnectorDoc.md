## About the connector
The IBM IAM Identity Service API is used to manage service IDs, API key identities, trusted profiles, account security settings and to create IAM access tokens for a user or service ID.
<p>This document provides information about the IBM IAM Connector, which facilitates automated interactions, with a IBM IAM server using FortiSOAR&trade; playbooks. Add the IBM IAM Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with IBM IAM.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-ibm-iam`

## Prerequisites to configuring the connector
- You must have the URL of IBM IAM server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the IBM IAM server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>IBM IAM</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the IBM IAM server to connect and perform automated operations.<br>
<tr><td>API key<br></td><td>Enter your IBM Cloud API key.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get API Keys By IAM ID & Account ID<br></td><td>Returns the list of API key details for a given service or user IAM ID and account ID.<br></td><td>get_api_keys_by_iam_id_and_account_id <br/>Investigation<br></td></tr>
<tr><td>Create An API Key<br></td><td>Creates an API key for a UserID or service ID. Users can manage user API keys for themself, or service ID API keys for service IDs they have access to<br></td><td>create_an_api_key <br/>Investigation<br></td></tr>
<tr><td>Get API Key Details By Value<br></td><td>Returns the details of an API key by its value.<br></td><td>get_api_key_details_by_value <br/>Investigation<br></td></tr>
<tr><td>Get API Key Details<br></td><td>Returns the details of an API key<br></td><td>Get_api_key_details <br/>Investigation<br></td></tr>
<tr><td>Update API Key<br></td><td>Creates an API key for a UserID or service ID.<br></td><td>update_api_key <br/>Investigation<br></td></tr>
<tr><td>Delete API Key<br></td><td>Deletes an API key.<br></td><td>delete_api_key <br/>Investigation<br></td></tr>
<tr><td>Lock API Key<br></td><td>Lock an API key by ID.<br></td><td>lock_api_key <br/>Investigation<br></td></tr>
<tr><td>UnLock API Key<br></td><td>Un-Lock an API key by ID.<br></td><td>unlock_api_key <br/>Investigation<br></td></tr>
<tr><td>Disable the API key<br></td><td>Disable an API key.<br></td><td>disable_the_api_key <br/>Investigation<br></td></tr>
<tr><td>Enable the API key<br></td><td>Enable an API key.<br></td><td>enable_the_api_key <br/>Investigation<br></td></tr>
<tr><td>List Service IDs By Name<br></td><td>Returns a list of service IDs. Users can manage user API keys for themself, or service ID API keys for service IDs they have access.<br></td><td>list_service_id_by_name <br/>Investigation<br></td></tr>
<tr><td>List Service IDs By Account ID<br></td><td>Returns a list of service IDs. Users can manage user API keys for themself, or service ID API keys for service IDs they have access.<br></td><td>list_service_id_by_account_id <br/>Investigation<br></td></tr>
<tr><td>Create A Service ID<br></td><td>Creates a service ID for an IBM Cloud account. Users can manage user API keys for themself, or service ID API keys for service IDs.<br></td><td>create_a_service_id <br/>Investigation<br></td></tr>
<tr><td>Update Service ID<br></td><td>Updates properties of a service ID.<br></td><td>update_service_id <br/>Investigation<br></td></tr>
<tr><td>Delete Service ID and Associated API keys<br></td><td>Deletes a service ID and all API keys associated to it. Before deleting the service ID, all associated API keys are deleted. <br></td><td>delete_service_id_and_associated_api_keys <br/>Investigation<br></td></tr>
<tr><td>Lock The Service ID<br></td><td>Locks a service ID by ID. Users can manage user API keys for themself, or service ID API keys for service IDs <br></td><td>lock_service_id <br/>Investigation<br></td></tr>
<tr><td>Unlock The Service ID<br></td><td>Unlocks a service ID by ID. Users can manage user API keys for themself, or service ID API keys for service IDs <br></td><td>unlock_service_id <br/>Investigation<br></td></tr>
<tr><td>Get Account Configurations<br></td><td>Returns the details of an account's configuration.<br></td><td>get_account_configurations <br/>Investigation<br></td></tr>
<tr><td>Update Account Configurations<br></td><td>Allows a user to configure settings on their account with regards to MFA, MFA excemption list, session lifetimes, access control for creating new identities, and enforcing IP restrictions on token creation.<br></td><td>update_account_configurations <br/>Investigation<br></td></tr>
<tr><td>Trigger Activity Report For The Account<br></td><td>Trigger activity report for the account by specifying the account ID. It can take a few minutes to generate the report for retrieval.<br></td><td>trigger_activity_report_for_the_account <br/>Investigation<br></td></tr>
<tr><td>Get Activity Report For The Account<br></td><td>Get activity report for the account by specifying the account ID and the reference that is generated by triggering the report. Reports older than a day are deleted when generating a new report.<br></td><td>get_activity_report_for_the_account <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get API Keys By IAM ID & Account ID
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Account ID<br></td><td>Specify the Account ID of the API keys to query.<br>
</td></tr><tr><td>IAM ID<br></td><td>Specify the IAM ID of the API keys to be queried.<br>
</td></tr><tr><td>Page Size<br></td><td>Optional size of a single page. Default is 20 items per page. Valid range is 1 to 100.<br>
</td></tr><tr><td>Page Token<br></td><td>Optional Prev or Next page token returned from a previous query execution. Default is start with first page.<br>
</td></tr><tr><td>Scope<br></td><td>Optional parameter to define the scope of the queried API keys. Can be 'entity' (default) or 'account'.<br>
</td></tr><tr><td>Type<br></td><td>Optional parameter to filter the type of the queried API keys. Can be 'user' or 'serviceid'.<br>
</td></tr><tr><td>Sort<br></td><td>Optional parameter to filter the type of the queried API keys. Can be 'user' or 'serviceid'.<br>
</td></tr><tr><td>Order<br></td><td>Optional sort order, valid values are asc and desc. Default: asc.<br>
</td></tr><tr><td>Include History<br></td><td>Defines if the entity history is included in the response.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "limit": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "first": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "next": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "apikeys": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "entity_tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "crn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "locked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "disabled": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "created_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "modified_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "support_sessions": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "action_when_leaked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "account_id": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Create An API Key
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Account ID<br></td><td>Specify the account ID of the API key.<br>
</td></tr><tr><td>Name<br></td><td>Specify the name is not checked for uniqueness. Therefore multiple names with the same value can exist. Access is done via the UUID of the API key.<br>
</td></tr><tr><td>IAM ID<br></td><td>Specify the Specify  iam_id that this API key authenticates.<br>
</td></tr><tr><td>Description<br></td><td>Optional description of the API key. The 'description' property is only available if a description was provided during a create of an API key.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "entity_tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "crn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "locked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "disabled": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "modified_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "support_sessions": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "action_when_leaked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "account_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "apikey": ""
</code><code><br>}</code>

### operation: Get API Key Details By Value
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>IAM ApiKey<br></td><td>Pass the API key value for this API key.<br>
</td></tr><tr><td>Include History<br></td><td>Defines if the entity history is included in the response Default: false.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "entity_tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "crn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "locked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "disabled": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "modified_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "support_sessions": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "action_when_leaked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "account_id": ""
</code><code><br>}</code>

### operation: Get API Key Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Api Key Unique ID<br></td><td>Specify the Unique ID of the API key.<br>
</td></tr><tr><td>Include History<br></td><td>Defines if the entity history is included in the response Default: false.<br>
</td></tr><tr><td>Include Activity<br></td><td>Defines if the entity's activity is included in the response. Retrieving activity data is an expensive operation, so only request this when needed Default: false.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "entity_tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "crn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "locked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "disabled": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "modified_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "support_sessions": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "action_when_leaked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "account_id": ""
</code><code><br>}</code>

### operation: Update API Key
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Entity Tag<br></td><td>Specify the version that you retrieved when reading the API key.<br>
</td></tr><tr><td>Api Key Unique ID<br></td><td>Specify the Unique ID of the API key.<br>
</td></tr><tr><td>Name<br></td><td>Specify the name is not checked for uniqueness. Therefore multiple names with the same value can exist. Access is done via the UUID of the API key.<br>
</td></tr><tr><td>Description<br></td><td>Optional description of the API key. The 'description' property is only available if a description was provided during a create of an API key.<br>
</td></tr><tr><td>Support Sessions<br></td><td>Define if the API key supports sessions.<br>
</td></tr><tr><td>Action When Leaked<br></td><td>Select the action to take when API key is leaked, valid values are 'none', 'disable' and 'delete'.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "entity_tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "crn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "locked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "disabled": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "modified_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "support_sessions": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "action_when_leaked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "account_id": ""
</code><code><br>}</code>

### operation: Delete API Key
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Api Key Unique ID<br></td><td>Specify the Unique ID of the API key.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key ID": ""
</code><code><br>}</code>

### operation: Lock API Key
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Api Key Unique ID<br></td><td>Specify the Unique ID of the API key.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key ID": ""
</code><code><br>}</code>

### operation: UnLock API Key
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Api Key Unique ID<br></td><td>Specify the Unique ID of the API key.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key ID": ""
</code><code><br>}</code>

### operation: Disable the API key
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Api Key Unique ID<br></td><td>Specify the Unique ID of the API key.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key ID": ""
</code><code><br>}</code>

### operation: Enable the API key
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Api Key Unique ID<br></td><td>Specify the Unique ID of the API key.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key ID": ""
</code><code><br>}</code>

### operation: List Service IDs By Name
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Account ID<br></td><td>Specify Account ID of the service ID(s) to query.<br>
</td></tr><tr><td>Name<br></td><td>Specify name of the service ID(s) to query. Optional.20 items per page.<br>
</td></tr><tr><td>Page Size<br></td><td>Optional size of a single page. Default is 20 items per page. Valid range is 1 to 100.<br>
</td></tr><tr><td>Page Token<br></td><td>Optional Prev or Next page token returned from a previous query execution. Default is start with first page.<br>
</td></tr><tr><td>Sort<br></td><td>Optional parameter to filter the type of the queried API keys. Can be 'user' or 'serviceid'.<br>
</td></tr><tr><td>Order<br></td><td>Optional sort order, valid values are asc and desc. Default: asc.<br>
</td></tr><tr><td>Include History<br></td><td>Defines if the entity history is included in the response.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "offset": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "limit": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "first": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "next": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "serviceids": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "entity_tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "crn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "locked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "modified_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "account_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "unique_instance_crns": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: List Service IDs By Account ID
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Account ID<br></td><td>Specify Account ID of the service ID(s) to query.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "offset": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "limit": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "first": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "next": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "serviceids": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "entity_tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "crn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "locked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "modified_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "account_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "unique_instance_crns": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Create A Service ID
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Account ID<br></td><td>Specify Account ID of the service ID(s) to query.<br>
</td></tr><tr><td>Name<br></td><td>Specify the name is not checked for uniqueness. Therefore multiple names with the same value can exist. Access is done via the UUID of the API key.<br>
</td></tr><tr><td>Description<br></td><td>Optional description of the service ID to update. If specified an empty description will clear the description of the service ID. If an non empty value is provided the service ID will be updated.<br>
</td></tr><tr><td>Unique Instance CRNs<br></td><td>Optional CRNs which point to the services connected to this service ID.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "entity_tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "crn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "locked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "disabled": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "modified_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "support_sessions": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "action_when_leaked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "account_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "apikey": ""
</code><code><br>}</code>

### operation: Update Service ID
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Service ID<br></td><td>Unique ID of the service ID to be updated.<br>
</td></tr><tr><td>Name<br></td><td>Specify the name is not checked for uniqueness. Therefore multiple names with the same value can exist. Access is done via the UUID of the API key.<br>
</td></tr><tr><td>Description<br></td><td>Optional description of the service ID to update. If specified an empty description will clear the description of the service ID. If an non empty value is provided the service ID will be updated.<br>
</td></tr><tr><td>Unique Instance CRNs<br></td><td>Optional CRNs which point to the services connected to this service ID.<br>
</td></tr><tr><td>Entity Tag<br></td><td>Specify the version that you retrieved when reading the service ID.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "entity_tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "crn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "locked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "modified_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "account_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "unique_instance_crns": []
</code><code><br>}</code>

### operation: Delete Service ID and Associated API keys
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Service ID<br></td><td>Unique ID of the service ID to be updated.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "entity_tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "crn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "locked": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "modified_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "account_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "unique_instance_crns": []
</code><code><br>}</code>

### operation: Lock The Service ID
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Service ID<br></td><td>Unique ID of the service ID to be updated.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key ID": ""
</code><code><br>}</code>

### operation: Unlock The Service ID
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Service ID<br></td><td>Unique ID of the service ID to be updated.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "API Key ID": ""
</code><code><br>}</code>

### operation: Get Account Configurations
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Account ID<br></td><td>Specify Account ID of the service ID(s) to query.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "account_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "restrict_create_service_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "restrict_create_platform_apikey": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "entity_tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "mfa": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "user_mfa": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "mfa": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "session_expiration_in_seconds": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "session_invalidation_in_seconds": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "max_sessions_per_identity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "system_access_token_expiration_in_seconds": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "system_refresh_token_expiration_in_seconds": ""
</code><code><br>}</code>

### operation: Update Account Configurations
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Entity Tag<br></td><td>Specify the version that you retrieved when reading the API key.<br>
</td></tr><tr><td>Account ID<br></td><td>Specify Account ID of the service ID(s) to query.<br>
</td></tr><tr><td>Restrict Create Service ID<br></td><td>Select the action to take when service id is leaked, valid values are 'RESTRICTED', 'NOT_RESTRICTED' and 'NOT_SET'.<br>
</td></tr><tr><td>Restrict Create Platform Api key<br></td><td>Select the action to take when  API keys is leaked, valid values are 'RESTRICTED', 'NOT_RESTRICTED' and 'NOT_SET'.<br>
</td></tr><tr><td>Allowed IP Addresses<br></td><td>Defines the IP addresses and subnets from which IAM tokens can be created for the account.<br>
</td></tr><tr><td>MFA<br></td><td>Select the action to mfa trait for the account valid values are 'NONE', 'NONE_NO_ROPC', 'TOTP, 'TOTP4ALL','LEVEL1', 'LEVEL2', 'LEVEL3<br>
</td></tr><tr><td>User MFA<br></td><td>Defines users that are exempted from the MFA requirement of the account.<br>
</td></tr><tr><td>Session Expiration In Seconds<br></td><td>Defines the session expiration in seconds for the account.<br>
</td></tr><tr><td>Session Invalidation In Seconds<br></td><td>Defines the period of time in seconds in which a session will be invalidated due to inactivity. <br>
</td></tr><tr><td>Max Sessions Per Identity<br></td><td>Defines the max allowed sessions per identity required by the account.<br>
</td></tr><tr><td>System Access Token Expiration In Seconds<br></td><td>Defines the access token expiration in seconds.<br>
</td></tr><tr><td>System Refresh Token Expiration In Seconds<br></td><td>Defines the refresh token expiration in seconds.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "account_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "restrict_create_service_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "restrict_create_platform_apikey": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "entity_tag": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "mfa": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "user_mfa": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "mfa": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "session_expiration_in_seconds": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "session_invalidation_in_seconds": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "max_sessions_per_identity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "system_access_token_expiration_in_seconds": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "system_refresh_token_expiration_in_seconds": ""
</code><code><br>}</code>

### operation: Trigger Activity Report For The Account
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Account ID<br></td><td>Specify Account ID of the service ID(s) to query.<br>
</td></tr><tr><td>Type<br></td><td>Optional the supported value is 'inactive'. List all identities that have not authenticated within the time indicated by duration.<br>
</td></tr><tr><td>Duration<br></td><td>Optional duration of the report. The supported unit of duration is hours.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "reference": ""
</code><code><br>}</code>

### operation: Get Activity Report For The Account
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Account ID<br></td><td>Specify Account ID of the service ID(s) to query.<br>
</td></tr><tr><td>Reference<br></td><td>Specify reference for the report to be generated, You can use 'latest' to get the latest report for the given account.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "reference": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "report_duration": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "report_start_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "report_end_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "users": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "username": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "email": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "last_authn": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "serviceids": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "last_authn": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "profiles": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "last_authn": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "apikeys": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "serviceid": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "name": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "last_authn": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "user": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "iam_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "username": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "last_authn": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>
## Included playbooks
The `Sample - ibm-iam - 1.0.0` playbook collection comes bundled with the IBM IAM connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the IBM IAM connector.

- Get API Keys By IAM ID & Account ID
- Create An API Key
- Get API Key Details By Value
- Get API Key Details
- Update API Key
- Delete API Key
- Lock API Key
- UnLock API Key
- Disable the API key
- Enable the API key
- List Service IDs By Name
- List Service IDs By Account ID
- Create A Service ID
- Update Service ID
- Delete Service ID and Associated API keys
- Lock The Service ID
- Unlock The Service ID
- Get Account Configurations
- Update Account Configurations
- Trigger Activity Report For The Account
- Get Activity Report For The Account

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
