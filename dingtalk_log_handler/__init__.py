"""
dingtalk_log_handler: send log message to dingtalk

addtion info https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq/XAzBI
"""
import base64
import hashlib
import hmac
import http.client
import json
import logging
import logging.handlers
import ssl
import socket
import time
import urllib.parse


__author__ = 'ruan.lj'
__version__ = '0.0.7'
__all__ = (
    'OAPI_DOMAIN',
    'DingTalkHandler',
)

OAPI_DOMAIN = 'oapi.dingtalk.com'   # dingtalk open api domain

class DingdingApiError(RuntimeError):
    pass

class DingTalkHandler(logging.Handler):
    """Handler for logging message to dingtalk"""

    def __init__(self, webhook, keyword='alarm', secret='', hostname='', timeout=1, cert_verify=True):
        """
        args:
            webhook: webhook url for dingtalk open api
            keyword: allowed message keyword, default 'alarm'
            secret: secret for dingtalk open api
            hostname: hostname for identify machine, default local ip address
            timeout: http request timeout, default 1 second
            cert_verify: verify SSL certificates or not, default True
        """

        logging.Handler.__init__(self)
        if OAPI_DOMAIN not in webhook:
            raise ValueError('webhook url must like "https://oapi.dingtalk.com/robot/send?access_token=XXXXXXX"')
        self.webhook = webhook
        self.keyword = keyword
        self.secret = secret
        self.hostname = hostname if hostname else self.get_hostname()
        self.timeout = timeout
        self.cert_verify = cert_verify

    @staticmethod
    def get_hostname():
        """get local ip address as hostname"""

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(1)
            s.connect((OAPI_DOMAIN, 443))
            return s.getsockname()[0]
        except socket.gaierror:
            raise ValueError('connect to "oapi.dingtalk.com" failed, please check your network')

    def get_timestamp_and_sign(self):
        """get timestamp and sign for dingtalk open api"""
        timestamp = str(round(time.time() * 1000))
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        hmac_code = hmac.new(self.secret.encode('utf8'), string_to_sign.encode('utf8'),
                             digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return timestamp, sign

    def emit(self, record):
        try:
            msg = self.format(record)
            final_msg = '{} from: {}\n{}'.format(self.keyword, self.hostname, msg)
            data = {
                'msgtype': 'text',
                'text': {'content': final_msg},
            }
            body = json.dumps(data).encode('utf8')
            if 'https' in self.webhook:
                context = None if self.cert_verify else ssl._create_unverified_context()
                h = http.client.HTTPSConnection(OAPI_DOMAIN, timeout=self.timeout, context=context)
            else:
                h = http.client.HTTPConnection(OAPI_DOMAIN, timeout=self.timeout)
            headers = dict([
                ('content-type', 'application/json;charset=UTF-8'),
                ("Content-length", len(body)),
            ])
            if self.secret:
                timestamp, sign = self.get_timestamp_and_sign()
                url = self.webhook + '&timestamp={}&sign={}'.format(timestamp, sign)
            else:
                url = self.webhook
            h.request('POST', url, body=body, headers=headers)
            r = h.getresponse()
            content = r.read().decode('utf8')
            if r.status != 200:
                raise DingdingApiError('call dingtalk api failed! status: {}, content: {}'.format(r.status, content))
            res = json.loads(content)
            if res.get('errcode') != 0:
                raise DingdingApiError(content)
        except Exception:
            self.handleError(record)

logging.handlers.DingTalkHandler = DingTalkHandler
