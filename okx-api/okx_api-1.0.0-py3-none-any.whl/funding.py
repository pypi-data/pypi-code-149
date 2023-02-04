from paux.param import to_local
from okx_api._client import Client


class _FundingEndpoints:
    get_currencies = ['/api/v5/asset/currencies', 'GET']  # 获取币种列表
    get_balances = ['/api/v5/asset/balances', 'GET']  # 获取资金账户余额
    get_non_tradable_assets = ['/api/v5/asset/non-tradable-assets', 'GET']  # 获取不可交易资产
    get_asset_valuation = ['/api/v5/asset/asset-valuation', 'GET']  # 获取账户资产估值
    set_transfer = ['/api/v5/asset/transfer', 'POST']  # 资金划转
    get_transfer_state = ['/api/v5/asset/transfer-state', 'GET']  # 获取资金划转状态
    get_bills = ['/api/v5/asset/bills', 'GET']  # 获取资金流水
    get_deposit_lightning = ['/api/v5/asset/deposit-lightning', 'GET']  # 闪电网络充币
    get_deposit_address = ['/api/v5/asset/deposit-address', 'GET']  # 获取充值地址信息
    get_deposit_history = ['/api/v5/asset/deposit-history', 'GET']  # 获取充值记录
    set_withdrawal = ['/api/v5/asset/withdrawal', 'POST']  # 提币
    set_withdrawal_lightning = ['/api/v5/asset/withdrawal-lightning', 'POST']  # 闪电网络提币
    set_cancel_withdrawal = ['/api/v5/asset/cancel-withdrawal', 'POST']  # 撤销提币
    get_withdrawal_history = ['/api/v5/asset/withdrawal-history', 'GET']  # 获取提币记录
    get_deposit_withdraw_status = ['/api/v5/asset/deposit-withdraw-status', 'GET']  # 获取充值/提现的详细状态
    set_convert_dust_assets = ['/api/v5/asset/convert-dust-assets', 'POST']  # 小额资产兑换
    get_saving_balance = ['/api/v5/asset/saving-balance', 'GET']  # 获取余币宝余额
    set_purchase_redempt = ['/api/v5/asset/purchase_redempt', 'POST']  # 余币宝申购/赎回
    set_set_lending_rate = ['/api/v5/asset/set-lending-rate', 'POST']  # 设置余币宝借贷利率
    get_lending_history = ['/api/v5/asset/lending-history', 'GET']  # 获取余币宝出借明细
    get_lending_rate_summary = ['/api/v5/asset/lending-rate-summary', 'GET']  # 获取市场借贷信息（公共）
    get_lending_rate_history = ['/api/v5/asset/lending-rate-history', 'GET']  # 获取市场借贷历史（公共）


