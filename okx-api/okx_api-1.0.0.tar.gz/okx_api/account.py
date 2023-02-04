from paux.param import to_local
from okx_api._client import Client


class _AccountEndpoints:
    get_balance = ['/api/v5/account/balance', 'GET']  # 查看账户余额
    get_positions = ['/api/v5/account/positions', 'GET']  # 查看持仓信息
    get_positions_history = ['/api/v5/account/positions-history', 'GET']  # 查看历史持仓信息
    get_account_position_risk = ['/api/v5/account/account-position-risk', 'GET']  # 查看账户持仓风险
    get_bills = ['/api/v5/account/bills', 'GET']  # 账单流水查询（近七天）
    get_bills_archive = ['/api/v5/account/bills-archive', 'GET']  # 账单流水查询（近三月）
    get_config = ['/api/v5/account/config', 'GET']  # 查看账户配置
    set_set_position_mode = ['/api/v5/account/set-position-mode', 'POST']  # 设置持仓模式
    set_set_leverage = ['/api/v5/account/set-leverage', 'POST']  # 设置杠杆倍数
    get_max_size = ['/api/v5/account/max-size', 'GET']  # 获取最大可买卖/开仓数量
    get_max_avail_size = ['/api/v5/account/max-avail-size', 'GET']  # 获取最大可用数量
    set_margin_balance = ['/api/v5/account/position/margin-balance', 'POST']  # 调整保证金
    get_leverage_info = ['/api/v5/account/leverage-info', 'GET']  # 获取杠杆倍数
    get_max_loan = ['/api/v5/account/max-loan', 'GET']  # 获取交易产品最大可借
    get_trade_fee = ['/api/v5/account/trade-fee', 'GET']  # 获取当前账户交易手续费费率
    get_interest_accrued = ['/api/v5/account/interest-accrued', 'GET']  # 获取计息记录
    get_interest_rate = ['/api/v5/account/interest-rate', 'GET']  # 获取用户当前杠杆借币利率
    set_set_greeks = ['/api/v5/account/set-greeks', 'POST']  # 期权greeks的PA/BS切换
    set_set_isolated_mode = ['/api/v5/account/set-isolated-mode', 'POST']  # 逐仓交易设置
    get_max_withdrawal = ['/api/v5/account/max-withdrawal', 'GET']  # 查看账户最大可转余额
    get_risk_state = ['/api/v5/account/risk-state', 'GET']  # 查看账户特定风险状态
    set_quick_margin_borrow_repay = ['/api/v5/account/quick-margin-borrow-repay', 'POST']  # 一键借币模式手动借币还币
    get_quick_margin_borrow_repay_history = ['/api/v5/account/quick-margin-borrow-repay-history', 'GET']  # 获取一键借币还币历史
    set_borrow_repay = ['/api/v5/account/borrow-repay', 'POST']  # 尊享借币还币
    get_borrow_repay_history = ['/api/v5/account/borrow-repay-history', 'GET']  # 获取尊享借币还币历史
    get_vip_interest_accrued = ['/api/v5/account/vip-interest-accrued', 'GET']  # 获取尊享借币计息记录
    get_vip_interest_deducted = ['/api/v5/account/vip-interest-deducted', 'GET']  # 获取尊享借币扣息记录
    get_vip_loan_order_list = ['/api/v5/account/vip-loan-order-list', 'GET']  # 尊享借币订单列表
    get_vip_loan_order_detail = ['/api/v5/account/vip-loan-order-detail', 'GET']  # 尊享借币订单详情
    get_interest_limits = ['/api/v5/account/interest-limits', 'GET']  # 获取借币利率与限额
    set_simulated_margin = ['/api/v5/account/simulated_margin', 'POST']  # 组合保证金的虚拟持仓保证金计算
    get_greeks = ['/api/v5/account/greeks', 'GET']  # 查看账户Greeks
    get_position_tiers = ['/api/v5/account/position-tiers', 'GET']  # 获取组合保证金模式全仓限制
    set_set_riskOffset_type = ['/api/v5/account/set-riskOffset-type', 'POST']  # 设置组合保证金账户风险对冲模式
    set_activate_option = ['/api/v5/account/activate-option', 'POST']  # 开通期权交易


