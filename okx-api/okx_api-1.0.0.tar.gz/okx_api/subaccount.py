from paux.param import to_local
from okx_api._client import Client


class _SubAccountEndpoints:
    get_list = ['/api/v5/users/subaccount/list', 'GET']  # 查看子账户列表
    set_modify_apikey = ['/api/v5/users/subaccount/modify-apikey', 'POST']  # 重置子账户的APIKey
    get_account_balances = ['/api/v5/account/subaccount/balances', 'GET']  # 获取子账户交易账户余额
    get_asset_balances = ['/api/v5/asset/subaccount/balances', 'GET']  # 获取子账户资金账户余额
    get_bills = ['/api/v5/asset/subaccount/bills', 'GET']  # 查询子账户转账记录
    set_transfer = ['/api/v5/asset/subaccount/transfer', 'POST']  # 子账户间资金划转
    set_set_transfer_out = ['/api/v5/users/subaccount/set-transfer-out', 'POST']  # 设置子账户主动转出权限
    get_entrust_subaccount_list = ['/api/v5/users/entrust-subaccount-list', 'GET']  # 查看被托管的子账户列表
    get_if_rebate = ['/api/v5/users/partner/if-rebate', 'GET']  # 获取用户的节点返佣信息


class SubAccount(Client):
    # 查看子账户列表
    def get_list(self, enable: str = '', subAcct: str = '', after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-subaccount-view-sub-account-list
        '''
        return self.send_request(*_SubAccountEndpoints.get_list, **to_local(locals()))

    # 重置子账户的APIKey
    def set_modify_apikey(self, subAcct: str, apiKey: str, label: str = '', perm: str = '', ip: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-subaccount-reset-the-apikey-of-a-sub-account
        '''
        return self.send_request(*_SubAccountEndpoints.set_modify_apikey, **to_local(locals()))

    # 获取子账户交易账户余额
    def get_account_balances(self, subAcct: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-subaccount-get-sub-account-trading-balance
        '''
        return self.send_request(*_SubAccountEndpoints.get_account_balances, **to_local(locals()))

    # 获取子账户资金账户余额
    def get_asset_balances(self, subAcct: str, ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-subaccount-get-sub-account-funding-balance
        '''
        return self.send_request(*_SubAccountEndpoints.get_asset_balances, **to_local(locals()))

    # 查询子账户转账记录
    def get_bills(self, ccy: str = '', type: str = '', subAcct: str = '', after: str = '', before: str = '',
                  limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-subaccount-history-of-sub-account-transfer
        '''
        return self.send_request(*_SubAccountEndpoints.get_bills, **to_local(locals()))

    # 子账户间资金划转
    def set_transfer(self, ccy: str, amt: str, _from: str, to: str, fromSubAccount: str, toSubAccount: str,
                     loanTrans: bool = '', omitPosRisk: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-subaccount-master-accounts-manage-the-transfers-between-sub-accounts
        '''
        data = to_local(locals())
        data['from'] = data['_from']
        del data['_from']
        return self.send_request(*_SubAccountEndpoints.set_transfer, **data)

    # 设置子账户主动转出权限
    def set_set_transfer_out(self, subAcct: str, canTransOut: bool = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-subaccount-set-permission-of-transfer-out
        '''
        return self.send_request(*_SubAccountEndpoints.set_set_transfer_out, **to_local(locals()))

    # 查看被托管的子账户列表
    def get_entrust_subaccount_list(self, subAcct: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-subaccount-get-custody-trading-sub-account-list
        '''
        return self.send_request(*_SubAccountEndpoints.get_entrust_subaccount_list, **to_local(locals()))

    # 获取用户的节点返佣信息
    def get_if_rebate(self, apiKey: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-subaccount-get-the-user-39-s-affiliate-rebate-information
        '''
        return self.send_request(*_SubAccountEndpoints.get_if_rebate, **to_local(locals()))
