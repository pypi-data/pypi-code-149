from web3 import Web3
from ..web3_utils import web3_globals, web3_generic
from uniswap import Uniswap

def get_liquidity_pool_address_uniswapV3(connection, schema, w3:Web3,swap_contract_address:str,swap_contract_abi:str,chain_id:int,token0_address:str,token1_address:str,prodEnv:bool=True):
    swap_router_abi = web3_generic.getABI(connection, schema, swap_contract_address, 1)
    swap_contract = w3.eth.contract(address=swap_contract_address, abi=swap_router_abi)
    swap_contract_factory_address = swap_contract.functions.factory().call()
    swap_contract_factory_abi = web3_generic.getABI(connection, schema, swap_contract_factory_address,1)
    swap_contract_factory = w3.eth.contract(address=swap_contract_factory_address, abi=swap_contract_factory_abi)

    lp_addr_ret = None
    lp_liq = 0
    fee = 0

    for i in [3000, 500, 10000, 100 ]:
        try:
            lp_addr = swap_contract_factory.functions.getPool(token0_address,token1_address, i).call()
            
            if lp_addr and lp_addr != '0x0000000000000000000000000000000000000000':
                tok_abi = web3_generic.getABI(connection, schema, token0_address, 1)
                tok_contract = w3.eth.contract(address=token0_address, abi=tok_abi)
                liq = tok_contract.functions.balanceOf(w3.toChecksumAddress(lp_addr)).call()

                if liq > lp_liq:
                    lp_addr_ret = lp_addr 
                    lp_liq = liq
                    fee = i
        except Exception as e:
            pass

    uniswap = Uniswap(None, None, None, w3, 3)
    price = uniswap.get_raw_price(token1_address, token0_address, fee) 

    return [lp_addr_ret, price]

def get_lp_pool_price(connection, schema, w3:Web3,chain_id:int,lp_contract_address:str):
    # WORK IN POGRESS (use get_liquidity_pool_address_uniswapV3 instead)
    lp_contract_abi = [{"inputs":[{"internalType":"uint32[]","name":"secondsAgos","type":"uint32[]"}],"name":"observe","outputs":[{"internalType":"int56[]","name":"tickCumulatives","type":"int56[]"},{"internalType":"uint160[]","name":"secondsPerLiquidityCumulativeX128s","type":"uint160[]"}],"stateMutability":"view","type":"function"}]
    lp_contract_instance = w3.eth.contract(address=w3.toChecksumAddress(lp_contract_address), abi=lp_contract_abi)
    # Converting UniswapV3 return values to a prive is a nightmare
    retVal = lp_contract_instance.functions.observe([3600,0]).call()
    print(retVal)