class Funding(Client):
    # 获取币种列表
    def get_currencies(self, ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-currencies
        '''
        return self.send_request(*_FundingEndpoints.get_currencies, **to_local(locals()))

    # 获取资金账户余额
    def get_balances(self, ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-balance
        '''
        return self.send_request(*_FundingEndpoints.get_balances, **to_local(locals()))

    # 获取不可交易资产
    def get_non_tradable_assets(self, ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-non-tradable-assets
        '''
        return self.send_request(*_FundingEndpoints.get_non_tradable_assets, **to_local(locals()))

    # 获取账户资产估值
    def get_asset_valuation(self, ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-account-asset-valuation
        '''
        return self.send_request(*_FundingEndpoints.get_asset_valuation, **to_local(locals()))

    # 资金划转
    def set_transfer(self, ccy: str, amt: str, _from: str, to: str, subAcct: str = '', type: str = '',
                     loanTrans: bool = '', clientId: str = '', omitPosRisk: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-funds-transfer
        '''
        data = to_local(locals())
        data['from'] = data['_from']
        del data['_from']
        return self.send_request(*_FundingEndpoints.set_transfer, **data)

    # 获取资金划转状态
    def get_transfer_state(self, transId: str = '', clientId: str = '', type: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-funds-transfer-state
        '''
        return self.send_request(*_FundingEndpoints.get_transfer_state, **to_local(locals()))

    # 获取资金流水
    def get_bills(self, ccy: str = '', type: str = '', clientId: str = '', after: str = '', before: str = '',
                  limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-asset-bills-details
        '''
        return self.send_request(*_FundingEndpoints.get_bills, **to_local(locals()))

    # 闪电网络充币
    def get_deposit_lightning(self, ccy: str, amt: str, to: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-lightning-deposits
        '''
        return self.send_request(*_FundingEndpoints.get_deposit_lightning, **to_local(locals()))

    # 获取充值地址信息
    def get_deposit_address(self, ccy: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-deposit-address
        '''
        return self.send_request(*_FundingEndpoints.get_deposit_address, **to_local(locals()))

    # 获取充值记录
    def get_deposit_history(self, ccy: str = '', depId: str = '', fromWdId: str = '', txId: str = '', type: str = '',
                            state: str = '', after: str = '', before: str = '', limit: object = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-deposit-history
        '''
        return self.send_request(*_FundingEndpoints.get_deposit_history, **to_local(locals()))

    # 提币
    def set_withdrawal(self, ccy: str, amt: str, dest: str, toAddr: str, fee: str, chain: str = '', areaCode: str = '',
                       clientId: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-withdrawal
        '''
        return self.send_request(*_FundingEndpoints.set_withdrawal, **to_local(locals()))

    # 闪电网络提币
    def set_withdrawal_lightning(self, ccy: str, invoice: str, memo: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-lightning-withdrawals
        '''
        return self.send_request(*_FundingEndpoints.set_withdrawal_lightning, **to_local(locals()))

    # 撤销提币
    def set_cancel_withdrawal(self, wdId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-cancel-withdrawal
        '''
        return self.send_request(*_FundingEndpoints.set_cancel_withdrawal, **to_local(locals()))

    # 获取提币记录
    def get_withdrawal_history(self, ccy: str = '', wdId: str = '', clientId: str = '', txId: str = '', type: str = '',
                               state: str = '', after: str = '', before: str = '', limit: object = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-withdrawal-history
        '''
        return self.send_request(*_FundingEndpoints.get_withdrawal_history, **to_local(locals()))

    # 获取充值/提现的详细状态
    def get_deposit_withdraw_status(self, wdId: str = '', txId: str = '', ccy: str = '', to: str = '', chain: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-deposit-withdraw-status
        '''
        return self.send_request(*_FundingEndpoints.get_deposit_withdraw_status, **to_local(locals()))

    # 小额资产兑换
    def set_convert_dust_assets(self, ccy: object):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-small-assets-convert
        '''
        return self.send_request(*_FundingEndpoints.set_convert_dust_assets, **to_local(locals()))

    # 获取余币宝余额
    def get_saving_balance(self, ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-saving-balance
        '''
        return self.send_request(*_FundingEndpoints.get_saving_balance, **to_local(locals()))

    # 余币宝申购/赎回
    def set_purchase_redempt(self, ccy: str, amt: str, side: str, rate: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-savings-purchase-redemption
        '''
        return self.send_request(*_FundingEndpoints.set_purchase_redempt, **to_local(locals()))

    # 设置余币宝借贷利率
    def set_set_lending_rate(self, ccy: str, rate: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-set-lending-rate
        '''
        return self.send_request(*_FundingEndpoints.set_set_lending_rate, **to_local(locals()))

    # 获取余币宝出借明细
    def get_lending_history(self, ccy: str = '', after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-lending-history
        '''
        return self.send_request(*_FundingEndpoints.get_lending_history, **to_local(locals()))

    # 获取市场借贷信息（公共）
    def get_lending_rate_summary(self, ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-public-borrow-info-public
        '''
        return self.send_request(*_FundingEndpoints.get_lending_rate_summary, **to_local(locals()))

    # 获取市场借贷历史（公共）
    def get_lending_rate_history(self, ccy: str = '', after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-funding-get-public-borrow-history-public
        '''
        return self.send_request(*_FundingEndpoints.get_lending_rate_history, **to_local(locals()))
