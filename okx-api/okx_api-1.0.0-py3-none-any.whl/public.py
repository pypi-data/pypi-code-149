from paux.param import to_local
from okx_api._client import Client


class _PublicEndpoints:
    get_instruments = ['/api/v5/public/instruments', 'GET']  # 获取交易产品基础信息
    get_delivery_exercise_history = ['/api/v5/public/delivery-exercise-history', 'GET']  # 获取交割和行权记录
    get_open_interest = ['/api/v5/public/open-interest', 'GET']  # 获取持仓总量
    get_funding_rate = ['/api/v5/public/funding-rate', 'GET']  # 获取永续合约当前资金费率
    get_funding_rate_history = ['/api/v5/public/funding-rate-history', 'GET']  # 获取永续合约历史资金费率
    get_price_limit = ['/api/v5/public/price-limit', 'GET']  # 获取限价
    get_opt_summary = ['/api/v5/public/opt-summary', 'GET']  # 获取期权定价
    get_estimated_price = ['/api/v5/public/estimated-price', 'GET']  # 获取预估交割/行权价格
    get_discount_rate_interest_free_quota = ['/api/v5/public/discount-rate-interest-free-quota', 'GET']  # 获取免息额度和币种折算率等级
    get_time = ['/api/v5/public/time', 'GET']  # 获取系统时间
    get_liquidation_orders = ['/api/v5/public/liquidation-orders', 'GET']  # 获取平台公共爆仓单信息
    get_mark_price = ['/api/v5/public/mark-price', 'GET']  # 获取标记价格
    get_position_tiers = ['/api/v5/public/position-tiers', 'GET']  # 获取衍生品仓位档位
    get_interest_rate_loan_quota = ['/api/v5/public/interest-rate-loan-quota', 'GET']  # 获取市场借币杠杆利率和借币限额
    get_vip_interest_rate_loan_quota = ['/api/v5/public/vip-interest-rate-loan-quota', 'GET']  # 获取尊享借币杠杆利率和借币限额
    get_underlying = ['/api/v5/public/underlying', 'GET']  # 获取衍生品标的指数
    get_insurance_fund = ['/api/v5/public/insurance-fund', 'GET']  # 获取风险准备金余额
    get_convert_contract_coin = ['/api/v5/public/convert-contract-coin', 'GET']  # 张币转换
    get_option_trades = ['/api/v5/public/option-trades', 'GET']  # 获取期权公共成交数据


class Public(Client):
    # 获取交易产品基础信息
    def get_instruments(self, instType: str, uly: str = '', instFamily: str = '', instId: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-instruments
        '''
        return self.send_request(*_PublicEndpoints.get_instruments, **to_local(locals()))

    # 获取交割和行权记录
    def get_delivery_exercise_history(self, instType: str, uly: str = '', instFamily: str = '', after: str = '',
                                      before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-delivery-exercise-history
        '''
        return self.send_request(*_PublicEndpoints.get_delivery_exercise_history, **to_local(locals()))

    # 获取持仓总量
    def get_open_interest(self, instType: str, uly: str = '', instFamily: str = '', instId: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-open-interest
        '''
        return self.send_request(*_PublicEndpoints.get_open_interest, **to_local(locals()))

    # 获取永续合约当前资金费率
    def get_funding_rate(self, instId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-funding-rate
        '''
        return self.send_request(*_PublicEndpoints.get_funding_rate, **to_local(locals()))

    # 获取永续合约历史资金费率
    def get_funding_rate_history(self, instId: str, before: str = '', after: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-funding-rate-history
        '''
        return self.send_request(*_PublicEndpoints.get_funding_rate_history, **to_local(locals()))

    # 获取限价
    def get_price_limit(self, instId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-limit-price
        '''
        return self.send_request(*_PublicEndpoints.get_price_limit, **to_local(locals()))

    # 获取期权定价
    def get_opt_summary(self, uly: str = '', instFamily: str = '', expTime: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-option-market-data
        '''
        return self.send_request(*_PublicEndpoints.get_opt_summary, **to_local(locals()))

    # 获取预估交割/行权价格
    def get_estimated_price(self, instId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-estimated-delivery-exercise-price
        '''
        return self.send_request(*_PublicEndpoints.get_estimated_price, **to_local(locals()))

    # 获取免息额度和币种折算率等级
    def get_discount_rate_interest_free_quota(self, ccy: str = '', discountLv: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-discount-rate-level-and-interest-free-quota
        '''
        return self.send_request(*_PublicEndpoints.get_discount_rate_interest_free_quota, **to_local(locals()))

    # 获取系统时间
    def get_time(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-system-time
        '''
        return self.send_request(*_PublicEndpoints.get_time, **to_local(locals()))

    # 获取平台公共爆仓单信息
    def get_liquidation_orders(self, instType: str, mgnMode: str = '', instId: str = '', ccy: str = '', uly: str = '',
                               instFamily: str = '', alias: str = '', state: str = '', before: str = '',
                               after: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-liquidation-orders
        '''
        return self.send_request(*_PublicEndpoints.get_liquidation_orders, **to_local(locals()))

    # 获取标记价格
    def get_mark_price(self, instType: str, uly: str = '', instFamily: str = '', instId: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-mark-price
        '''
        return self.send_request(*_PublicEndpoints.get_mark_price, **to_local(locals()))

    # 获取衍生品仓位档位
    def get_position_tiers(self, instType: str, tdMode: str, uly: str = '', instFamily: str = '', instId: str = '',
                           ccy: str = '', tier: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-position-tiers
        '''
        return self.send_request(*_PublicEndpoints.get_position_tiers, **to_local(locals()))

    # 获取市场借币杠杆利率和借币限额
    def get_interest_rate_loan_quota(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-interest-rate-and-loan-quota-for-market-loans
        '''
        return self.send_request(*_PublicEndpoints.get_interest_rate_loan_quota, **to_local(locals()))

    # 获取尊享借币杠杆利率和借币限额
    def get_vip_interest_rate_loan_quota(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-interest-rate-and-loan-quota-for-vip-loans
        '''
        return self.send_request(*_PublicEndpoints.get_vip_interest_rate_loan_quota, **to_local(locals()))

    # 获取衍生品标的指数
    def get_underlying(self, instType: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-underlying
        '''
        return self.send_request(*_PublicEndpoints.get_underlying, **to_local(locals()))

    # 获取风险准备金余额
    def get_insurance_fund(self, instType: str, type: str = '', uly: str = '', instFamily: str = '', ccy: str = '',
                           before: str = '', after: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-insurance-fund
        '''
        return self.send_request(*_PublicEndpoints.get_insurance_fund, **to_local(locals()))

    # 张币转换
    def get_convert_contract_coin(self, instId: str, sz: str, type: str = '', px: str = '', unit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-unit-convert
        '''
        return self.send_request(*_PublicEndpoints.get_convert_contract_coin, **to_local(locals()))

    # 获取期权公共成交数据
    def get_option_trades(self, instId: str = '', instFamily: str = '', optType: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-public-data-get-option-trades
        '''
        return self.send_request(*_PublicEndpoints.get_option_trades, **to_local(locals()))
