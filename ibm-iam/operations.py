"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from .ibm_iam_auth import *
from connectors.core.connector import get_logger, ConnectorError
import requests, json

logger = get_logger('ibm-iam')


def make_rest_call(endpoint, method, connector_info, config, headers=None, data=None, params=None):
    try:
        co = IBM(config)
        url = co.host + endpoint
        token = co.validate_token(config, connector_info)
        if headers is None:
            headers = {'Authorization': token, 'Content-Type': 'application/json'}
            
        else:
            key = list(headers.keys())[0]
            value = list(headers.values())[0]
            headers.update({'Authorization': token, 'Content-Type': 'application/json', key: value})
            
        logger.debug("Action Header: {0}".format(headers))
        logger.debug("Action Endpoint: {0}".format(url))
        response = requests.request(method, url, headers=headers, verify=co.verify_ssl, data=data, params=params)
        logger.debug("Action Response: {0}".format(response.status_code))
        if response.status_code in [200, 201, 202, 204]:
            if response.text != "":
                return response.json()
            else:
                return {}
        elif response.status_code == 404:
            return {'Not Found'}
        else:
            raise ConnectorError("Response: {0}: {1}".format(response.status_code, response.content))
    except requests.exceptions.SSLError:
        raise ConnectorError('SSL certificate validation failed')
    except requests.exceptions.ConnectTimeout:
        raise ConnectorError('The request timed out while trying to connect to the server')
    except requests.exceptions.ReadTimeout:
        raise ConnectorError(
            'The server did not send any data in the allotted amount of time')
    except requests.exceptions.ConnectionError:
        raise ConnectorError('Invalid endpoint or credentials')
    except Exception as err:
        raise ConnectorError(str(err))


def _check_health(config, connector_info):
    try:
        return check(config, connector_info)
    except Exception as err:
        logger.exception('Health check failed with: {0}'.format(err))
        raise ConnectorError('Health check failed with: {0}'.format(err))


