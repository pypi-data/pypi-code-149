from paux.param import to_local
from okx_api._client import Client


class _SystemEndpoints:
    get_status = ['/api/v5/system/status', 'GET']  # 获取系统升级事件的状态。


class System(Client):
    # 获取系统升级事件的状态。
    def get_status(self, state: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-status
        '''
        return self.send_request(*_SystemEndpoints.get_status, **to_local(locals()))
