from paux.param import to_local
from okx_api._client import Client


class _MarketEndpoints:
    get_tickers = ['/api/v5/market/tickers', 'GET']  # 获取所有产品行情信息
    get_ticker = ['/api/v5/market/ticker', 'GET']  # 获取单个产品行情信息
    get_index_tickers = ['/api/v5/market/index-tickers', 'GET']  # 获取指数行情
    get_books = ['/api/v5/market/books', 'GET']  # 获取产品深度
    get_books_lite = ['/api/v5/market/books-lite', 'GET']  # 获取产品轻量深度
    get_candles = ['/api/v5/market/candles', 'GET']  # 获取交易产品K线数据
    get_history_candles = ['/api/v5/market/history-candles', 'GET']  # 获取交易产品历史K线数据
    get_index_candles = ['/api/v5/market/index-candles', 'GET']  # 获取指数K线数据
    get_history_index_candles = ['/api/v5/market/history-index-candles', 'GET']  # 获取指数历史K线数据
    get_mark_price_candles = ['/api/v5/market/mark-price-candles', 'GET']  # 获取标记价格K线数据
    get_history_mark_price_candles = ['/api/v5/market/history-mark-price-candles', 'GET']  # 获取标记价格历史K线数据
    get_trades = ['/api/v5/market/trades', 'GET']  # 获取交易产品公共成交数据
    get_history_trades = ['/api/v5/market/history-trades', 'GET']  # 获取交易产品公共历史成交数据
    get_instrument_family_trades = ['/api/v5/market/option/instrument-family-trades', 'GET']  # 获取期权品种公共成交数据
    get_platform_24_volume = ['/api/v5/market/platform-24-volume', 'GET']  # 获取平台24小时总成交量
    get_open_oracle = ['/api/v5/market/open-oracle', 'GET']  # Oracle  上链交易数据
    get_exchange_rate = ['/api/v5/market/exchange-rate', 'GET']  # 获取法币汇率
    get_index_components = ['/api/v5/market/index-components', 'GET']  # 获取指数成分数据
    get_block_tickers = ['/api/v5/market/block-tickers', 'GET']  # 获取大宗交易所有产品行情信息
    get_block_ticker = ['/api/v5/market/block-ticker', 'GET']  # 获取大宗交易单个产品行情信息
    get_block_trades = ['/api/v5/market/block-trades', 'GET']  # 获取大宗交易公共成交数据


class Market(Client):
    # 获取所有产品行情信息
    def get_tickers(self, instType: str, uly: str = '', instFamily: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-tickers
        '''
        return self.send_request(*_MarketEndpoints.get_tickers, **to_local(locals()))

    # 获取单个产品行情信息
    def get_ticker(self, instId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-ticker
        '''
        return self.send_request(*_MarketEndpoints.get_ticker, **to_local(locals()))

    # 获取指数行情
    def get_index_tickers(self, quoteCcy: str = '', instId: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-index-tickers
        '''
        return self.send_request(*_MarketEndpoints.get_index_tickers, **to_local(locals()))

    # 获取产品深度
    def get_books(self, instId: str, sz: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-order-book
        '''
        return self.send_request(*_MarketEndpoints.get_books, **to_local(locals()))

    # 获取产品轻量深度
    def get_books_lite(self, instId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-order-lite-book
        '''
        return self.send_request(*_MarketEndpoints.get_books_lite, **to_local(locals()))

    # 获取交易产品K线数据
    def get_candles(self, instId: str, bar: str = '', after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-candlesticks
        '''
        return self.send_request(*_MarketEndpoints.get_candles, **to_local(locals()))

    # 获取交易产品历史K线数据
    def get_history_candles(self, instId: str, after: str = '', before: str = '', bar: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-candlesticks-history
        '''
        return self.send_request(*_MarketEndpoints.get_history_candles, **to_local(locals()))

    # 获取指数K线数据
    def get_index_candles(self, instId: str, after: str = '', before: str = '', bar: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-index-candlesticks
        '''
        return self.send_request(*_MarketEndpoints.get_index_candles, **to_local(locals()))

    # 获取指数历史K线数据
    def get_history_index_candles(self, instId: str, after: str = '', before: str = '', bar: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-index-candlesticks-history
        '''
        return self.send_request(*_MarketEndpoints.get_history_index_candles, **to_local(locals()))

    # 获取标记价格K线数据
    def get_mark_price_candles(self, instId: str, after: str = '', before: str = '', bar: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-mark-price-candlesticks
        '''
        return self.send_request(*_MarketEndpoints.get_mark_price_candles, **to_local(locals()))

    # 获取标记价格历史K线数据
    def get_history_mark_price_candles(self, instId: str, after: str = '', before: str = '', bar: str = '',
                                       limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-mark-price-candlesticks-history
        '''
        return self.send_request(*_MarketEndpoints.get_history_mark_price_candles, **to_local(locals()))

    # 获取交易产品公共成交数据
    def get_trades(self, instId: str, limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-trades
        '''
        return self.send_request(*_MarketEndpoints.get_trades, **to_local(locals()))

    # 获取交易产品公共历史成交数据
    def get_history_trades(self, instId: str, type: str = '', after: str = '', before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-trades-history
        '''
        return self.send_request(*_MarketEndpoints.get_history_trades, **to_local(locals()))

    # 获取期权品种公共成交数据
    def get_instrument_family_trades(self, instFamily: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-option-trades
        '''
        return self.send_request(*_MarketEndpoints.get_instrument_family_trades, **to_local(locals()))

    # 获取平台24小时总成交量
    def get_platform_24_volume(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-24h-total-volume
        '''
        return self.send_request(*_MarketEndpoints.get_platform_24_volume, **to_local(locals()))

    # Oracle  上链交易数据
    def get_open_oracle(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-oracle
        '''
        return self.send_request(*_MarketEndpoints.get_open_oracle, **to_local(locals()))

    # 获取法币汇率
    def get_exchange_rate(self, ):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-exchange-rate
        '''
        return self.send_request(*_MarketEndpoints.get_exchange_rate, **to_local(locals()))

    # 获取指数成分数据
    def get_index_components(self, index: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-index-components
        '''
        return self.send_request(*_MarketEndpoints.get_index_components, **to_local(locals()))

    # 获取大宗交易所有产品行情信息
    def get_block_tickers(self, instType: str, uly: str = '', instFamily: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-block-tickers
        '''
        return self.send_request(*_MarketEndpoints.get_block_tickers, **to_local(locals()))

    # 获取大宗交易单个产品行情信息
    def get_block_ticker(self, instId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-block-ticker
        '''
        return self.send_request(*_MarketEndpoints.get_block_tickers, **to_local(locals()))

    # 获取大宗交易公共成交数据
    def get_block_trades(self, instId: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-block-trades
        '''
        return self.send_request(*_MarketEndpoints.get_block_trades, **to_local(locals()))