def get_api_keys_by_iam_id_and_account_id(config, params, connector_info):
    try:
        query_params = {}
        keys_to_check = ['account_id', 'iam_id', 'pagesize', 'pagetoken', 'scope', 'type_value','sort', 'order', 'include_history']
    
        for key in keys_to_check:
            value = params.get(key)
            if value:
                query_params[key] = value

        query = '&'.join([f"{key}={val}" for key, val in query_params.items()])
        endpoints = f"/v1/apikeys?{query}"
        response = make_rest_call(endpoint=endpoints,
                                    method='GET',
                                    connector_info=connector_info,
                                    config=config)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def create_an_api_key(config, params, connector_info):
    try:
        payload = {
            'name': params.get('name'),
            'iam_id': params.get('iam_id'),
            'description': params.get('description'),
            'account_id': params.get('account_id'),
            'store_value': 'false'
        }
        endpoint = '/v1/apikeys'
        payload = {key: value for key, value in payload.items() if value is not None and value != ""}
        response = make_rest_call(endpoint=endpoint,
                                    method='POST',
                                    connector_info=connector_info,
                                    config=config,
                                    data=json.dumps(payload))
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def get_api_key_details_by_value(config, params, connector_info):
    try:
        iam_apiKey = params.get('iam_apiKey')
        headers = {'IAM-Apikey': iam_apiKey}
        param = {'include_history': params.get('include_history')}
        
        endpoint = f'/v1/apikeys/details'
        response = make_rest_call(endpoint=endpoint,
                                    method='GET',
                                    headers=headers,
                                    connector_info=connector_info,
                                    config=config,
                                    params=param)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def get_api_key_details(config, params, connector_info):
    try:
        api_key_unique_id = params.get('api_key_unique_id')
        include_history = params.get('include_history')
        include_activity = params.get('include_activity')
        param = {
            'include_history': include_history,
            'include_activity': include_activity
        }
        endpoint = f"/v1/apikeys/{api_key_unique_id}"
        response = make_rest_call(endpoint=endpoint,
                                    method='GET',
                                    connector_info=connector_info,
                                    config=config,
                                    params=param)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def update_api_key(config, params, connector_info):
    try:
        entity_tag = params.get('entity_tag')
        api_key_unique_id = params.get('api_key_unique_id')
        
        headers = {'If-Match': entity_tag}
        payload = {
            'name': params.get('name'),
            'description': params.get('description'),
            'support_sessions': params.get('support_sessions'),
            'action_when_leaked': params.get('action_when_leaked')
        }
        payload = {key: value for key, value in payload.items() if value is not None and value != ""}
        endpoint = f"/v1/apikeys/{api_key_unique_id}"
        response = make_rest_call(endpoint=endpoint,
                                    method='PUT',
                                    connector_info=connector_info,
                                    headers=headers,
                                    config=config,
                                    data=json.dumps(payload))
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def delete_api_key(config, params, connector_info):
    try:
        api_key_unique_id = params.get('api_key_unique_id')
        endpoint = f"/v1/apikeys/{api_key_unique_id}"
        response = make_rest_call(endpoint=endpoint,
                                    method='DELETE',
                                    connector_info=connector_info,
                                    config=config)
        if response:
            return {'Status': 400, 'API Key Status': 'Failed too Delete API Key', 'API Key ID': api_key_unique_id}
        else:
            return {'Status': 200, 'API Key Status': 'API Key Deleted Successfully', 'API Key ID': api_key_unique_id}
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def lock_api_key(config, params, connector_info):
    try:
        api_key_unique_id = params.get('api_key_unique_id')
        endpoint = f"/v1/apikeys/{api_key_unique_id}/lock"
        response = make_rest_call(endpoint=endpoint,
                                    method='POST',
                                    connector_info=connector_info,
                                    config=config)
        if response:
            return {'Status': 400, 'API Key Status': 'Failed to Lock API Key', 'API Key ID': api_key_unique_id}
        else:
            return {'Status': 200, 'API Key Status': 'API Key Successfully Locked', 'API Key ID': api_key_unique_id}
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def unlock_api_key(config, params, connector_info):
    try:
        api_key_unique_id = params.get('api_key_unique_id')
        endpoint = f"/v1/apikeys/{api_key_unique_id}/lock"
        response = make_rest_call(  endpoint=endpoint,
                                    method='DELETE',
                                    connector_info=connector_info,
                                    config=config)
        if response:
            return {'Status': 400, 'API Key Status': 'Failed to Unlock API Key', 'API Key ID': api_key_unique_id}
        else:
            return {'Status': 200, 'API Key Status': 'API Key Successfully Unlocked', 'API Key ID': api_key_unique_id}
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def disable_the_api_key(config, params, connector_info):
    try:
        api_key_unique_id = params.get('api_key_unique_id')
        endpoint = f"/v1/apikeys/{api_key_unique_id}/disable"
        response = make_rest_call(endpoint=endpoint,
                                    method='POST',
                                    connector_info=connector_info,
                                    config=config)
        if response:
            return {'Status': 400, 'API Key Status': 'Failed to disable API Key', 'API Key ID': api_key_unique_id}
        else:
            return {'Status': 200, 'API Key Status': 'API Key Successfully Disabled', 'API Key ID': api_key_unique_id}
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def enable_the_api_key(config, params, connector_info):
    try:
        api_key_unique_id = params.get('api_key_unique_id')
        endpoint = f"/v1/apikeys/{api_key_unique_id}/disable"
        response = make_rest_call(endpoint=endpoint,
                                    method='DELETE',
                                    connector_info=connector_info,
                                    config=config)
        if response:
            return {'Status': 400, 'API Key Status': 'Failed to enable API Key', 'API Key ID': api_key_unique_id}
        else:
            return {'Status': 200, 'API Key Status': 'API Key Successfully Enabled', 'API Key ID': api_key_unique_id}
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def list_service_id_by_name(config, params, connector_info):
    try:
        query_params = {}
        keys_to_check = ['account_id', 'name', 'pagesize', 'pagetoken', 'sort', 'order', 'include_history']
    
        for key in keys_to_check:
            value = params.get(key)
            if value:
                query_params[key] = value

        query = '&'.join([f"{key}={val}" for key, val in query_params.items()])
        endpoints = '/v1/serviceids?' + query
        response = make_rest_call(endpoint=endpoints,
                                    method='GET',
                                    connector_info=connector_info,
                                    config=config)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def list_service_id_by_account_id(config, params, connector_info):
    try:
        account_id = params.get('account_id')
        endpoints = f'/v1/serviceids?account_id={account_id}' 
        response = make_rest_call(endpoint=endpoints,
                                    method='GET',
                                    connector_info=connector_info,
                                    config=config)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def create_a_service_id(config, params, connector_info):
    try:
        payload = {      
            'account_id': params.get('account_id'),
            'name': params.get('name'),
            'unique_instance_crns': params.get('unique_instance_crns'),
            'description': params.get('description'),
        }
        endpoint = '/v1/serviceids'
        payload = {key: value for key, value in payload.items() if value is not None and value != ""}
        response = make_rest_call(endpoint=endpoint,
                                    method='POST',
                                    connector_info=connector_info,
                                    config=config,
                                    data=json.dumps(payload))
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))    


