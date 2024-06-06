"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests, json
import base64
from time import time, ctime
from datetime import datetime
from connectors.core.utils import update_connnector_config
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('ibm-iam')

REFRESH_TOKEN_FLAG = False


class IBM:
    def __init__(self, config):
        self.verify_ssl = config.get('verify_ssl')
        self.host = config.get("server_url")
        self.api_key = config.get('api_key')
        if self.host[:7] == "http://":
            self.host = "https://{0}".format(self.host)
        elif self.host[:8] == "https://":
            self.host = "{0}".format(self.host)
        else:
            self.host = "https://{0}".format(self.host)

    def convert_ts_epoch(self, ts):
        datetime_object = datetime.strptime(ctime(ts), "%a %b %d %H:%M:%S %Y")
        return datetime_object.timestamp()

    def generate_token(self, REFRESH_TOKEN_FLAG):
        try:
            token_resp = self.acquire_token(REFRESH_TOKEN_FLAG)
            ts_now = time()
            token_resp['expiresOn'] = (ts_now + token_resp['expires_in']) if token_resp.get("expires_in") else None
            token_resp['accessToken'] = token_resp.get("access_token")
            token_resp.pop("access_token")
            return token_resp
        except Exception as err:
            logger.error("{0}".format(err))
            raise ConnectorError("{0}".format(err))

    def validate_token(self, connector_config, connector_info):
        try:
            ts_now = time()
            if not connector_config.get('accessToken'):
                logger.error('Error occurred while connecting server: Unauthorized')
                raise ConnectorError('Error occurred while connecting server: Unauthorized')
            expires = connector_config['expiresOn']
            expires_ts = self.convert_ts_epoch(expires)
            if ts_now > float(expires_ts):
                logger.info("Token expired at {0}".format(expires))
                REFRESH_TOKEN_FLAG = True
                token_resp = self.generate_token(REFRESH_TOKEN_FLAG)
                connector_config['accessToken'] = token_resp['accessToken']
                connector_config['expiresOn'] = token_resp['expiresOn']
                update_connnector_config(connector_info['connector_name'], 
                                        connector_info['connector_version'],
                                        connector_config,
                                        connector_config['config_id'])

                return "Bearer {0}".format(connector_config.get('accessToken'))
            else:
                logger.info("Token is valid till {0}".format(expires))
                return "Bearer {0}".format(connector_config.get('accessToken'))
        except Exception as err:
            logger.error("{0}".format(str(err)))
            raise ConnectorError("{0}".format(str(err)))

    def acquire_token(self, REFRESH_TOKEN_FLAG):
        try:
            error_msg = ''
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded', 
                'Accept':'application/json'
            }
            data = {'grant_type': 'urn:ibm:params:oauth:grant-type:apikey', 'apikey': self.api_key}
            endpoint = self.host + '/identity/token'
            logger.debug("Endpoint: {0}".format(endpoint))
            logger.debug("Headers: {0}".format(headers))
            response = requests.post(endpoint, data=data, headers=headers, verify=self.verify_ssl, timeout=600)
            logger.debug("Response: {0}".format(response))
            if response.status_code in [200, 204, 201]:
                return response.json()
            else:
                if response.text != "":
                    err_resp = response.json()
                    if err_resp and 'error' in err_resp:
                        failure_msg = err_resp.get('error_description')
                        error_msg = 'Response {0}: {1} \n Error Message: {2}'.format(response.status_code,
                                                                                    response.reason,
                                                                                    failure_msg if failure_msg else '')
                    else:
                        err_resp = response.text
                else:
                    error_msg = '{0}:{1}'.format(response.status_code, response.reason)
                raise ConnectorError(error_msg)
        except Exception as err:
            logger.error("{0}".format(str(err)))
            raise ConnectorError("{0}".format(str(err)))


def check(config, connector_info):
    try:
        co = IBM(config)
        if not 'accessToken' in config:
            token_resp = co.generate_token(REFRESH_TOKEN_FLAG)
            config['accessToken'] = token_resp.get('accessToken')
            config['expiresOn'] = token_resp.get('expiresOn')
            update_connnector_config(connector_info['connector_name'], 
                                    connector_info['connector_version'], 
                                    config,
                                    config['config_id'])
            return True
        else:
            token_resp = co.validate_token(config, connector_info)
            return True
    except Exception as err:
        raise ConnectorError(str(err))