class Account(Client):
    # 查看账户余额
    def get_balance(self, ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-balance
        '''
        return self.send_request(*_AccountEndpoints.get_balance, **to_local(locals()))

    # 查看持仓信息
    def get_positions(self, instType: str = '', instId: str = '', posId: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-positions
        '''
        return self.send_request(*_AccountEndpoints.get_positions, **to_local(locals()))

    # 查看历史持仓信息
    def get_positions_history(self, instType: str = '', instId: str = '', mgnMode: str = '', type: str = '',
                              posId: str = '', after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-positions-history
        '''
        return self.send_request(*_AccountEndpoints.get_positions_history, **to_local(locals()))

    # 查看账户持仓风险
    def get_account_position_risk(self, instType: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-account-and-position-risk
        '''
        return self.send_request(*_AccountEndpoints.get_account_position_risk, **to_local(locals()))

    # 账单流水查询（近七天）
    def get_bills(self, instType: str = '', ccy: str = '', mgnMode: str = '', ctType: str = '', type: str = '',
                  subType: str = '', after: str = '', before: str = '', begin: str = '', end: str = '',
                  limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-bills-details-last-7-days
        '''
        return self.send_request(*_AccountEndpoints.get_bills, **to_local(locals()))

    # 账单流水查询（近三月）
    def get_bills_archive(self, instType: str = '', ccy: str = '', mgnMode: str = '', ctType: str = '', type: str = '',
                          subType: str = '', after: str = '', before: str = '', begin: str = '', end: str = '',
                          limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-bills-details-last-3-months
        '''
        return self.send_request(*_AccountEndpoints.get_bills_archive, **to_local(locals()))

    # 查看账户配置
    def get_config(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-account-configuration
        '''
        return self.send_request(*_AccountEndpoints.get_config, **to_local(locals()))

    # 设置持仓模式
    def set_set_position_mode(self, posMode: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-set-position-mode
        '''
        return self.send_request(*_AccountEndpoints.set_set_position_mode, **to_local(locals()))

    # 设置杠杆倍数
    def set_set_leverage(self, lever: str, mgnMode: str, instId: str = '', ccy: str = '', posSide: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-set-leverage
        '''
        return self.send_request(*_AccountEndpoints.set_set_leverage, **to_local(locals()))

    # 获取最大可买卖/开仓数量
    def get_max_size(self, instId: str, tdMode: str, ccy: str = '', px: str = '', leverage: str = '',
                     unSpotOffset: bool = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-maximum-buy-sell-amount-or-open-amount
        '''
        return self.send_request(*_AccountEndpoints.get_max_size, **to_local(locals()))

    # 获取最大可用数量
    def get_max_avail_size(self, instId: str, tdMode: str, ccy: str = '', reduceOnly: bool = '',
                           unSpotOffset: bool = '', quickMgnType: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-maximum-available-tradable-amount
        '''
        return self.send_request(*_AccountEndpoints.get_max_avail_size, **to_local(locals()))

    # 调整保证金
    def set_margin_balance(self, instId: str, posSide: str, type: str, amt: str, ccy: str = '', auto: bool = '',
                           loanTrans: bool = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-increase-decrease-margin
        '''
        return self.send_request(*_AccountEndpoints.set_margin_balance, **to_local(locals()))

    # 获取杠杆倍数
    def get_leverage_info(self, instId: str, mgnMode: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-leverage
        '''
        return self.send_request(*_AccountEndpoints.get_leverage_info, **to_local(locals()))

    # 获取交易产品最大可借
    def get_max_loan(self, instId: str, mgnMode: str, mgnCcy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-the-maximum-loan-of-instrument
        '''
        return self.send_request(*_AccountEndpoints.get_max_loan, **to_local(locals()))

    # 获取当前账户交易手续费费率
    def get_trade_fee(self, instType: str, instId: str = '', uly: str = '', instFamily: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-fee-rates
        '''
        return self.send_request(*_AccountEndpoints.get_trade_fee, **to_local(locals()))

    # 获取计息记录
    def get_interest_accrued(self, type: str = '', ccy: str = '', instId: str = '', mgnMode: str = '', after: str = '',
                             before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-interest-accrued-data
        '''
        return self.send_request(*_AccountEndpoints.get_interest_accrued, **to_local(locals()))

    # 获取用户当前杠杆借币利率
    def get_interest_rate(self, ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-interest-rate
        '''
        return self.send_request(*_AccountEndpoints.get_interest_rate, **to_local(locals()))

    # 期权greeks的PA/BS切换
    def set_set_greeks(self, greeksType: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-set-greeks-pa-bs
        '''
        return self.send_request(*_AccountEndpoints.set_set_greeks, **to_local(locals()))

    # 逐仓交易设置
    def set_set_isolated_mode(self, isoMode: str, type: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-isolated-margin-trading-settings
        '''
        return self.send_request(*_AccountEndpoints.set_set_isolated_mode, **to_local(locals()))

    # 查看账户最大可转余额
    def get_max_withdrawal(self, ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-maximum-withdrawals
        '''
        return self.send_request(*_AccountEndpoints.get_max_withdrawal, **to_local(locals()))

    # 查看账户特定风险状态
    def get_risk_state(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-account-risk-state
        '''
        return self.send_request(*_AccountEndpoints.get_risk_state, **to_local(locals()))

    # 一键借币模式手动借币还币
    def set_quick_margin_borrow_repay(self, instId: str, ccy: str, side: str, amt: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-manual-borrow-and-repay-in-quick-margin-mode
        '''
        return self.send_request(*_AccountEndpoints.set_quick_margin_borrow_repay, **to_local(locals()))

    # 获取一键借币还币历史
    def get_quick_margin_borrow_repay_history(self, instId: str = '', ccy: str = '', side: str = '', after: str = '',
                                              before: str = '', begin: str = '', end: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-manual-borrow-and-repay-history-in-quick-margin-mode
        '''
        return self.send_request(*_AccountEndpoints.get_quick_margin_borrow_repay_history, **to_local(locals()))

    # 尊享借币还币
    def set_borrow_repay(self, ccy: str, side: str, amt: str, ordId: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-vip-loans-borrow-and-repay
        '''
        return self.send_request(*_AccountEndpoints.set_borrow_repay, **to_local(locals()))

    # 获取尊享借币还币历史
    def get_borrow_repay_history(self, ccy: str = '', after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-borrow-and-repay-history-for-vip-loans
        '''
        return self.send_request(*_AccountEndpoints.get_borrow_repay_history, **to_local(locals()))

    # 获取尊享借币计息记录
    def get_vip_interest_accrued(self, ccy: str = '', ordId: str = '', after: str = '', before: str = '',
                                 limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-vip-interest-accrued-data
        '''
        return self.send_request(*_AccountEndpoints.get_vip_interest_accrued, **to_local(locals()))

    # 获取尊享借币扣息记录
    def get_vip_interest_deducted(self, ordId: str = '', ccy: str = '', after: str = '', before: str = '',
                                  limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-vip-interest-deducted-data
        '''
        return self.send_request(*_AccountEndpoints.get_vip_interest_deducted, **to_local(locals()))

    # 尊享借币订单列表
    def get_vip_loan_order_list(self, ordId: str = '', state: str = '', ccy: str = '', after: str = '',
                                before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-vip-loan-order-list
        '''
        return self.send_request(*_AccountEndpoints.get_vip_loan_order_list, **to_local(locals()))

    # 尊享借币订单详情
    def get_vip_loan_order_detail(self, ordId: str, ccy: str = '', after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-vip-loan-order-detail
        '''
        return self.send_request(*_AccountEndpoints.get_vip_loan_order_detail, **to_local(locals()))

    # 获取借币利率与限额
    def get_interest_limits(self, type: str = '', ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-borrow-interest-and-limit
        '''
        return self.send_request(*_AccountEndpoints.get_interest_limits, **to_local(locals()))

    # 组合保证金的虚拟持仓保证金计算
    def set_simulated_margin(self, instType: str = '', inclRealPos: bool = '', spotOffsetType: str = '',
                             simPos: object = '', instId: str = '', pos: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-position-builder
        '''
        return self.send_request(*_AccountEndpoints.set_simulated_margin, **to_local(locals()))

    # 查看账户Greeks
    def get_greeks(self, ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-greeks
        '''
        return self.send_request(*_AccountEndpoints.get_greeks, **to_local(locals()))

    # 获取组合保证金模式全仓限制
    def get_position_tiers(self, instType: str, uly: str = '', instFamily: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-get-pm-limitation
        '''
        return self.send_request(*_AccountEndpoints.get_position_tiers, **to_local(locals()))

    # 设置组合保证金账户风险对冲模式
    def set_set_riskOffset_type(self, type: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-set-risk-offset-type
        '''
        return self.send_request(*_AccountEndpoints.set_set_riskOffset_type, **to_local(locals()))

    # 开通期权交易
    def set_activate_option(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-account-activate-option
        '''
        return self.send_request(*_AccountEndpoints.set_activate_option, **to_local(locals()))
