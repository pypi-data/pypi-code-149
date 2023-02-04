from paux.param import to_local
from okx_api._client import Client


class _ConvertEndpoints:
    get_currencies = ['/api/v5/asset/convert/currencies', 'GET']  # 获取闪兑币种列表
    get_currency_pair = ['/api/v5/asset/convert/currency-pair', 'GET']  # 获取闪兑币对信息
    set_estimate_quote = ['/api/v5/asset/convert/estimate-quote', 'POST']  # 闪兑预估询价
    set_trade = ['/api/v5/asset/convert/trade', 'POST']  # 闪兑交易
    get_history = ['/api/v5/asset/convert/history', 'GET']  # 获取闪兑交易历史


class Convert(Client):
    # 获取闪兑币种列表
    def get_currencies(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-convert-get-convert-currencies
        '''
        return self.send_request(*_ConvertEndpoints.get_currencies, **to_local(locals()))

    # 获取闪兑币对信息
    def get_currency_pair(self, fromCcy: str, toCcy: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-convert-get-convert-currency-pair
        '''
        return self.send_request(*_ConvertEndpoints.get_currency_pair, **to_local(locals()))

    # 闪兑预估询价
    def set_estimate_quote(self, baseCcy: str, quoteCcy: str, side: str, rfqSz: str, rfqSzCcy: str, clQReqId: str = '',
                           tag: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-convert-estimate-quote
        '''
        return self.send_request(*_ConvertEndpoints.set_estimate_quote, **to_local(locals()))

    # 闪兑交易
    def set_trade(self, quoteId: str, baseCcy: str, quoteCcy: str, side: str, sz: str, szCcy: str, clTReqId: str = '',
                  tag: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-convert-convert-trade
        '''
        return self.send_request(*_ConvertEndpoints.set_trade, **to_local(locals()))

    # 获取闪兑交易历史
    def get_history(self, after: str = '', before: str = '', limit: str = '', tag: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-convert-get-convert-history
        '''
        return self.send_request(*_ConvertEndpoints.get_history, **to_local(locals()))
