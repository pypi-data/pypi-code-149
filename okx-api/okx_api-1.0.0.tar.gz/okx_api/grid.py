from paux.param import to_local
from okx_api._client import Client


class _GridEndpoints:
    set_order_algo = ['/api/v5/tradingBot/grid/order-algo', 'POST']  # 网格策略委托下单
    set_amend_order_algo = ['/api/v5/tradingBot/grid/amend-order-algo', 'POST']  # 修改网格策略订单
    set_stop_order_algo = ['/api/v5/tradingBot/grid/stop-order-algo', 'POST']  # 网格策略停止
    get_orders_algo_pending = ['/api/v5/tradingBot/grid/orders-algo-pending', 'GET']  # 获取未完成网格策略委托单列表
    get_orders_algo_history = ['/api/v5/tradingBot/grid/orders-algo-history', 'GET']  # 获取历史网格策略委托单列表
    get_orders_algo_details = ['/api/v5/tradingBot/grid/orders-algo-details', 'GET']  # 获取网格策略委托订单详情
    get_sub_orders = ['/api/v5/tradingBot/grid/sub-orders', 'GET']  # 获取网格策略委托子订单信息
    get_positions = ['/api/v5/tradingBot/grid/positions', 'GET']  # 获取网格策略委托持仓
    set_withdraw_income = ['/api/v5/tradingBot/grid/withdraw-income', 'POST']  # 现货/天地网格提取利润
    set_compute_margin_balance = ['/api/v5/tradingBot/grid/compute-margin-balance', 'POST']  # 调整保证金计算
    set_margin_balance = ['/api/v5/tradingBot/grid/margin-balance', 'POST']  # 调整保证金
    get_ai_param = ['/api/v5/tradingBot/grid/ai-param', 'GET']  # 网格策略智能回测（公共）


class Grid(Client):
    # 网格策略委托下单
    def set_order_algo(self, instId: str, algoOrdType: str, maxPx: str, minPx: str, gridNum: str, runType: str = '',
                       tpTriggerPx: str = '', slTriggerPx: str = '', tag: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-grid-trading-place-grid-algo-order
        '''
        return self.send_request(*_GridEndpoints.set_order_algo, **to_local(locals()))

    # 修改网格策略订单
    def set_amend_order_algo(self, algoId: str, instId: str, slTriggerPx: str = '', tpTriggerPx: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-grid-trading-amend-grid-algo-order
        '''
        return self.send_request(*_GridEndpoints.set_amend_order_algo, **to_local(locals()))

    # 网格策略停止
    def set_stop_order_algo(self, algoId: str, instId: str, algoOrdType: str, stopType: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-grid-trading-stop-grid-algo-order
        '''
        return self.send_request(*_GridEndpoints.set_stop_order_algo, **to_local(locals()))

    # 获取未完成网格策略委托单列表
    def get_orders_algo_pending(self, algoOrdType: str, algoId: str = '', instId: str = '', instType: str = '',
                                after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-grid-trading-get-grid-algo-order-list
        '''
        return self.send_request(*_GridEndpoints.get_orders_algo_pending, **to_local(locals()))

    # 获取历史网格策略委托单列表
    def get_orders_algo_history(self, algoOrdType: str, algoId: str = '', instId: str = '', instType: str = '',
                                after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-grid-trading-get-grid-algo-order-history
        '''
        return self.send_request(*_GridEndpoints.get_orders_algo_history, **to_local(locals()))

    # 获取网格策略委托订单详情
    def get_orders_algo_details(self, algoOrdType: str, algoId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-grid-trading-get-grid-algo-order-details
        '''
        return self.send_request(*_GridEndpoints.get_orders_algo_details, **to_local(locals()))

    # 获取网格策略委托子订单信息
    def get_sub_orders(self, algoId: str, algoOrdType: str, type: str, groupId: str = '', after: str = '',
                       before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-grid-trading-get-grid-algo-sub-orders
        '''
        return self.send_request(*_GridEndpoints.get_sub_orders, **to_local(locals()))

    # 获取网格策略委托持仓
    def get_positions(self, algoOrdType: str, algoId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-grid-trading-get-grid-algo-order-positions
        '''
        return self.send_request(*_GridEndpoints.get_positions, **to_local(locals()))

    # 现货/天地网格提取利润
    def set_withdraw_income(self, algoId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-grid-trading-spot-moon-grid-withdraw-income
        '''
        return self.send_request(*_GridEndpoints.set_withdraw_income, **to_local(locals()))

    # 调整保证金计算
    def set_compute_margin_balance(self, algoId: str, type: str, amt: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-grid-trading-compute-margin-balance
        '''
        return self.send_request(*_GridEndpoints.set_compute_margin_balance, **to_local(locals()))

    # 调整保证金
    def set_margin_balance(self, algoId: str, type: str, amt: str = '', percent: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-grid-trading-adjust-margin-balance
        '''
        return self.send_request(*_GridEndpoints.set_margin_balance, **to_local(locals()))

    # 网格策略智能回测（公共）
    def get_ai_param(self, algoOrdType: str, instId: str, direction: str = '', duration: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-grid-trading-get-grid-ai-parameter-public
        '''
        return self.send_request(*_GridEndpoints.get_ai_param, **to_local(locals()))
