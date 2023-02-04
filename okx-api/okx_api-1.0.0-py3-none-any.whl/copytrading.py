from paux.param import to_local
from okx_api._client import Client


class _CopytradingEndpoints:
    get_current_subpositions = ['/api/v5/copytrading/current-subpositions', 'GET']  # 交易员获取当前带单
    get_subpositions_history = ['/api/v5/copytrading/subpositions-history', 'GET']  # 交易员获取历史带单
    set_algo_order = ['/api/v5/copytrading/algo-order', 'POST']  # 交易员止盈止损
    set_close_subposition = ['/api/v5/copytrading/close-subposition', 'POST']  # 交易员平仓
    get_instruments = ['/api/v5/copytrading/instruments', 'GET']  # 交易员获取带单合约
    set_set_instruments = ['/api/v5/copytrading/set-instruments', 'POST']  # 交易员修改带单合约
    get_profit_sharing_details = ['/api/v5/copytrading/profit-sharing-details', 'GET']  # 交易员历史分润明细
    get_total_profit_sharing = ['/api/v5/copytrading/total-profit-sharing', 'GET']  # 交易员历史分润汇总
    get_unrealized_profit_sharing_details = ['/api/v5/copytrading/unrealized-profit-sharing-details', 'GET']  # 交易员待分润明细


class Copytrading(Client):
    # 交易员获取当前带单
    def get_current_subpositions(self, instId: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-copy-trading-get-existing-leading-positions
        '''
        return self.send_request(*_CopytradingEndpoints.get_current_subpositions, **to_local(locals()))

    # 交易员获取历史带单
    def get_subpositions_history(self, instId: str = '', after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-copy-trading-get-leading-position-history
        '''
        return self.send_request(*_CopytradingEndpoints.get_subpositions_history, **to_local(locals()))

    # 交易员止盈止损
    def set_algo_order(self, subPosId: str, tpTriggerPx: str = '', slTriggerPx: str = '', tpTriggerPxType: str = '',
                       slTriggerPxType: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-copy-trading-place-leading-stop-order
        '''
        return self.send_request(*_CopytradingEndpoints.set_algo_order, **to_local(locals()))

    # 交易员平仓
    def set_close_subposition(self, subPosId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-copy-trading-close-leading-position
        '''
        return self.send_request(*_CopytradingEndpoints.set_close_subposition, **to_local(locals()))

    # 交易员获取带单合约
    def get_instruments(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-copy-trading-get-leading-instruments
        '''
        return self.send_request(*_CopytradingEndpoints.get_instruments, **to_local(locals()))

    # 交易员修改带单合约
    def set_set_instruments(self, instId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-copy-trading-set-leading-instruments
        '''
        return self.send_request(*_CopytradingEndpoints.set_set_instruments, **to_local(locals()))

    # 交易员历史分润明细
    def get_profit_sharing_details(self, after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-copy-trading-get-profit-sharing-details
        '''
        return self.send_request(*_CopytradingEndpoints.get_profit_sharing_details, **to_local(locals()))

    # 交易员历史分润汇总
    def get_total_profit_sharing(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-copy-trading-get-total-profit-sharing
        '''
        return self.send_request(*_CopytradingEndpoints.get_total_profit_sharing, **to_local(locals()))

    # 交易员待分润明细
    def get_unrealized_profit_sharing_details(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-copy-trading-get-unrealized-profit-sharing-details
        '''
        return self.send_request(*_CopytradingEndpoints.get_unrealized_profit_sharing_details, **to_local(locals()))
