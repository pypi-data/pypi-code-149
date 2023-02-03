import json
import random
import time

from ston.client import StonClient
from ston.__ton_client import TonClient
from tonsdk.contract.wallet import WalletVersionEnum, WalletContract, Wallets
from tonsdk.boc import begin_cell
from tonsdk.utils import bytes_to_b64str, to_nano, Address
from tvm_valuetypes import deserialize_cell_from_json

__ROUTER_ADDRESS = Address('0:779dcc815138d9500e449c5291e7f12738c23d575b5310000f6a253bd607384e')


def __get_contract_address(ton: TonClient, wallet_address: Address, token_address: Address):
    payload = begin_cell().store_address(wallet_address).end_cell()
    result = ton.call2(token_address.to_string(),
                       'get_wallet_address',
                       [['tvm.Slice', bytes_to_b64str(payload.to_boc(False))]])
    # believe me, it hurts more to write it, then to read it
    cell_obj = result[0]['stack'][0][1]['object']
    res_cell = deserialize_cell_from_json(json.dumps(cell_obj))
    return Address('0:' + res_cell.data.data[11:].tobytes().hex())


def __get_seqno(ton: TonClient):
    result = ton.seqno()
    num_obj = result[0]['stack'][0][1]
    return int(num_obj, 16)


def __random_query_id(t=0, e=2 ** 53 - 1) -> int:
    return random.randint(t, e)


def swap(wallet_mnemonics: str,
         bid_amount: float,
         bid_token_address: str,
         min_ask_amount: float,
         ask_token_address: str) -> bool:
    mnemonics = wallet_mnemonics.split(" ")
    _, _, _, wallet = Wallets.from_mnemonics(mnemonics, WalletVersionEnum.v4r2, 0)

    ton = TonClient(wallet.address.to_string())
    ston = StonClient.get_instance()

    query_id = __random_query_id()
    wallet_token_address = __get_contract_address(ton, wallet.address, Address(bid_token_address))
    router_token_address = __get_contract_address(ton, __ROUTER_ADDRESS, Address(ask_token_address))

    payload = (begin_cell()
               .store_uint(260734629, 32)
               .store_uint(query_id, 64)
               .store_coins(ston.to_decimals(bid_amount, bid_token_address))
               .store_address(__ROUTER_ADDRESS)
               .store_uint(0, 3)
               .store_coins(to_nano(0.26, 'ton'))
               .store_bit(1)
               .store_ref(begin_cell()
                          .store_uint(630424929, 32)
                          .store_address(router_token_address)
                          .store_coins(min_ask_amount)
                          .store_address(wallet.address)
                          .store_bit(0)
                          .end_cell())
               .end_cell())

    query = wallet.create_transfer_message(
        to_addr=wallet_token_address,
        amount=to_nano(0.3, 'ton'),
        seqno=__get_seqno(ton),
        payload=payload
    )
    ton.send_boc(query["message"].to_boc(False))

    retries = 30
    while retries > 0:
        res = ston.ston_request('dex.swap_status', {'query_id': str(query_id)})
        if 'result' in res and 'exit_code' in res['result'] and res['result']['exit_code'] == 'swap_ok':
            ston.stop_updating_data()
            return True
        else:
            retries -= 1
            time.sleep(2)

    ston.stop_updating_data()
    return False
