import json
import os
from datetime import datetime, timedelta
from enum import Enum, auto

import requests

from .exceptions import QYWXIdSecretInvalidError, QYWXTokenInvalidError


class MsgType(Enum):
    TEXT = auto()


class QYWX:
    def __init__(self, id=None, secret=None):
        if id is None or secret is None:
            self.corp_id = os.environ.get('QYWX_CORP_ID', '')
            self.corp_secret = os.environ.get('QYWX_CORP_SECRET', '')
        else:
            self.corp_id = id
            self.corp_secret = secret
        self._check_id_and_secret()

        self.expired_time = datetime.utcnow()
        self.token = self._get_token()
        if not self._token_is_valid():
            raise QYWXTokenInvalidError

    def _check_id_and_secret(self):
        if len(self.corp_id) == 0 or len(self.corp_secret) == 0:
            raise QYWXIdSecretInvalidError

    def _get_token(self):
        """
        https://developer.work.weixin.qq.com/document/path/91039
        """
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={'corpid': self.corp_id, 'corpsecret': self.corp_secret})
        if r.status_code == 200:
            result = json.loads(r.content)
            err = result.get('errcode', -1)
            if err == 0:
                self.expired_time = datetime.utcnow() + timedelta(seconds=int(result.get('expires_in', 7200)))
                return result.get('access_token', '')
        else:
            return ''

    def _token_is_valid(self):
        return len(self.token) > 0 and datetime.utcnow() < self.expired_time

    def _push_text(self, content, **kwargs):
        payload = {
            'msgtype': 'text',
            'agentid': int(kwargs.get('agent_id', 1000001)),
            'text': {"content": content},
            'touser': str(kwargs.get('to_user', '@all'))
        }
        if payload['touser'] != '@all':
            payload['toparty'] = kwargs.get('to_party', '')
            payload['totag'] = kwargs.get('to_tag', '')
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send',
                          params={'access_token': self.token}, json=payload)
        if r.status_code == 200:
            send_result = json.loads(r.content)
            if send_result['errcode'] == 0:
                return True
            else:
                print(send_result['errmsg'])
        return False

    def push(self, msg, msg_type=MsgType.TEXT, **kwargs):
        """
        https://developer.work.weixin.qq.com/document/path/90236
        :param msg:
        :param msg_type:
        :return:
        """
        res = False
        if msg_type == MsgType.TEXT:
            res = self._push_text(msg, **kwargs)

        if res:
            print('Message send succeed.')
        else:
            print('Message send failed, please check the error message above.')