def update_service_id(config, params, connector_info):
    try:
        entity_tag = params.get('entity_tag')
        service_id = params.get('service_id')
        
        headers = {'If-Match': entity_tag}
        payload = {
            'name': params.get('name'),
            'description': params.get('description'),
            'unique_instance_crns': params.get('unique_instance_crns'),
            'action_when_leaked': params.get('action_when_leaked')
        }
        payload = {key: value for key, value in payload.items() if value is not None and value != ""}
        endpoint = f"/v1/serviceids/{service_id}"
        response = make_rest_call(endpoint=endpoint,
                                    method='PUT',
                                    connector_info=connector_info,
                                    headers=headers,
                                    config=config,
                                    data=json.dumps(payload))
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def delete_service_id_and_associated_api_keys(config, params, connector_info):
    try:
        service_id = params.get('service_id')
        endpoint = f"/v1/serviceids/{service_id}"
        response = make_rest_call(endpoint=endpoint,
                                    method='DELETE',
                                    connector_info=connector_info,
                                    config=config)
        if response:
            return {'Status': 400, 'API Key Status': 'Failed too Delete API Key', 'API Key ID': service_id}
        else:
            return {'Status': 200, 'API Key Status': 'API Key Deleted Successfully', 'API Key ID': service_id}
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def lock_service_id(config, params, connector_info):
    try:
        service_id = params.get('service_id')
        endpoint = f"/v1/serviceids/{service_id}/lock"
        response = make_rest_call(endpoint=endpoint,
                                    method='POST',
                                    connector_info=connector_info,
                                    config=config)
        if response:
            return {'Status': 400, 'Service ID Status': 'Failed to Lock API Key', 'Service ID': service_id}
        else:
            return {'Status': 200, 'Service ID Status': 'API Key Successfully Locked', 'Service ID': service_id}
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def unlock_service_id(config, params, connector_info):
    try:
        service_id = params.get('service_id')
        endpoint = f"/v1/serviceids/{service_id}/lock"
        response = make_rest_call(endpoint=endpoint,
                                    method='DELETE',
                                    connector_info=connector_info,
                                    config=config)
        if response:
            return {'Status': 400, 'Service ID Status': 'Failed to Lock API Key', 'Service ID': service_id}
        else:
            return {'Status': 200, 'Service ID Status': 'API Key Successfully Locked', 'Service ID': service_id}
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))  


def get_account_configurations(config, params, connector_info):
    try:
        accounts_id = params.get('account_id')
        endpoints = f'/v1/accounts/{accounts_id}/settings/identity'
        response = make_rest_call(endpoint=endpoints,
                                    method='GET',
                                    connector_info=connector_info,
                                    config=config)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def update_account_configurations(config, params, connector_info):
    try:
        entity_tag = params.get('entity_tag')
        account_id = params.get('account_id')
        
        headers = {'If-Match': entity_tag}
        payload = {
            'restrict_create_service_id': params.get('restrict_create_service_id'),
            'restrict_create_platform_apikey': params.get('restrict_create_platform_apikey'),
            'allowed_ip_addresses': params.get('allowed_ip_addresses'),
            'mfa': params.get('mfa'),
            'user_mfa': params.get('user_mfa'),
            'session_expiration_in_seconds': params.get('session_expiration_in_seconds'),
            'session_invalidation_in_seconds': params.get('session_invalidation_in_seconds'),
            'max_sessions_per_identity': params.get('max_sessions_per_identity'),
            'system_access_token_expiration_in_seconds': params.get('system_access_token_expiration_in_seconds'),
            'system_refresh_token_expiration_in_seconds': params.get('system_refresh_token_expiration_in_seconds')
        }
        payload = {key: value for key, value in payload.items() if value is not None and value != ""}
        endpoint = f"/v1/accounts/{account_id}/settings/identity"
        response = make_rest_call(  endpoint=endpoint,
                                    method='PUT',
                                    connector_info=connector_info,
                                    headers=headers,
                                    config=config,
                                    data=json.dumps(payload))
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))    


def trigger_activity_report_for_the_account(config, params, connector_info):
    try:
        accounts_id = params.get('account_id')
        param = {
            "type":  params.get('type'),
            "duration":  params.get('duration')
        }
        endpoints = f'/v1/activity/accounts/{accounts_id}/report'
        response = make_rest_call(endpoint=endpoints,
                                    method='POST',
                                    connector_info=connector_info,
                                    config=config,
                                    params=param)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def get_activity_report_for_the_account(config, params, connector_info):
    try:
        accounts_id = params.get('account_id')
        reference = params.get('reference')
        endpoints = f'/v1/activity/accounts/{accounts_id}/report/{reference}'
        response = make_rest_call(endpoint=endpoints,
                                    method='GET',
                                    connector_info=connector_info,
                                    config=config)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))    


operations = {
    # API keys Operations 
    'get_api_keys': get_api_keys_by_iam_id_and_account_id,
    'create_an_api_key': create_an_api_key,
    'get_api_key_details_by_value': get_api_key_details_by_value,
    'get_api_key_details': get_api_key_details,
    'update_api_key': update_api_key,
    'delete_api_key': delete_api_key,
    'lock_api_key': lock_api_key,
    'unlock_api_key': unlock_api_key,
    'disable_the_api_key': disable_the_api_key,
    'enable_the_api_key': enable_the_api_key,
    # Service ID Operations 
    'list_service_id_by_name': list_service_id_by_name,
    'list_service_id_by_account_id': list_service_id_by_account_id,
    'create_a_service_id': create_a_service_id,
    'update_service_id': update_service_id,
    'delete_service_id_and_associated_api_keys':delete_service_id_and_associated_api_keys,
    'lock_service_id': lock_service_id,
    'unlock_service_id':unlock_service_id,
    # Account Setting
    'get_account_configurations':get_account_configurations,
    'update_account_configurations':update_account_configurations,
    # Activity Operations
    'trigger_activity_report_for_the_account': trigger_activity_report_for_the_account,
    'get_activity_report_for_the_account': get_activity_report_for_the_account
    
    
    
}

