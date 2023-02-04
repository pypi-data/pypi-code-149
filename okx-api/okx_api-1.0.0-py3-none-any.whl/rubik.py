from paux.param import to_local
from okx_api._client import Client


class _RubikEndpoints:
    get_support_coin = ['/api/v5/rubik/stat/trading-data/support-coin', 'GET']  # 获取交易大数据支持币种
    get_taker_volume = ['/api/v5/rubik/stat/taker-volume', 'GET']  # 获取主动买入/卖出情况
    get_loan_ratio = ['/api/v5/rubik/stat/margin/loan-ratio', 'GET']  # 获取杠杆多空比
    get_long_short_account_ratio = ['/api/v5/rubik/stat/contracts/long-short-account-ratio', 'GET']  # 获取合约多空持仓人数比
    get_contracts_open_interest_volume = ['/api/v5/rubik/stat/contracts/open-interest-volume', 'GET']  # 获取合约持仓量及交易量
    get_option_open_interest_volume = ['/api/v5/rubik/stat/option/open-interest-volume', 'GET']  # 获取期权持仓量及交易量
    get_open_interest_volume_ratio = ['/api/v5/rubik/stat/option/open-interest-volume-ratio', 'GET']  # 看涨/看跌期权合约 持仓总量比/交易总量比
    get_open_interest_volume_expiry = ['/api/v5/rubik/stat/option/open-interest-volume-expiry', 'GET']  # 看涨看跌持仓总量及交易总量（按到期日分）
    get_open_interest_volume_strike = ['/api/v5/rubik/stat/option/open-interest-volume-strike', 'GET']  # 看涨看跌持仓总量及交易总量（按执行价格分）
    get_taker_block_volume = ['/api/v5/rubik/stat/option/taker-block-volume', 'GET']  # 看跌/看涨期权合约 主动买入/卖出量


class Rubik(Client):
    # 获取交易大数据支持币种
    def get_support_coin(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trading-data-get-support-coin
        '''
        return self.send_request(*_RubikEndpoints.get_support_coin, **to_local(locals()))

    # 获取主动买入/卖出情况
    def get_taker_volume(self, ccy: str, instType: str, begin: str = '', end: str = '', period: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trading-data-get-taker-volume
        '''
        return self.send_request(*_RubikEndpoints.get_taker_volume, **to_local(locals()))

    # 获取杠杆多空比
    def get_loan_ratio(self, ccy: str, begin: str = '', end: str = '', period: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trading-data-get-margin-lending-ratio
        '''
        return self.send_request(*_RubikEndpoints.get_loan_ratio, **to_local(locals()))

    # 获取合约多空持仓人数比
    def get_long_short_account_ratio(self, ccy: str, begin: str = '', end: str = '', period: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trading-data-get-long-short-ratio
        '''
        return self.send_request(*_RubikEndpoints.get_long_short_account_ratio, **to_local(locals()))

    # 获取合约持仓量及交易量
    def get_contracts_open_interest_volume(self, ccy: str, begin: str = '', end: str = '', period: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trading-data-get-contracts-open-interest-and-volume
        '''
        return self.send_request(*_RubikEndpoints.get_contracts_open_interest_volume, **to_local(locals()))

    # 获取期权持仓量及交易量
    def get_option_open_interest_volume(self, ccy: str, period: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trading-data-get-options-open-interest-and-volume
        '''
        return self.send_request(*_RubikEndpoints.get_option_open_interest_volume, **to_local(locals()))

    # 看涨/看跌期权合约 持仓总量比/交易总量比
    def get_open_interest_volume_ratio(self, ccy: str, period: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trading-data-get-put-call-ratio
        '''
        return self.send_request(*_RubikEndpoints.get_open_interest_volume_ratio, **to_local(locals()))

    # 看涨看跌持仓总量及交易总量（按到期日分）
    def get_open_interest_volume_expiry(self, ccy: str, period: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trading-data-get-open-interest-and-volume-expiry
        '''
        return self.send_request(*_RubikEndpoints.get_open_interest_volume_expiry, **to_local(locals()))

    # 看涨看跌持仓总量及交易总量（按执行价格分）
    def get_open_interest_volume_strike(self, ccy: str, expTime: str, period: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trading-data-get-open-interest-and-volume-strike
        '''
        return self.send_request(*_RubikEndpoints.get_open_interest_volume_strike, **to_local(locals()))

    # 看跌/看涨期权合约 主动买入/卖出量
    def get_taker_block_volume(self, ccy: str, period: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trading-data-get-taker-flow
        '''
        return self.send_request(*_RubikEndpoints.get_taker_block_volume, **to_local(locals()))
