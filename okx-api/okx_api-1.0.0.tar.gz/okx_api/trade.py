from paux.param import to_local
from okx_api._client import Client


class _TradeEndpoints:
    set_order = ['/api/v5/trade/order', 'POST']  # 下单
    set_batch_orders = ['/api/v5/trade/batch-orders', 'POST']  # 批量下单
    set_cancel_order = ['/api/v5/trade/cancel-order', 'POST']  # 撤单
    set_cancel_batch_orders = ['/api/v5/trade/cancel-batch-orders', 'POST']  # 批量撤单
    set_amend_order = ['/api/v5/trade/amend-order', 'POST']  # 修改订单
    set_amend_batch_orders = ['/api/v5/trade/amend-batch-orders', 'POST']  # 批量修改订单
    set_close_position = ['/api/v5/trade/close-position', 'POST']  # 市价仓位全平
    get_order = ['/api/v5/trade/order', 'GET']  # 获取订单信息
    get_orders_pending = ['/api/v5/trade/orders-pending', 'GET']  # 获取未成交订单列表
    get_orders_history = ['/api/v5/trade/orders-history', 'GET']  # 获取历史订单记录（近七天）
    get_orders_history_archive = ['/api/v5/trade/orders-history-archive', 'GET']  # 获取历史订单记录（近三个月）
    get_fills = ['/api/v5/trade/fills', 'GET']  # 获取成交明细（近三天）
    get_fills_history = ['/api/v5/trade/fills-history', 'GET']  # 获取成交明细（近三个月）
    set_order_algo = ['/api/v5/trade/order-algo', 'POST']  # 策略委托下单
    set_cancel_algos = ['/api/v5/trade/cancel-algos', 'POST']  # 撤销策略委托订单
    set_cancel_advance_algos = ['/api/v5/trade/cancel-advance-algos', 'POST']  # 撤销高级策略委托订单
    get_orders_algo_pending = ['/api/v5/trade/orders-algo-pending', 'GET']  # 获取未完成策略委托单列表
    get_orders_algo_history = ['/api/v5/trade/orders-algo-history', 'GET']  # 获取历史策略委托单列表
    get_easy_convert_currency_list = ['/api/v5/trade/easy-convert-currency-list', 'GET']  # 获取一键兑换主流币币种列表
    set_easy_convert = ['/api/v5/trade/easy-convert', 'POST']  # 一键兑换主流币交易
    get_easy_convert_history = ['/api/v5/trade/easy-convert-history', 'GET']  # 获取一键兑换主流币历史记录
    get_one_click_repay_currency_list = ['/api/v5/trade/one-click-repay-currency-list', 'GET']  # 获取一键还债币种列表
    set_one_click_repay = ['/api/v5/trade/one-click-repay', 'POST']  # 一键还债交易
    get_one_click_repay_history = ['/api/v5/trade/one-click-repay-history', 'GET']  # 获取一键还债历史记录


