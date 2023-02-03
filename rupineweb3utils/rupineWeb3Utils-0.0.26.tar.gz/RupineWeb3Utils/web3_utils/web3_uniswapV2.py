from web3 import Web3
from ..web3_utils import web3_globals, web3_generic

def get_liquidity_pool_address(connection, schema, w3:Web3,swap_contract_address:str,swap_contract_abi:str,chain_id:int,token0_address:str,token1_address:str,prodEnv:bool=True):
    swap_contract = w3.eth.contract(address=swap_contract_address, abi=swap_contract_abi)
    swap_contract_factory_address = swap_contract.functions.factory().call()
    swap_contract_factory_abi = web3_generic.getABI(connection, schema, swap_contract_factory_address,chain_id)
    swap_contract_factory = w3.eth.contract(address=swap_contract_factory_address, abi=swap_contract_factory_abi)
    try:
        return swap_contract_factory.functions.getPair(token0_address,token1_address).call()
    except Exception as e:
        return None

def get_lp_pool_reserves(connection, schema, w3:Web3,chain_id:int,lp_contract_address:str, prodEnv:bool=True, blocknumber='latest'):
    lp_contract_abi = web3_generic.getABI(connection, schema, w3.toChecksumAddress(lp_contract_address),chain_id)
    lp_contract_instance = w3.eth.contract(address=w3.toChecksumAddress(lp_contract_address), abi=lp_contract_abi)
    reserves = lp_contract_instance.functions.getReserves().call(None, blocknumber)
    result = {
        'blockTimestamp': reserves[2]
    }
    token0_address = lp_contract_instance.functions.token0().call()
    if token0_address == web3_globals.get_address_weth_or_wbnb(chain_id,w3):
        result.update({
            'WETH': reserves[0],
            'Token': reserves[1]
        })
    else:
        result.update({
            'WETH': reserves[1],
            'Token': reserves[0]
        })

    return result