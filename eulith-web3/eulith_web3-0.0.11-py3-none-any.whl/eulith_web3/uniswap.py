from enum import Enum
from typing import Optional, TypedDict

from eth_typing import ChecksumAddress

from eulith_web3.contract_bindings.i_uniswap_v3_pool import IUniswapV3Pool
from eulith_web3.erc20 import EulithERC20
from eulith_web3.exceptions import EulithRpcException


class UniswapV3PoolFee(int, Enum):
    FiveBips = 500
    ThirtyBips = 3000
    OneHundredBips = 10000


class EulithUniV3StartLoanRequest(TypedDict):
    borrow_token_a: EulithERC20
    borrow_amount_a: float
    borrow_token_b: Optional[EulithERC20]
    borrow_amount_b: Optional[float]
    pay_transfer_from: Optional[ChecksumAddress]
    recipient: Optional[ChecksumAddress]


class EulithUniV3StartSwapRequest(TypedDict):
    sell_token: EulithERC20
    sell_amount: float
    pool_address: ChecksumAddress
    fill_or_kill: bool
    sqrt_limit_price: str
    recipient: Optional[ChecksumAddress]
    pay_transfer_from: Optional[ChecksumAddress]


class EulithUniV3SwapQuoteRequest(TypedDict):
    sell_token: EulithERC20
    buy_token: EulithERC20
    sell_amount: float
    fee: Optional[UniswapV3PoolFee]


class EulithUniswapPoolLookupRequest(TypedDict):
    token_a: EulithERC20
    token_b: EulithERC20
    fee: UniswapV3PoolFee


class EulithUniswapV3Pool(IUniswapV3Pool):
    def __init__(self, eulith_web3,
                 pool_address: ChecksumAddress,
                 fee: Optional[UniswapV3PoolFee],
                 token0: Optional[ChecksumAddress],
                 token1: Optional[ChecksumAddress]):
        super().__init__(eulith_web3, pool_address)
        self.pool_fee = fee
        self.t0 = token0
        self.t1 = token1
        self.ew3 = eulith_web3

    def get_token_zero(self) -> EulithERC20:
        if not self.t0:
            self.t0 = self.ew3.toChecksumAddress(self.token0())
            return EulithERC20(self.ew3, self.t0)
        else:
            return EulithERC20(self.ew3, self.t0)

    def get_token_one(self) -> EulithERC20:
        if not self.t1:
            self.t1 = self.ew3.toChecksumAddress(self.token1())
            return EulithERC20(self.ew3, self.t1)
        else:
            return EulithERC20(self.ew3, self.t1)

    def get_fee(self) -> UniswapV3PoolFee:
        if not self.pool_fee:
            self.pool_fee = UniswapV3PoolFee(self.fee())
            return self.pool_fee
        else:
            return self.pool_fee

    def get_quote(self, sell_token: EulithERC20, sell_amount: float,
                  fill_or_kill: Optional[bool] = True,
                  recipient: Optional[ChecksumAddress] = None,
                  pay_transfer_from: Optional[ChecksumAddress] = None) -> (float, EulithUniV3StartSwapRequest):

        if sell_token.address != self.get_token_one().address and sell_token.address != self.get_token_zero().address:
            raise EulithRpcException("cannot start swap on pool with no matching sell token, "
                                     "please make sure you're requesting to swap with one of the pool's tokens")

        if sell_token.address == self.get_token_zero().address:
            buy_token = self.get_token_one()
        else:
            buy_token = self.get_token_zero()

        fee = self.get_fee()

        params = EulithUniV3SwapQuoteRequest(sell_token=sell_token, buy_token=buy_token,
                                             sell_amount=sell_amount, fee=fee)

        status, res = self.ew3.eulith_data.uniswap_v3_quote(params)

        if status:
            return self.ew3.parse_uni_quote_to_swap_request(res, fill_or_kill, recipient, pay_transfer_from)
        else:
            raise EulithRpcException(res)