class Trade(Client):
    # 下单
    def set_order(self, instId: str, tdMode: str, side: str, ordType: str, sz: str, ccy: str = '', clOrdId: str = '',
                  tag: str = '', posSide: str = '', px: str = '', reduceOnly: bool = '', tgtCcy: str = '',
                  banAmend: bool = '', tpTriggerPx: str = '', tpOrdPx: str = '', slTriggerPx: str = '',
                  slOrdPx: str = '', tpTriggerPxType: str = '', slTriggerPxType: str = '', quickMgnType: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-place-order
        '''
        return self.send_request(*_TradeEndpoints.set_order, **to_local(locals()))

    # 批量下单
    def set_batch_orders(self, instId: str, tdMode: str, side: str, ordType: str, sz: str, ccy: str = '',
                         clOrdId: str = '', tag: str = '', posSide: str = '', px: str = '', reduceOnly: bool = '',
                         tgtCcy: str = '', banAmend: bool = '', tpTriggerPx: str = '', tpOrdPx: str = '',
                         slTriggerPx: str = '', slOrdPx: str = '', tpTriggerPxType: str = '', slTriggerPxType: str = '',
                         quickMgnType: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-place-multiple-orders
        '''
        return self.send_request(*_TradeEndpoints.set_batch_orders, **to_local(locals()))

    # 撤单
    def set_cancel_order(self, instId: str, ordId: str = '', clOrdId: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-cancel-order
        '''
        return self.send_request(*_TradeEndpoints.set_cancel_order, **to_local(locals()))

    # 批量撤单
    def set_cancel_batch_orders(self, instId: str, ordId: str = '', clOrdId: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-cancel-multiple-orders
        '''
        return self.send_request(*_TradeEndpoints.set_cancel_batch_orders, **to_local(locals()))

    # 修改订单
    def set_amend_order(self, instId: str, cxlOnFail: bool = '', ordId: str = '', clOrdId: str = '', reqId: str = '',
                        newSz: str = '', newPx: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-amend-order
        '''
        return self.send_request(*_TradeEndpoints.set_amend_order, **to_local(locals()))

    # 批量修改订单
    def set_amend_batch_orders(self, instId: str, cxlOnFail: bool = '', ordId: str = '', clOrdId: str = '',
                               reqId: str = '', newSz: str = '', newPx: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-amend-multiple-orders
        '''
        return self.send_request(*_TradeEndpoints.set_amend_batch_orders, **to_local(locals()))

    # 市价仓位全平
    def set_close_position(self, instId: str, mgnMode: str, posSide: str = '', ccy: str = '', autoCxl: bool = '',
                           clOrdId: str = '', tag: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-close-positions
        '''
        return self.send_request(*_TradeEndpoints.set_close_position, **to_local(locals()))

    # 获取订单信息
    def get_order(self, instId: str, ordId: str = '', clOrdId: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-get-order-details
        '''
        return self.send_request(*_TradeEndpoints.get_order, **to_local(locals()))

    # 获取未成交订单列表
    def get_orders_pending(self, instType: str = '', uly: str = '', instFamily: str = '', instId: str = '',
                           ordType: str = '', state: str = '', after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-get-order-list
        '''
        return self.send_request(*_TradeEndpoints.get_orders_pending, **to_local(locals()))

    # 获取历史订单记录（近七天）
    def get_orders_history(self, instType: str, uly: str = '', instFamily: str = '', instId: str = '',
                           ordType: str = '', state: str = '', category: str = '', after: str = '', before: str = '',
                           begin: str = '', end: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-get-order-history-last-7-days
        '''
        return self.send_request(*_TradeEndpoints.get_orders_history, **to_local(locals()))

    # 获取历史订单记录（近三个月）
    def get_orders_history_archive(self, instType: str, uly: str = '', instFamily: str = '', instId: str = '',
                                   ordType: str = '', state: str = '', category: str = '', after: str = '',
                                   before: str = '', begin: str = '', end: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-get-order-history-last-3-months
        '''
        return self.send_request(*_TradeEndpoints.get_orders_history_archive, **to_local(locals()))

    # 获取成交明细（近三天）
    def get_fills(self, instType: str = '', uly: str = '', instFamily: str = '', instId: str = '', ordId: str = '',
                  after: str = '', before: str = '', begin: str = '', end: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-get-transaction-details-last-3-days
        '''
        return self.send_request(*_TradeEndpoints.get_fills, **to_local(locals()))

    # 获取成交明细（近三个月）
    def get_fills_history(self, instType: str, uly: str = '', instFamily: str = '', instId: str = '', ordId: str = '',
                          after: str = '', before: str = '', begin: str = '', end: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-get-transaction-details-last-3-months
        '''
        return self.send_request(*_TradeEndpoints.get_fills_history, **to_local(locals()))

    # 策略委托下单
    def set_order_algo(self, instId: str, tdMode: str, side: str, ordType: str, ccy: str = '', posSide: str = '',
                       sz: str = '', tag: str = '', tgtCcy: str = '', reduceOnly: bool = '', clOrdId: str = '',
                       closeFraction: str = '', quickMgnType: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-place-algo-order
        '''
        return self.send_request(*_TradeEndpoints.set_order_algo, **to_local(locals()))

    # 撤销策略委托订单
    def set_cancel_algos(self, algoId: str, instId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-cancel-algo-order
        '''
        return self.send_request(*_TradeEndpoints.set_cancel_algos, **to_local(locals()))

    # 撤销高级策略委托订单
    def set_cancel_advance_algos(self, algoId: str, instId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-cancel-advance-algo-order
        '''
        return self.send_request(*_TradeEndpoints.set_cancel_advance_algos, **to_local(locals()))

    # 获取未完成策略委托单列表
    def get_orders_algo_pending(self, ordType: str, algoId: str = '', instType: str = '', instId: str = '',
                                after: str = '', before: str = '', limit: str = '', clOrdId: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-get-algo-order-list
        '''
        return self.send_request(*_TradeEndpoints.get_orders_algo_pending, **to_local(locals()))

    # 获取历史策略委托单列表
    def get_orders_algo_history(self, ordType: str, state: str = '', algoId: str = '', instType: str = '',
                                instId: str = '', after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-get-algo-order-history
        '''
        return self.send_request(*_TradeEndpoints.get_orders_algo_history, **to_local(locals()))

    # 获取一键兑换主流币币种列表
    def get_easy_convert_currency_list(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-get-easy-convert-currency-list
        '''
        return self.send_request(*_TradeEndpoints.get_easy_convert_currency_list, **to_local(locals()))

    # 一键兑换主流币交易
    def set_easy_convert(self, fromCcy: object, toCcy: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-place-easy-convert-rest-api-trade-easy-convert
        '''
        return self.send_request(*_TradeEndpoints.set_easy_convert, **to_local(locals()))

    # 获取一键兑换主流币历史记录
    def get_easy_convert_history(self, after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-get-easy-convert-history-rest-api-trade-easy-convert-history
        '''
        return self.send_request(*_TradeEndpoints.get_easy_convert_history, **to_local(locals()))

    # 获取一键还债币种列表
    def get_one_click_repay_currency_list(self, debtType: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-get-one-click-repay-currency-list-rest-api-trade-one-click-repay-currency-list
        '''
        return self.send_request(*_TradeEndpoints.get_one_click_repay_currency_list, **to_local(locals()))

    # 一键还债交易
    def set_one_click_repay(self, debtCcy: object, repayCcy: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-trade-one-click-repay-rest-api-trade-one-click-repay
        '''
        return self.send_request(*_TradeEndpoints.set_one_click_repay, **to_local(locals()))

    # 获取一键还债历史记录
    def get_one_click_repay_history(self, after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-trade-get-one-click-repay-history-rest-api-trade-one-click-repay-history
        '''
        return self.send_request(*_TradeEndpoints.get_one_click_repay_history, **to_local(locals()))
