from paux.param import to_local
from okx_api._client import Client


class _StakingEndpoints:
    get_offers = ['/api/v5/finance/staking-defi/offers', 'GET']  # 查看项目
    set_purchase = ['/api/v5/finance/staking-defi/purchase', 'POST']  # 申购项目
    set_redeem = ['/api/v5/finance/staking-defi/redeem', 'POST']  # 赎回项目
    set_cancel = ['/api/v5/finance/staking-defi/cancel', 'POST']  # 撤销项目申购/赎回
    get_orders_active = ['/api/v5/finance/staking-defi/orders-active', 'GET']  # 查看活跃订单
    get_orders_history = ['/api/v5/finance/staking-defi/orders-history', 'GET']  # 查看历史订单


class Staking(Client):
    # 查看项目
    def get_offers(self, productId: str = '', protocolType: str = '', ccy: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-earn-get-offers
        '''
        return self.send_request(*_StakingEndpoints.get_offers, **to_local(locals()))

    # 申购项目
    def set_purchase(self, productId: str, investData: object, ccy:str, amt:str, term: str = '', tag: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-earn-purchase
        '''
        return self.send_request(*_StakingEndpoints.set_purchase, **to_local(locals()))

    # 赎回项目
    def set_redeem(self, ordId: str, protocolType: str, allowEarlyRedeem: bool = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-earn-redeem
        '''
        return self.send_request(*_StakingEndpoints.set_redeem, **to_local(locals()))

    # 撤销项目申购/赎回
    def set_cancel(self, ordId: str, protocolType: str):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-earn-cancel-purchases-redemptions
        '''
        return self.send_request(*_StakingEndpoints.set_cancel, **to_local(locals()))

    # 查看活跃订单
    def get_orders_active(self, productId: str = '', protocolType: str = '', ccy: str = '', state: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-earn-get-active-orders
        '''
        return self.send_request(*_StakingEndpoints.get_orders_active, **to_local(locals()))

    # 查看历史订单
    def get_orders_history(self, productId: str = '', protocolType: str = '', ccy: str = '', after: str = '',
                           before: str = '', limit: str = ''):
        '''
        https://www.okx.com/docs-v5/zh/#rest-api-earn-get-order-history
        '''
        return self.send_request(*_StakingEndpoints.get_orders_history, **to_local(locals()))
